import abjad
from . import pitch

# import muda
import re
import sys
import subprocess

# Tenta importar pyphen, se não estiver disponível, sugere instalação
try:
    import pyphen

    PYPHEM_AVAILABLE = True
except ImportError:
    PYPHEM_AVAILABLE = False
    print(
        "Aviso: A biblioteca 'pyphen' não está instalada. "
        "Para usar a separação silábica, instale com: pip install pyphen"
    )

# sílaba, nota para régua, número de notas para música
# neste caso, 5 seria 4 grace notes mais uma semínima


def syllabify(text: str, language: str = "pt_BR") -> list[list[str]]:
    """
    Divide um texto em sílabas por palavra.

    Args:
        text: String de entrada.
        language: Código de idioma para o pyphen (padrão: 'pt_BR').

    Returns:
        Lista de listas, onde cada sublista contém as sílabas de uma palavra.

    Exemplo:
        >>> syllabify("Resquício de qualquer")
        [['Res', 'quí', 'cio'], ['de'], ['qual', 'quer']]
    """
    if not PYPHEM_AVAILABLE:
        raise ImportError(
            "A biblioteca 'pyphen' é necessária para a separação silábica. "
            "Instale com: pip install pyphen"
        )

    dic = pyphen.Pyphen(lang=language)
    words = re.findall(
        r"\b[\w'ãõáéíóúâêîôûàèìòùäëïöüç]+\b", text, re.IGNORECASE
    )
    result = []
    for word in words:
        hyphenated = dic.inserted(word, hyphen="\u00AD")  # soft hyphen
        syllables = [
            syl.strip() for syl in hyphenated.split("\u00AD") if syl.strip()
        ]
        if syllables:
            result.append(syllables)
    return result


def tonic_syllable_index(word: str, language: str = "pt_BR") -> int:
    """
    Retorna o índice (0‑based) da sílaba tônica de uma palavra em português.

    Usa acentos gráficos para determinar a tônica. Se não houver acento,
    assume padrão paroxítona (penúltima sílaba), exceto para palavras terminadas
    em 'r', 'l', 'z', 'x', 'n', 's' (oxítonas) ou vogais nasaladas (oxítonas).
    """
    if not PYPHEM_AVAILABLE:
        raise ImportError(
            "A biblioteca 'pyphen' é necessária. Instale com: pip install pyphen"
        )
    dic = pyphen.Pyphen(lang=language)
    hyphenated = dic.inserted(word, hyphen="\u00AD")
    syllables = [
        syl.strip() for syl in hyphenated.split("\u00AD") if syl.strip()
    ]
    if not syllables:
        return 0

    # 1. Verifica acentos gráficos
    tonic_accents = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "â": "a",
        "ê": "e",
        "ô": "o",
        "ã": "a",
        "õ": "o",
        "à": "a",
        "è": "e",
        "ì": "i",
        "ò": "o",
        "ù": "u",
        "ä": "a",
        "ë": "e",
        "ï": "i",
        "ö": "o",
        "ü": "u",
    }
    for i, syl in enumerate(syllables):
        for accented_char, base_char in tonic_accents.items():
            if accented_char in syl.lower():
                return i

    # 2. Se não houver acento, aplica regras de posição
    last_char = word[-1].lower()
    # Oxítonas: terminadas em r, l, z, x, n, s (exceto se forem plurais 'ns' ou 'ões'?)
    # Também vogais nasaladas (ã, õ) já foram capturadas acima.
    oxitona_endings = {"r", "l", "z", "x", "n", "s"}
    # Verifica se a última letra é consoante oxítona e a palavra tem mais de uma sílaba
    if last_char in oxitona_endings and len(syllables) > 1:
        # Mas cuidado com plurais 'ns' (ex: 'bons' -> paroxítona)
        if word.lower().endswith("ns"):
            pass  # trata como paroxítona
        else:
            return len(syllables) - 1  # última sílaba

    # 3. Padrão paroxítona (penúltima sílaba)
    if len(syllables) >= 2:
        return len(syllables) - 2
    else:
        return 0  # monossílabo


def syllable_durations(word: str, language: str = "pt_BR") -> list[float]:
    """
    Retorna durações relativas (valores float) para cada sílaba da palavra.

    A sílaba tônica recebe duração 1.5, as adjacentes 1.0,
    as demais 0.8. Monossílabos recebem 1.0.
    """
    if not PYPHEM_AVAILABLE:
        raise ImportError(
            "A biblioteca 'pyphen' é necessária. Instale com: pip install pyphen"
        )
    dic = pyphen.Pyphen(lang=language)
    hyphenated = dic.inserted(word, hyphen="\u00AD")
    syllables = [
        syl.strip() for syl in hyphenated.split("\u00AD") if syl.strip()
    ]
    if not syllables:
        return []

    tonic_idx = tonic_syllable_index(word, language)
    durations = []
    for i in range(len(syllables)):
        if i == tonic_idx:
            durations.append(1.5)
        elif abs(i - tonic_idx) == 1:
            durations.append(1.0)
        else:
            durations.append(0.8)

    # Ajusta monossílabos para 1.0
    if len(syllables) == 1:
        durations = [1.0]

    return durations


