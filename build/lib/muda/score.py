import abjad
import muda.functions as functions
       
def instrument(abjad_instrument, lilypond_name, nstaffs, nvoices, piano=None):
    site = "muda.score.instrument()"
    tag = abjad.Tag(site)
    staffs = []
    voices = []
        
    print(str(tag)+" -> "+lilypond_name)
    for i in range(nstaffs):
        if nstaffs == 1:
            staffs.append(abjad.Staff(name=lilypond_name+"_Staff",tag=tag))
            print("    creating "+lilypond_name+"_Staff_"+str(i+1))
        else:
            staffs.append(abjad.Staff(name=lilypond_name+"_Staff_"+str(i+1),tag=tag))
            print("    creating "+lilypond_name+"_Staff_"+str(i+1))

    for i in range(sum(nvoices)):
        if nvoices == 1:
            voices.append(abjad.Voice(name=lilypond_name+"_Voice", tag=tag))
            print("        creating "+lilypond_name+"_Voice_"+str(i+1))
        else:
            voices.append(abjad.Voice(name=lilypond_name+"_Voice_"+str(i+1), tag=tag))
            print("        creating "+lilypond_name+"_Voice_"+str(i+1))            
        
    for i, number_of_voices_in_each_staff in enumerate(nvoices):
        for n in range(number_of_voices_in_each_staff):
            if i == 0:
                staffs[i].append(voices[n])
                print("            attaching "+voices[n].name+" to "+staffs[i].name)
            if i >= 1:
                staffs[i].append(voices[n+sum(nvoices[:i])])
                print("            attaching "+voices[n+sum(nvoices[:i])].name+" to "+staffs[i].name)
    
    if nstaffs == 1:
        abjad.annotate(staffs[0], "default_instrument", abjad_instrument)
        ready_staff = staffs[0]
    
    else:
        if piano is True:
            staffgroup = abjad.StaffGroup(
                lilypond_type="PianoStaff",
                name="Piano_StaffGroup",
                tag=tag
                )
            for staff in staffs:
                staffgroup.append(staff)
        
        else:
            staffgroup = abjad.StaffGroup(
                name=lilypond_name,
                tag=tag
                )
            for staff in staffs:
                staffgroup.append(staff)
                
        abjad.annotate(staffgroup, "default_instrument", abjad_instrument)

        ready_staff = staffgroup
         
    return ready_staff
    
def create_score():
    site = "muda.score.create_score()"
    tag = abjad.Tag(site)
    score = abjad.Score(name="Score", tag=tag)  
    score.append(abjad.Staff(lilypond_type="TimeSignatureContext", name="Global_Context"))
    print(str(tag)) 
    return score
    
def add_instrument(instrument, score):
    site = "muda.score.add_instruments()"
    tag = abjad.Tag(site)
    print(str(tag))
    for inst in instrument:
        print("    "+str(inst.name)) 
    if isinstance(instrument, list):
        for inst in instrument:
            score.append(inst)
    else:
        score.append(instrument)

def make_skips(time_signatures, score):
    site = "muda.score.make_skips()"
    tag = abjad.Tag(site)
    print(str(tag))
    
    time_signatures_abjad = [
        abjad.TimeSignature(_) for _ in time_signatures
        ]
        
    for time_sig in time_signatures_abjad:
        skip = abjad.Skip(1, multiplier=(time_sig))
        score["Global_Context"].append(skip)
    
# select skips to attach TIME SIGNATURES

    for i, element in enumerate(time_signatures):
        previous_element = time_signatures[i-1] if i > 0 else None
        current_element = element

        if current_element != previous_element:
            a = time_signatures.index(current_element)
           
            abjad.attach(
                time_signatures_abjad[a],
                score["Global_Context"][a],
                tag=tag
                )
                
def write_material(voice_name, material):
    score[voice_name].extend(material)
    
    
def create_lilypond_file(score, includes):
    lilypond_file = abjad.LilyPondFile.new(
        score,
        includes=includes,
        )
    midi_block = abjad.Block(name="midi")
    layout_block = abjad.Block(name="layout")
    lilypond_file["score"].items.append(layout_block)
    lilypond_file["score"].items.append(midi_block)
    return lilypond_file


        