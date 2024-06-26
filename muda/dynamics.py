import abjad
from typing import Optional


def inspect_selection(selection):
    """

    :param selection:

    """
    if isinstance(selection, abjad.Leaf):
        selection = [[selection]]
    if isinstance(selection, abjad.LogicalTie):
        selection = [selection]


def make_dynamics(dynamics: list, leak=False, command: Optional[str] = None):
    """

    :param dynamics: list:
    :param leak:  (Default value = False)
    :param command: Optional[str]:  (Default value = None)

    """
    dynamics = [abjad.Dynamic(_, leak=leak, command=command) for _ in dynamics]
    return dynamics


def dynamics(
    dynamics: str | list,
    selection: list,
    leak=False,
    command: Optional[str] = None,
    hide: bool = False,
):
    """

    :param dynamics: str | list:
    :param selection: list:
    :param leak:  (Default value = False)
    :param command: Optional[str]:  (Default value = None)

    """

    if abjad.Dynamic.is_dynamic_name(dynamics) or isinstance(dynamics, list):
        if isinstance(selection, abjad.Leaf):
            abjad.attach(
                abjad.Dynamic(dynamics, leak=leak, command=command, hide=hide),
                selection,
            )
        elif isinstance(selection, abjad.LogicalTie):
            abjad.attach(
                abjad.Dynamic(dynamics, leak=leak, command=command, hide=hide),
                selection[0],
            )

        elif not isinstance(selection, abjad.LogicalTie):
            if isinstance(dynamics, list):
                for target, dyn in zip(selection, dynamics):
                    abjad.attach(
                        abjad.Dynamic(dyn, leak=leak, command=command, hide=hide),
                        target,
                    )
            else:
                for _ in selection:
                    abjad.attach(
                        abjad.Dynamic(dynamics, leak=leak, command=command, hide=hide),
                        _,
                    )

    elif isinstance(selection, list):
        try:
            selection
            if isinstance(selection[0], list):
                for sel in selection:
                    abjad.hairpin(dynamics, sel)
            else:
                # print("else")
                abjad.hairpin(dynamics, selection)
        except IndexError:
            Warning(f"selection: {selection}, dynamic: {dynamics}")


def dynamics_after(
    material: abjad.Container,
    points_list: list[int],
    literal_dynamics: list[str],
    denominator=16,
    new_container=True,
    parent_component=None,
    flared_hairpin=False,
):
    """

    :param material: abjad.Container:
    :param points_list: list[int]:
    :param literal_dynamics: list[str]:
    :param denominator:  (Default value = 16)
    :param new_container:  (Default value = True)

    """

    duration = abjad.get.duration(material)
    total_points = int(duration / abjad.Duration(1, denominator))
    _max = max(points_list)
    proportions = [_ / _max for _ in points_list]
    points = [int(_ * total_points) for _ in proportions if _ != 1]
    points.append(total_points - 1)
    points = [(_, denominator) for _ in points]
    points = [rf"1 * {a}/{b}" for a, b in points]

    literals = []
    for i, point in enumerate(points):
        if i != 0 or i != len(literal_dynamics) - 1:
            if literal_dynamics[i] is not None:
                for dyn in literal_dynamics[i]:
                    if dyn is not None:
                        literals.append(rf"\after {point} {dyn}")

    if new_container:
        literals.append(r"{")

    if flared_hairpin:
        literals.append(r"\override Hairpin.stencil = #flared-hairpin")

    literals = abjad.LilyPondLiteral(literals, site="absolute_before")

    # if parent_component is not None:
    parentage = abjad.get.parentage(material[0])
    if parent_component is not None and isinstance(parentage.parent, parent_component):
        # pass
        abjad.attach(literals, parentage.parent)
        # print(parentage.parent)
    else:
        # pass
        abjad.attach(literals, material[0])

    if new_container:
        parentage = abjad.get.parentage(material[-1])
        if parent_component is not None and isinstance(
            parentage.parent, parent_component
        ):
            abjad.attach(abjad.LilyPondLiteral(r"}", site="after"), parentage.parent)
        else:
            abjad.attach(abjad.LilyPondLiteral(r"}", site="after"), material[-1])

    if flared_hairpin:
        abjad.attach(
            abjad.LilyPondLiteral(r"\revert Hairpin.stencil", site="after"),
            material[-1],
        )


# class Velocity:
#     def __init__(self, velocity: float):
#         self.velocity = velocity
#         self.__call__()

#     def __call__(self):
#         return abjad.LilyPondLiteral(rf"\vel {self.velocity} ")


def make_velocity(velocity: float):
    return abjad.LilyPondLiteral(rf"\vel {velocity} ", site="after")


def make_arc_velocities(argument, dynamic_range=[0.1, 0.6]):
    # runs = abjad.select.runs(argument)
    # for run in runs:
    lts = abjad.select.logical_ties(argument, pitched=True)
    metade = int(len(lts) / 2)
    if metade > 0:
        multiplo = (dynamic_range[1] - dynamic_range[0]) / metade
        int_list = [_ for _ in range(metade)]
        if int_list:
            int_list[0] = 1

        floats = [dynamic_range[0] + (_ * multiplo) for _ in int_list]
        floats = floats + floats[::-1]
        if len(lts) % 2 != 0:
            floats.append(floats[-1])

        for lt, vel in zip(lts, floats):
            abjad.attach(make_velocity(vel), lt[0])
