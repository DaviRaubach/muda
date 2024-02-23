import abjad


def select_contiguous_containers_by_name(parent_container, containers_names: list[str]):
    materials = abjad.select.components(parent_container, abjad.Container)
    materials = [_ for _ in materials if not isinstance(
        _, abjad.Tuplet or abjad.Voice)]
    selected = []
    indices = []
    for i, c in enumerate(materials):
        # print(c.name, c, c.identifier)
        for name in containers_names:
            if c.name and c.name.startswith(name):
                selected.append(c)
                indices.append(i)

    # s_and_i = zip(selected, indices)
    # print("s", indices)
    new_indices = []
    for (i, a), b in zip(enumerate(indices), indices[1:]):
        # print(selected[i+1].name, selected[i].name)
        if b == (a + 1):
            # print(a, b)
            if selected[i+1].name != selected[i].name:
                new_indices.append(a)

    new_materials = []
    for i in new_indices:
        j = i + 1
        new_materials.append([materials[i], materials[j]])

    return new_materials


select_contiguous_materials = select_contiguous_containers_by_name


def select_not_contiguous_containers_by_name(parent_container, select_name: str, neiborgh_name: str):
    materials = abjad.select.components(parent_container, abjad.Container)
    selected = []
    indices = []
    for i, c in enumerate(materials):
        for name in [select_name, neiborgh_name]:
            if c.name and c.name.startswith(name):
                # selected.append(c)
                indices.append(i)

    new_indices = []
    for (i, a), b in zip(enumerate(indices), indices[1:]):
        if b != (a + 1):
            new_indices.append(a)

    # indices = [_ for _ in range(len(materials)) if _ not in not_indices]
    new_materials = []
    for i in new_indices:
        # j = i + 1
        new_materials.append(materials[i])

    return new_materials


select_not_contiguous_materials = select_not_contiguous_containers_by_name


def call_function_on_leaf_in_selection(selection, n=0, function=lambda _: print(_), all_leaves=False):
    if isinstance(selection, list):
        if isinstance(selection, abjad.LogicalTie):
            function(abjad.select.leaf(selection, n))
        else:
            if selection:
                if isinstance(selection[0], abjad.Leaf):
                    if all_leaves is True:
                        for leaf in selection:
                            function(leaf)
                    else:
                        function(selection[n])
            
