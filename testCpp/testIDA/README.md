this is for using of IDA, reverse Engine

professor has got the full version of IDA, in /opt/ida-6.9
and run software with ./idaq64 in the background

# learning to IDA, the slide, Reverse Engineering with ida pro, with Chris Eagle
## Assembly Notes
"intel" syntax: MOV <dest>, <src>
objdump -d -M intel <file>
gdb -set disassembly-flavor intel
As opposed to "AT&T" syntax
MOV <src>, <dest>
default for objdump, gdb

through IDA to analysis string out of string.cpp, and generate other files like
string.id0, string.id1, string.id2, string.nam, string.til

## ida default names
sub_XXXX - function starting at address XXXX
loc_XXXX - Code at location XXXX is referenced from elsewhere, generally a branch target
byte_XXXX, word_XXXX, dword_XXXX - byte, word or dword data at location XXXX

easy navigation reduces the need for search
esc will take you back

## assembly constructs, PageNo.54
call convections
visual C++:
- cdecl: push parameters right to left, caller cleans up stack
- stdcall: push parameters right to left, called function cleans up stack, Windows API functions use this calling convertion
- fastcall: First two parameters(on the left) go in ECX and EDX, remaining parameters are pushed right to left
- thiscall: for C++ non-static member functions, this is placed in ECX

## parameter access
...

## local variables

## if statements, PageNo.72
```asm
    cmp eax, ebx    ; if
    jle endif       ; (eax > ebx) {
        ; if body
                    ; }
    endif:
```