def syllabify_with_durations(
    text: str,
    language: str = "pt_BR",
    base_duration: abjad.Duration = abjad.Duration(1, 8),
) -> list[tuple[list[str], list[abjad.Duration]]]:
    """
    Separa o texto em palavras e, para cada palavra, retorna suas sílabas
    e durações musicais calculadas a partir dos pesos relativos.

    Args:
        text: String de entrada.
        language: Código de idioma para pyphen.
        base_duration: Duração que corresponde ao peso 1.0.

    Returns:
        Lista de tuplas (sílabas, durações) para cada palavra.
    """
    if not PYPHEM_AVAILABLE:
        raise ImportError(
            "A biblioteca 'pyphen' é necessária. Instale com: pip install pyphen"
        )
    words = re.findall(
        r"\b[\w'ãõáéíóúâêîôûàèìòùäëïöüç]+\b", text, re.IGNORECASE
    )
    result = []
    for word in words:
        syllables = syllabify(word, language)[0]  # uma palavra por vez
        rel_durations = syllable_durations(word, language)
        # Converte pesos relativos em durações musicais
        abs_durations = [base_duration * (rel / 1.0) for rel in rel_durations]
        result.append((syllables, abs_durations))
    return result


def syllabify_to_lilypond(
    text: str,
    language: str = "pt_BR",
    separator: str = " -- ",
    keep_punctuation: bool = False,
) -> str:
    """
    Converte um texto para formato LilyPond com sílabas separadas.

    Args:
        text: String de entrada.
        language: Código de idioma para pyphen.
        separator: Separador entre sílabas (padrão: " -- ").
        keep_punctuation: Se True, mantém pontuação original.

    Returns:
        String formatada para LilyPond.

    Exemplo:
        >>> syllabify_to_lilypond("Resquício de qualquer")
        "Res -- quí -- cio de qual -- quer"
    """
    if not PYPHEM_AVAILABLE:
        raise ImportError(
            "A biblioteca 'pyphen' é necessária. Instale com: pip install pyphen"
        )

    if keep_punctuation:
        # Preserva pontuação dividindo por palavras mas mantendo espaços e pontuação
        pattern = re.compile(r"(\b[\w'ãõáéíóúâêîôûàèìòùäëïöüç]+\b|[^\w\s])")
        tokens = pattern.findall(text)
        dic = pyphen.Pyphen(lang=language)
        result_parts = []
        for token in tokens:
            if re.match(
                r"\b[\w'ãõáéíóúâêîôûàèìòùäëïöüç]+\b", token, re.IGNORECASE
            ):
                hyphenated = dic.inserted(token, hyphen="\u00AD")
                syllables = [
                    syl.strip()
                    for syl in hyphenated.split("\u00AD")
                    if syl.strip()
                ]
                if syllables:
                    result_parts.append(separator.join(syllables))
            else:
                result_parts.append(token)
        # Reconstroi mantendo espaços
        return " ".join(result_parts).replace("  ", " ")
    else:
        # Comportamento simples: apenas palavras
        syllabified = syllabify(text, language)
        words_with_syllables = []
        for syllables in syllabified:
            if len(syllables) > 1:
                words_with_syllables.append(separator.join(syllables))
            else:
                words_with_syllables.append(syllables[0])
        return " ".join(words_with_syllables)


