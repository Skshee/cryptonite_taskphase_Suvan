# Level 7.1

## Challenge Objectives

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

I opened the challenge and found a program named `babygame-level-7-1` and I went through it's assembly code using objdump.

``` asm

    14bb:       e8 a0 fc ff ff          call   1160 <read@plt>
    14c0:       c7 45 bc 00 00 00 00    mov    DWORD PTR [rbp-0x44],0x0
    14c7:       eb 73                   jmp    153c <strerror@plt+0x38c>
    14c9:       c7 45 c0 00 00 00 00    mov    DWORD PTR [rbp-0x40],0x0
    14d0:       eb 59                   jmp    152b <strerror@plt+0x37b>
    14d2:       8b 45 c0                mov    eax,DWORD PTR [rbp-0x40]
    14d5:       48 98                   cdqe
    14d7:       0f b6 54 05 d0          movzx  edx,BYTE PTR [rbp+rax*1-0x30]
    14dc:       8b 45 c0                mov    eax,DWORD PTR [rbp-0x40]
    14df:       83 c0 01                add    eax,0x1
    14e2:       48 98                   cdqe
    14e4:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    14e9:       38 c2                   cmp    dl,al
    14eb:       76 3a                   jbe    1527 <strerror@plt+0x377>
    14ed:       8b 45 c0                mov    eax,DWORD PTR [rbp-0x40]
    14f0:       48 98                   cdqe
    14f2:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    14f7:       88 45 ba                mov    BYTE PTR [rbp-0x46],al
    14fa:       8b 45 c0                mov    eax,DWORD PTR [rbp-0x40]
    14fd:       83 c0 01                add    eax,0x1
    1500:       48 98                   cdqe
    1502:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    1507:       88 45 bb                mov    BYTE PTR [rbp-0x45],al
    150a:       8b 45 c0                mov    eax,DWORD PTR [rbp-0x40]
    150d:       48 98                   cdqe
    150f:       0f b6 55 bb             movzx  edx,BYTE PTR [rbp-0x45]
    1513:       88 54 05 d0             mov    BYTE PTR [rbp+rax*1-0x30],dl
    1517:       8b 45 c0                mov    eax,DWORD PTR [rbp-0x40]
    151a:       83 c0 01                add    eax,0x1
    151d:       48 98                   cdqe
    151f:       0f b6 55 ba             movzx  edx,BYTE PTR [rbp-0x46]
    1523:       88 54 05 d0             mov    BYTE PTR [rbp+rax*1-0x30],dl
    1527:       83 45 c0 01             add    DWORD PTR [rbp-0x40],0x1
    152b:       b8 1a 00 00 00          mov    eax,0x1a
    1530:       2b 45 bc                sub    eax,DWORD PTR [rbp-0x44]
    1533:       39 45 c0                cmp    DWORD PTR [rbp-0x40],eax
    1536:       7c 9a                   jl     14d2 <strerror@plt+0x322>
    1538:       83 45 bc 01             add    DWORD PTR [rbp-0x44],0x1
    153c:       83 7d bc 19             cmp    DWORD PTR [rbp-0x44],0x19
    1540:       7e 87                   jle    14c9 <strerror@plt+0x319>
    1542:       c7 45 c4 00 00 00 00    mov    DWORD PTR [rbp-0x3c],0x0
    1549:       eb 42                   jmp    158d <strerror@plt+0x3dd>
    154b:       8b 45 c4                mov    eax,DWORD PTR [rbp-0x3c]
    154e:       48 98                   cdqe
    1550:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    1555:       88 45 b8                mov    BYTE PTR [rbp-0x48],al
    1558:       b8 1a 00 00 00          mov    eax,0x1a
    155d:       2b 45 c4                sub    eax,DWORD PTR [rbp-0x3c]
    1560:       48 98                   cdqe
    1562:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    1567:       88 45 b9                mov    BYTE PTR [rbp-0x47],al
    156a:       8b 45 c4                mov    eax,DWORD PTR [rbp-0x3c]
    156d:       48 98                   cdqe
    156f:       0f b6 55 b9             movzx  edx,BYTE PTR [rbp-0x47]
    1573:       88 54 05 d0             mov    BYTE PTR [rbp+rax*1-0x30],dl
    1577:       b8 1a 00 00 00          mov    eax,0x1a
    157c:       2b 45 c4                sub    eax,DWORD PTR [rbp-0x3c]
    157f:       48 98                   cdqe
    1581:       0f b6 55 b8             movzx  edx,BYTE PTR [rbp-0x48]
    1585:       88 54 05 d0             mov    BYTE PTR [rbp+rax*1-0x30],dl
    1589:       83 45 c4 01             add    DWORD PTR [rbp-0x3c],0x1
    158d:       83 7d c4 0c             cmp    DWORD PTR [rbp-0x3c],0xc
    1591:       7e b8                   jle    154b <strerror@plt+0x39b>
    1593:       c7 45 c8 00 00 00 00    mov    DWORD PTR [rbp-0x38],0x0
    159a:       eb 50                   jmp    15ec <strerror@plt+0x43c>
    159c:       8b 45 c8                mov    eax,DWORD PTR [rbp-0x38]
    159f:       99                      cdq
    15a0:       c1 ea 1f                shr    edx,0x1f
    15a3:       01 d0                   add    eax,edx
    15a5:       83 e0 01                and    eax,0x1
    15a8:       29 d0                   sub    eax,edx
    15aa:       85 c0                   test   eax,eax
    15ac:       74 07                   je     15b5 <strerror@plt+0x405>
    15ae:       83 f8 01                cmp    eax,0x1
    15b1:       74 1c                   je     15cf <strerror@plt+0x41f>
    15b3:       eb 33                   jmp    15e8 <strerror@plt+0x438>
    15b5:       8b 45 c8                mov    eax,DWORD PTR [rbp-0x38]
    15b8:       48 98                   cdqe
    15ba:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    15bf:       83 f0 16                xor    eax,0x16
    15c2:       89 c2                   mov    edx,eax
    15c4:       8b 45 c8                mov    eax,DWORD PTR [rbp-0x38]
    15c7:       48 98                   cdqe
    15c9:       88 54 05 d0             mov    BYTE PTR [rbp+rax*1-0x30],dl
    15cd:       eb 19                   jmp    15e8 <strerror@plt+0x438>
    15cf:       8b 45 c8                mov    eax,DWORD PTR [rbp-0x38]
    15d2:       48 98                   cdqe
    15d4:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    15d9:       83 f0 bf                xor    eax,0xffffffbf
    15dc:       89 c2                   mov    edx,eax
    15de:       8b 45 c8                mov    eax,DWORD PTR [rbp-0x38]
    15e1:       48 98                   cdqe
    15e3:       88 54 05 d0             mov    BYTE PTR [rbp+rax*1-0x30],dl
    15e7:       90                      nop
    15e8:       83 45 c8 01             add    DWORD PTR [rbp-0x38],0x1
    15ec:       83 7d c8 1a             cmp    DWORD PTR [rbp-0x38],0x1a
    15f0:       7e aa                   jle    159c <strerror@plt+0x3ec>
    15f2:       0f b6 45 d7             movzx  eax,BYTE PTR [rbp-0x29]
    15f6:       88 45 b6                mov    BYTE PTR [rbp-0x4a],al
    15f9:       0f b6 45 e7             movzx  eax,BYTE PTR [rbp-0x19]
    15fd:       88 45 b7                mov    BYTE PTR [rbp-0x49],al
    1600:       0f b6 45 b7             movzx  eax,BYTE PTR [rbp-0x49]
    1604:       88 45 d7                mov    BYTE PTR [rbp-0x29],al
    1607:       0f b6 45 b6             movzx  eax,BYTE PTR [rbp-0x4a]
    160b:       88 45 e7                mov    BYTE PTR [rbp-0x19],al
    160e:       c7 45 cc 00 00 00 00    mov    DWORD PTR [rbp-0x34],0x0
    1615:       eb 1d                   jmp    1634 <strerror@plt+0x484>
    1617:       8b 45 cc                mov    eax,DWORD PTR [rbp-0x34]
    161a:       48 98                   cdqe
    161c:       0f b6 44 05 d0          movzx  eax,BYTE PTR [rbp+rax*1-0x30]
    1621:       83 f0 fa                xor    eax,0xfffffffa
    1624:       89 c2                   mov    edx,eax
    1626:       8b 45 cc                mov    eax,DWORD PTR [rbp-0x34]
    1629:       48 98                   cdqe
    162b:       88 54 05 d0             mov    BYTE PTR [rbp+rax*1-0x30],dl
    162f:       90                      nop
    1630:       83 45 cc 01             add    DWORD PTR [rbp-0x34],0x1
    1634:       83 7d cc 1a             cmp    DWORD PTR [rbp-0x34],0x1a
    1638:       7e dd                   jle    1617 <strerror@plt+0x467>
    163a:       48 8d 3d b7 0c 00 00    lea    rdi,[rip+0xcb7]        # 22f8 <strerror@plt+0x1148>
    1641:       e8 da fa ff ff          call   1120 <puts@plt>
    1646:       48 8d 45 d0             lea    rax,[rbp-0x30]
    164a:       ba 1b 00 00 00          mov    edx,0x1b
    164f:       48 8d 35 ba 29 00 00    lea    rsi,[rip+0x29ba]        # 4010 <strerror@plt+0x2e60>
    1656:       48 89 c7                mov    rdi,rax
    1659:       e8 12 fb ff ff          call   1170 <memcmp@plt>
``` 

