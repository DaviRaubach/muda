import abjad
import muda
staff = abjad.Staff("c4 c4 c4")
sel = abjad.Selection(staff)

sel = lambda _: abjad.Selection(_).leaves.get



# def test(sel, select):
#     staff = abjad.Staff("c4 c4 c4")
#     sel = muda.Selection(staff)
    

# sel = muda.Selection().leaves()
# s = sel(staff)
# print(s)


a = [_.leaves() for _ in sel]
print(a)
