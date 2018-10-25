#!/usr/bin/env python

var = {"rbp": 0, "rsp": 0, "ebp": 0, "esp": 0, "eax": 0, "var_4": 0, "var_8": 0, "var_c": 0, "var_10": 0}


def get_ptr_offset(oper):
    idx_dash = oper.find('-')
    if idx_dash > -1:
        idx_end = oper.find(']')

        return (idx_dash + 2, idx_end)

    return -1


def mov(operands):
    for idx, oper in enumerate(operands):
        offset = get_ptr_offset(oper)
        if offset != -1:
            operands[idx] = operands[idx][offset[0]:offset[1]]

    if operands[1] in var:
        var[operands[0]] = var[operands[1]]
    else:
        if unicode(operands[1]).isnumeric():
            var[operands[0]] = operands[1]
        elif operands[1].find("0x") > -1:
            var[operands[0]] = int(operands[1], 16)
        else:
            var[operands[0]] = int(operands[1])


def add(operands):
    for idx, oper in enumerate(operands):
        offset = get_ptr_offset(oper)
        if offset != -1:
            operands[idx] = operands[idx][offset[0]:offset[1]]

    if operands[1] in var:
        var[operands[0]] += var[operands[1]]
    else:
        if unicode(operands[1]).isnumeric():
            var[operands[0]] += operands[1]
        elif operands[1].find("0x") > -1:
            var[operands[0]] += int(operands[1], 16)
        else:
            var[operands[0]] += int(operands[1])


def imul(operands):
    for idx, oper in enumerate(operands):
        offset = get_ptr_offset(oper)
        if offset != -1:
            operands[idx] = operands[idx][offset[0]:offset[1]]

    if len(operands) == 2:
        if operands[1] in var:
            var[operands[0]] *= var[operands[1]]
        else:
            if unicode(operands[1]).isnumeric():
                var[operands[0]] *= operands[1]
            elif operands[1].find("0x") > -1:
                var[operands[0]] *= int(operands[1], 16)
    elif len(operands) == 3:
        if operands[1] in var:
            if operands[2] in var:
                var[operands[0]] = var[operands[1]] * var[operands[2]]
            elif operands[2].find("0x") > -1:
                var[operands[0]] = var[operands[1]] * int(operands[2], 16)
            else:
                var[operands[0]] = var[operands[1]] * int(operands[2])


def _and(operands):
    for idx, oper in enumerate(operands):
        offset = get_ptr_offset(oper)
        if offset != -1:
            operands[idx] = operands[idx][offset[0]:offset[1]]

    if operands[1] in var:
        var[operands[0]] &= var[operands[1]]
    else:
        if unicode(operands[1]).isnumeric():
            var[operands[0]] &= operands[1]
        elif operands[1].find("0x") > -1:
            var[operands[0]] &= int(operands[1], 16)
        else:
            var[operands[0]] &= int(operands[1])


def _or(operands):
    for idx, oper in enumerate(operands):
        offset = get_ptr_offset(oper)
        if offset != -1:
            operands[idx] = operands[idx][offset[0]:offset[1]]

    if operands[1] in var:
        var[operands[0]] |= var[operands[1]]
    else:
        if unicode(operands[1]).isnumeric():
            var[operands[0]] |= operands[1]
        elif operands[1].find("0x") > -1:
            var[operands[0]] |= int(operands[1], 16)
        else:
            var[operands[0]] |= int(operands[1])


def xor(operands):
    for idx, oper in enumerate(operands):
        offset = get_ptr_offset(oper)
        if offset != -1:
            operands[idx] = operands[idx][offset[0]:offset[1]]

    if operands[1] in var:
        var[operands[0]] ^= var[operands[1]]
    else:
        if unicode(operands[1]).isnumeric():
            var[operands[0]] ^= operands[1]
        elif operands[1].find("0x") > -1:
            var[operands[0]] ^= int(operands[1], 16)
        else:
            var[operands[0]] ^= int(operands[1])


_asm = '''push rbp
mov rbp, rsp
mov dword ptr [rbp - 4], 0
mov dword ptr [rbp - 8], 0x496b
mov dword ptr [rbp - 0xc], 0x444c
mov dword ptr [rbp - 0x10], 0xb0a7
imul eax, dword ptr [rbp - 8], 0x1e47
add eax, dword ptr [rbp - 0xc]
xor eax, dword ptr [rbp - 0x10]
pop rbp
ret'''

# _asm = '''mov ebp, esp
# sub esp, 0x10
# mov dword ptr [ebp - 4], 0
# mov dword ptr [ebp - 8], 0x2047
# mov dword ptr [ebp - 0xc], 0xd8c4
# mov dword ptr [ebp - 0x10], 0x8a3a
# imul eax, dword ptr [ebp - 8], 0xdf6a
# or eax, dword ptr [ebp - 0xc]
# imul eax, dword ptr [ebp - 0x10]
# add esp, 0x10
# pop ebp
# ret'''

# _asm = '''mov rbp, rsp
# mov dword ptr [rbp - 4], 0
# mov dword ptr [rbp - 8], 0x8c41
# mov dword ptr [rbp - 0xc], 0x8e7f
# mov dword ptr [rbp - 0x10], 0x84c3
# mov eax, dword ptr [rbp - 8]
# add eax, 0x7323
# or eax, dword ptr [rbp - 0xc]
# imul eax, dword ptr [rbp - 0x10]
# pop rbp
# ret'''

for cmd in _asm.split('\n'):
    cmd_bak = cmd.split()
    cmd_bak.reverse()
    cmd_bak.pop()
    cmd_bak.reverse()
    operands = (' '.join(cmd_bak)).split(', ')
    cmd = cmd.split()[0]

    if cmd == "mov":
        mov(operands)
    elif cmd == "add":
        add(operands)
    elif cmd == "imul":
        imul(operands)
    elif cmd == "and":
        _and(operands)
    elif cmd == "or":
        _or(operands)
    elif cmd == "xor":
        xor(operands)
    else:
        print("not realization.")

print(var)
