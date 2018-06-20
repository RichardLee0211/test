for security study, I would need a virtual mechine, and it would be serveral options in macOS
- vitualBox(across platform and free)
- vmware, money and across platform
- parallels, refuse
- QEMU, open source but mainly for Linux
- boot camp, free but it's most like a dual system, refuse

I need windows because all my evil software are of windows
try parallels first and download window 10 from parallel
I prefer VMware
got to have a windows running first



might try dock(the develop tools) next time

here: http://www.panduoduo.net/r/35647068
it's could be a good one for download vmware MAC and cracked

insteresting search way:
need VMware Fusion in mac,
search panduoduo and find one, need to download
search for hacking pan.baidu.com, get TamperMoney extension and script
search for downloader apps for mac, get aria2.
Aria2, This is what I wanted serverial years ago. Could be a cool software to replace Xunlei

it seems aria2 is very popular and pan.baidu.com is limited in US

download MVware Fusion 8 from here: https://my.vmware.com/group/vmware/details?downloadGroup=FUS-8510&productId=527&download=true&fileId=167b6f633dc17a55c95d92619e7726a9&secureParam=3a79e727d026057034d66dcd6ee60b25&uuId=7230ac03-4273-4072-aba2-63bf89077263&downloadType=
and get license key from here: https://blog.csdn.net/zhao_liwei/article/details/50685889
FY75A-06W1M-H85PZ-0XP7T-MZ8E8
ZY7TK-A3D4N-08EUZ-TQN5E-XG2TF
FG1MA-25Y1J-H857P-6MZZE-YZAZ6
and may could get VMware from here: http://www.orsoon.com/news/174624.html
bother about it later
and one post save me, here: http://planetvm.net/blog/?p=3240
system preference->securityandPrivate->allow the block message



this might be the first time I try to look at PE file and windows reverse engienerring
and this would begin with search, have fun
https://security.stackexchange.com/questions/37921/windows-pe-file-and-malwares
and MSDN documentary in PE format
here: https://msdn.microsoft.com/en-us/library/windows/desktop/ms680547(v=vs.85).aspx

Portable Executable(PE) and Common Object File Format(COFF)

since I have install MVware and would need system ISO file, here's usually hacking linux distro
https://resources.infosecinstitute.com/top-10-linux-distro-ethical-hacking-penetration-testing/#gref

install Kali with root abcd

# note of "Pratical Reverse Engineering.pdf"
book list:
- [ ] The C Programming Language, by Brian Kernighan and Dennis Ritchie (Prentice Hall, 1988)
- [ ] C: A Reference Manual, by Samuel Harbison (Prentice Hall, 2002)
- [ ] Expert C Programming: Deep C Secrets, by Peter van der Linden (Prentice Hall, 1994)
- [ ] Compilers: Principles, Techniques, and Tools, by Alfred Aho, Ravi Sethi, and Jeffrey Ullman, (Prentice Hall, 1994)
- [ ] Linkers and Loaders, by John Levine (Morgan Kaufmann, 1999),
- [ ] Advanced Compiler Design and Implementation, by Steven Muchnick (Morgan Kaufmann, 1997).
- [ ] Intel 64 and IA-32 Architectures Software Developer’s Manual, Volume 1: Basic Architecture by Intel, with special attention to Chapters 2–7.
- [ ]
- [ ]

## ch1 x86 and x64

### data movement
little endian
MOV [0x0], 0x113
00 00 01 13h
0x000 Type          0x13
0x001 Important     0x01
0x002 Number        0x00
0x004 DpcListEntry  0x00

SCAS, compare AL/AX/EAX with data starting at the memory address EDI
```x86
    ; strlen implement
    01: 30 C0            xor    al, al
    ; set AL to 0 (NUL byte).  You will frequently observe the XOR reg, reg
    ;  pattern in code.
    02: 89 FB            mov    ebx, edi
    ; save the original pointer to the string
    03: F2 AE            repne  scasb
    ; repeatedly scan forward one byte at a time as long as AL does not match the
    ; byte at EDI when this instruction ends, it means we reached the NUL byte in
    ; the string buffer
    04: 29 DF            sub    edi, ebx
    ; edi is now the NUL byte location. Subtract that from the original pointer
    ; to the length.
```

STOS, write the value AL/AX/EAX to EDI
```x86
    ; memset()
    01: 33 C0            xor    eax, eax
    ; set EAX to 0
    02: 6A 09            push   9
    ; push 9 on the stack
    03: 59               pop    ecx
    ; pop it back in ECX. Now ECX = 9.
     04: 8B FE            mov    edi, esi
    ; set the destination address
    05: F3 AB            rep stosd
    ; write 36 bytes of zero to the destination buffer (STOSD repeated 9 times)
    ; this is equivalent lent to memset(edi, 0, 36)
```

exercise:
01: 8B 7D 08    mov   edi, [ebp+8]       // argument 1, pointer
02: 8B D7       mov   edx, edi           // store the original pointer
03: 33 C0       xor   eax, eax           // set eax to 0x0(NULL)
04: 83 C9 FF    or    ecx, 0FFFF FFFFh   // set ecx to 0xFFFF FFFF
05: F2 AE       repne scasb              // compare AX with edi
06: 83 C1 02    add   ecx, 2
07: F7 D9       neg   ecx
08: 8A 45 0C    mov   al, [ebp+0Ch]      // argument 2
09: 8B FA       mov   edi, edx
10: F3 AA       rep   stosb              // store whatever al to original pointer
11: 8B C2       mov   eax, edx

may to understand assembly is to use them
