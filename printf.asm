; without C library.
; org 100h
; mov dx, msg
; mov ah, 9
; int 21h
; mov ah, 4Ch
; int 21h
; msg db 'Hello, world', 0Dh, 0Ah, '$'

; with C library.
global  _main
extern  _printf

section .text
_main:
    push    message
    call    _printf
    add     esp, 4
    ret
message:
    db  'Hello, World', 10, 0