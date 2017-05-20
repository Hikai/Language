"""
IDAPython get argument function.

@hikai
"""
import sark


extern = list(sark.Segment(name="extern").functions)
system = filter(lambda x: x.name == 'system', extern)[0]
xrefs = filter(lambda x: x.iscode == 1, system.xrefs_to)
func_xrefs = []

for xref in xrefs:
    func_xrefs.append(sark.Function(xref.frm).startEA)
func_xrefs = set(func_xrefs)
for xref in func_xrefs:
    func = sark.Function(xref)
    lines = map(lambda x: x.disasm, func.lines)
    for index, line in enumerate(lines):
        if "jalr" in line and "websGetVar" in line:
            for i in range(index, 0, -1):
                if "$a1" in lines[i]:
                    print(func, lines[i])

                    break