def make_lyrics_rule_and_music(verses: list[list] = None):
    lyrics = []
    rule = abjad.Container()
    music = abjad.Container()
    for i, verse in enumerate(verses):
        # sílaba, nota para régua, número de notas para música
        # neste caso, 5 seria 4 grace notes mais uma semínima
        vlyr = ""
        vrule = abjad.Container(name="r1")
        vmusic = abjad.Container(name="m1")
        v1 = [
            ("we", 1, 1, "(", ".", "pp"),
            ("dream", 1, 5),
            ("to --", 1, 1),
            ("ge --", 1, 1),
            ("ther", 1, 2),
            ("", -1, -1),
            ("we", 1, -1),
            ('"wake up and"', 3, 1),
            ("keep", 1, 1),
            ("drea --", 1, 5),
            ("ming", 1, 1),
        ]
        if verses is None:
            verses = [v1]

        for tup in verses[0]:
            # lyrics
            vlyr += tup[0] + " "

            # rule
            if tup[1] > 0:
                vrule.append(abjad.Note("c'4", multiplier=(tup[1])))
            elif tup[1] < 0:
                vrule.append(abjad.Rest((1, 4), multiplier=(abs(tup[1]))))

            # music
            if tup[2] > 0:
                grace_string = ""
                note = abjad.Note("c'4", multiplier=(tup[1]))
                if tup[2] > 1:
                    for i in range(tup[2] - 1):
                        grace_string += "c'16 "
                        grace = abjad.BeforeGraceContainer(grace_string)
                        abjad.attach(grace, note)
                vmusic.append(note)
            elif tup[2] < 0:
                vmusic.append(abjad.Rest((1, 4), multiplier=(abs(tup[1]))))

        def articulations(attachable):
            # articulations
            if tup[3]:
                for string in tup[3:]:
                    if string == "(":
                        abjad.attach(abjad.StartSlur(), attachable)
                    if string == ")":
                        abjad.attach(abjad.StopSlur(), attachable)
                    if abjad.is_articulation:
                        abjad.attach(abjad.Articulation(string), attachable)

        lyrics.append(vlyr)
        rule.extend(vrule)
        music.extend(vmusic)

    return lyrics, rule, music


def main():
    # Demonstração das novas funções de separação silábica
    print("=== Teste de separação silábica ===")
    test_text = "Resquício de qualquer relíquia"
    try:
        syllables = syllabify(test_text)
        print(f"Entrada: {test_text}")
        print(f"Sílabas por palavra: {syllables}")

        lily_text = syllabify_to_lilypond(test_text)
        print(f"Formato LilyPond: {lily_text}")

        # Teste com pontuação
        test_with_punct = "Olá, mundo! Como vai você?"
        lily_with_punct = syllabify_to_lilypond(
            test_with_punct, keep_punctuation=True
        )
        print(f"\nCom pontuação: {test_with_punct}")
        print(f"LilyPond com pontuação: {lily_with_punct}")

        # Novas funções de duração
        print("\n=== Estimativa de durações por sílaba ===")
        words = ["Resquício", "qualquer", "relíquia", "mundo", "você"]
        for w in words:
            idx = tonic_syllable_index(w)
            durs = syllable_durations(w)
            print(f"{w}: tônica índice {idx}, durações relativas {durs}")

        # Exemplo com syllabify_with_durations
        print("\n=== Durações musicais (base = 1/8) ===")
        result = syllabify_with_durations(
            "Resquício qualquer", base_duration=abjad.Duration(1, 8)
        )
        for syllables, durations in result:
            print(f"Sílabas: {syllables}")
            print(f"Durações: {[str(d) for d in durations]}")

    except ImportError as e:
        print(f"Erro: {e}")

    # print("\n=== Exemplo original do make_lyrics_rule_and_music ===")
    # v1 = [
    #     ("we", 1, 1, "(", ".", "pp"),
    #     ("dream", 1, 5),
    #     ("to --", 1, 1),
    #     ("ge --", 1, 1),
    #     ("ther", 1, 2),
    #     ("", -1, -1),
    #     ("we", 1, -1),
    #     ('"wake up and"', 3, 1),
    #     ("keep", 1, 1),
    #     ("drea --", 1, 5),
    #     ("ming", 1, 1),
    # ]
    # verses = [v1]

    # lyrics, rule, music = make_lyrics_rule_and_music(verses)
    # # rule = abjad.mutate.eject_contents(rule[0])
    # # print(v1lyr)
    # # print(abjad.lilypond(v1rule))
    # # print(abjad.lilypond(v1music))
    # lyr = abjad.Context(
    #     lilypond_type="Lyrics",
    #     name="lyr",
    # )
    # align_str = r" \override LyricText.self-alignment-X = #LEFT  \override LyricText.X-offset = #-1 "
    # print(lyrics)
    # lit = abjad.LilyPondLiteral(
    #     r'\lyricsto "'
    #     + "v1rule"
    #     + r'" { \lyricmode {'
    #     + align_str
    #     + r" "
    #     + lyrics[0]
    #     + "}}"
    # )
    # abjad.attach(lit, lyr)

    # v1rule = abjad.Voice([rule], lilypond_type="NullVoice", name="v1rule")
    # v1music = abjad.Voice([music], name="v1music")
    # pitch.write_pitches(music, [24])
    # staff = abjad.Staff([v1rule, lyr, v1music], simultaneous=True)

    # lf = abjad.LilyPondFile(
    #     items=[
    #         r'\include "org_stylesheet.ily"',
    #         r"\paper { page-breaking = #ly:one-line-auto-height-breaking }",
    #         staff,
    #     ]
    # )

    # abjad.persist.as_pdf(lf, "texst.pdf")


if __name__ == "__main__":
    main()
