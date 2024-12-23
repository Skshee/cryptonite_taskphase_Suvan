# Level 5.1

## Challenge Objectives


## Approach

I opened the challenge and found a program called `babyrev-level-5-1` and opened it's assembly using objdump.

I found the `read and memcmp` functions.

```asm 

    14a9:       e8 b2 fc ff ff          call   1160 <read@plt>

    14ae:       c7 45 ec 00 00 00 00    mov    DWORD PTR [rbp-0x14],0x0      ; Set the value 0 at [rbp-0x14]

    14b5:       eb 1d                   jmp    14d4 <strerror@plt+0x324>

    14b7:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]

    14ba:       48 98                   cdqe

    14bc:       0f b6 44 05 f2          movzx  eax,BYTE PTR [rbp+rax*1-0xe]

    14c1:       83 f0 1c                xor    eax,0x1c

    14c4:       89 c2                   mov    edx,eax

    14c6:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]

    14c9:       48 98                   cdqe

    14cb:       88 54 05 f2             mov    BYTE PTR [rbp+rax*1-0xe],dl

    14cf:       90                      nop

    14d0:       83 45 ec 01             add    DWORD PTR [rbp-0x14],0x1

    14d4:       83 7d ec 04             cmp    DWORD PTR [rbp-0x14],0x4

    14d8:       7e dd                   jle    14b7 <strerror@plt+0x307>

    14da:       48 8d 3d 17 0e 00 00    lea    rdi,[rip+0xe17]        # 22f8 <strerror@plt+0x1148>

    14e1:       e8 3a fc ff ff          call   1120 <puts@plt>

    14e6:       48 8d 45 f2             lea    rax,[rbp-0xe]

    14ea:       ba 05 00 00 00          mov    edx,0x5

    14ef:       48 8d 35 1a 2b 00 00    lea    rsi,[rip+0x2b1a]        # 4010 <strerror@plt+0x2e60>

    14f6:       48 89 c7                mov    rdi,rax

    14f9:       e8 72 fc ff ff          call   1170 <memcmp@plt>
```
