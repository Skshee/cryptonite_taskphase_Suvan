# Level 6.1 

## Challenge Objectives

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

I opened the challenge and found a program named `babygame-level-6-1` and I went through it's assembly code using objdump.

I found the read and memcmp functions and went through the code.

``` asm
    14b0:       e8 ab fc ff ff          call   1160 <read@plt>
    14b5:       c7 45 d4 00 00 00 00    mov    DWORD PTR [rbp-0x2c],0x0
    14bc:       eb 1d                   jmp    14db <strerror@plt+0x32b>
    14be:       8b 45 d4                mov    eax,DWORD PTR [rbp-0x2c]
    14c1:       48 98                   cdqe
    14c3:       0f b6 44 05 e0          movzx  eax,BYTE PTR [rbp+rax*1-0x20]
    14c8:       83 f0 61                xor    eax,0x61
    14cb:       89 c2                   mov    edx,eax
    14cd:       8b 45 d4                mov    eax,DWORD PTR [rbp-0x2c]
    14d0:       48 98                   cdqe
    14d2:       88 54 05 e0             mov    BYTE PTR [rbp+rax*1-0x20],dl
    14d6:       90                      nop
    14d7:       83 45 d4 01             add    DWORD PTR [rbp-0x2c],0x1
    14db:       83 7d d4 0f             cmp    DWORD PTR [rbp-0x2c],0xf
    14df:       7e dd                   jle    14be <strerror@plt+0x30e>
    14e1:       c7 45 d8 00 00 00 00    mov    DWORD PTR [rbp-0x28],0x0
    14e8:       eb 42                   jmp    152c <strerror@plt+0x37c>
    14ea:       8b 45 d8                mov    eax,DWORD PTR [rbp-0x28]
    14ed:       48 98                   cdqe
    14ef:       0f b6 44 05 e0          movzx  eax,BYTE PTR [rbp+rax*1-0x20]
    14f4:       88 45 d2                mov    BYTE PTR [rbp-0x2e],al
    14f7:       b8 0f 00 00 00          mov    eax,0xf
    14fc:       2b 45 d8                sub    eax,DWORD PTR [rbp-0x28]
    14ff:       48 98                   cdqe
    1501:       0f b6 44 05 e0          movzx  eax,BYTE PTR [rbp+rax*1-0x20]
    1506:       88 45 d3                mov    BYTE PTR [rbp-0x2d],al
    1509:       8b 45 d8                mov    eax,DWORD PTR [rbp-0x28]
    150c:       48 98                   cdqe
    150e:       0f b6 55 d3             movzx  edx,BYTE PTR [rbp-0x2d]
    1512:       88 54 05 e0             mov    BYTE PTR [rbp+rax*1-0x20],dl
    1516:       b8 0f 00 00 00          mov    eax,0xf
    151b:       2b 45 d8                sub    eax,DWORD PTR [rbp-0x28]
    151e:       48 98                   cdqe
    1520:       0f b6 55 d2             movzx  edx,BYTE PTR [rbp-0x2e]
    1524:       88 54 05 e0             mov    BYTE PTR [rbp+rax*1-0x20],dl
    1528:       83 45 d8 01             add    DWORD PTR [rbp-0x28],0x1
    152c:       83 7d d8 07             cmp    DWORD PTR [rbp-0x28],0x7
    1530:       7e b8                   jle    14ea <strerror@plt+0x33a>
    1532:       c7 45 dc 00 00 00 00    mov    DWORD PTR [rbp-0x24],0x0
    1539:       eb 1d                   jmp    1558 <strerror@plt+0x3a8>
    153b:       8b 45 dc                mov    eax,DWORD PTR [rbp-0x24]
    153e:       48 98                   cdqe
    1540:       0f b6 44 05 e0          movzx  eax,BYTE PTR [rbp+rax*1-0x20]
    1545:       83 f0 d0                xor    eax,0xffffffd0
    1548:       89 c2                   mov    edx,eax
    154a:       8b 45 dc                mov    eax,DWORD PTR [rbp-0x24]
    154d:       48 98                   cdqe
    154f:       88 54 05 e0             mov    BYTE PTR [rbp+rax*1-0x20],dl
    1553:       90                      nop
    1554:       83 45 dc 01             add    DWORD PTR [rbp-0x24],0x1
    1558:       83 7d dc 0f             cmp    DWORD PTR [rbp-0x24],0xf
    155c:       7e dd                   jle    153b <strerror@plt+0x38b>
    155e:       48 8d 3d 93 0d 00 00    lea    rdi,[rip+0xd93]        # 22f8 <strerror@plt+0x1148>
    1565:       e8 b6 fb ff ff          call   1120 <puts@plt>
    156a:       48 8d 45 e0             lea    rax,[rbp-0x20]
    156e:       ba 10 00 00 00          mov    edx,0x10
    1573:       48 8d 35 96 2a 00 00    lea    rsi,[rip+0x2a96]        # 4010 <strerror@plt+0x2e60>
    157a:       48 89 c7                mov    rdi,rax
    157d:       e8 ee fb ff ff          call   1170 <memcmp@plt>
```

`Summary`

This code basically does three main operations

1. 14b5-14df: First loop
- Initializes counter at [rbp-0x2c] to 0
- Loops 16 times (0 to 0xf)
- For each byte in buffer:
  * Loads byte from [rbp+rax*1-0x20]
  * XORs it with 0x61
  * Stores result back in same location

2. 14e1-1530: Second loop
- Counter [rbp-0x28] goes from 0 to 7
- For each iteration:
  * Saves byte from start in temporary var [rbp-0x2e]
  * Saves byte from end in temporary var [rbp-0x2d]
  * Swaps the bytes

3. 1532-155c: Third loop
- Similar structure to first loop
- Loops through all 16 bytes
- XORs each byte with 0xd0

So basically, our input is `16 characters long` and it's getting `XORed with 0x61, reversed and XORed with 0xd0`.

I found the final value using the following instruction : `objdump -s --start-address=0x4009 --stop-address=0x4025 ./babyrev-level-6-1`

![alt text](./ReverseEngineering/Images/Level6.1(1).png)

I got the hexadecimal values of the final output from this.

I wrote the following Python script to reverse engineer the input : [Babyrev6.1](./ReverseEngineering/Codes/Level6.1.py)

Therefore, input : `skblbhzzoqezghhk`

![alt text](./ReverseEngineering/Images/Level6.1(2).png)

## Flag

`pwn.college{QcHKWq6A2pKIEO5tuFsjO_9n4uu.0lM2IDLzITO0czW}`

