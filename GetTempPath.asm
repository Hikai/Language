; push ebp
; mov ebp, esp
; sub esp, 400
; ; enter 0, N
; mov eax, [esp-400]
; push eax
; mov eax, [esp-200]
; push eax
; call GetTempPath
; mov eax, [esp-400]
; push eax
; push str_format
; call printf
; push 0
; call ExiProcess
; pop ebx
; pop eax
; leave
; ret
; ; format label
; str_format:
;     db '%s\n', 0Dh, 0Ah, 6
; str_format_end:

global _main
extern _printf
extern _GetTempPathA@8

section .data
str_format:
    db '%s\n', 10, 0

section .text
_main:
    sub esp, 400h
    mov eax, [esp-400]
    push eax
    mov [esp-200], 200h
    mov eax, [esp-200]
    push eax
    call _GetTempPathA@8
    ; [esp-400] = GetTempPathA return value.
    mov eax, [esp-400]
    push eax
    mov eax, str_format
    push eax
    call _printf
    ret
