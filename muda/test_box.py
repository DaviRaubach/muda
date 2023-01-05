import muda
import abjad


def write(container: abjad.Container, ly_str: str):
    container.extend(ly_str)


def test_box():
    # box file
    def my_fn(container):
        write(container, r"c'4")

    box = muda.Box()
    box.append_function([my_fn])

    # segment file
    mat = muda.Material("test")
    mat.append_box(box)
    material_list = [mat]
    segment = muda.Segment(material_list)
    segment()
    print(mat.container)
    # print(box)
    # print(box.functions)


test_box()