`Summary`

1. **Bubble Sort**: 0x14c0 - 0x1540
- [rbp-0x44] inner loop
- [rbp-0x0x40] outer loop (passes)

2. **Reversing**: 0x154b - 0x1591

3. **XORing**
- Even indices XORed with 0x16
- Odd indices XORed with 0xBF

4. **Swapping**
- Swaps bytes at offsets [rbp-0x29] (7) {Since 0x30 - 0x29 = 7} and [rbp-0x19] (17) {Since 0x30 - 0x19 = 17}

5. **All bytes XORed with 0xFA**

So, this time the length of the expected output is 27 bytes, so I used the following command to extract the expected output : `objdump -s --start-address=0x4010 --stop-address=0x4037 ./babyrev-level-7-1`

![alt text](./ReverseEngineering/Images/Level7.1(1).png)

The output hex values are : 963f963f 963f9522 953d9a33 99369f36 9d35832b 862c843c 89278d00

Now with some help from Chatgpt, I wrote a code to reverse engineer the operations.

[Level7.1](./ReverseEngineering/Codes/Level7.1.py)

Key : `beyhijnogqsssuvvxypyzzzzzzaE`

![alt text](./ReverseEngineering/Images/Level7.1(2).png)

## Flag

`pwn.college{AeQOKFFYzu2ujBlW6Cm2o4FSOsL.0FN2IDLzITO0czW}`



