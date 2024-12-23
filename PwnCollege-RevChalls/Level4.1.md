# Level 4.1

## Challenge Goals

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

I opened the challenge and found that there was a program called `babyrev-level-4-1`.

Again like in the previous levels, I opened gdb and used info functions instruction to check out all the functions that are present and I again found `read and memcmp`.

Then I opened the assembly using the objdump instruction.

``` asm
    14a9:       e8 b2 fc ff ff          call   1160 <read@plt>      // Take user input

    14ae:       c7 45 e8 00 00 00 00    mov    DWORD PTR [rbp-0x18],0x0     // Set [rbp-0x18] to 0

    14b5:       eb 73                   jmp    152a <strerror@plt+0x37a>    // Jump to address 152a

    14b7:       c7 45 ec 00 00 00 00    mov    DWORD PTR [rbp-0x14],0x0     // Set [rbp-0x14] to 0

    14be:       eb 59                   jmp    1519 <strerror@plt+0x369>    // Jump to address 1519

    14c0:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]     // Move the value at [rbp-0x14] to eax

    14c3:       48 98                   cdqe    // Convert eax to rax

    14c5:       0f b6 54 05 f2          movzx  edx,BYTE PTR [rbp+rax*1-0xe]   // Gets first byte into edx

    14ca:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]     // Move the value at [rbp-0x14] to eax

    14cd:       83 c0 01                add    eax,0x1      // Add 1 to eax

    14d0:       48 98                   cdqe

    14d2:       0f b6 44 05 f2          movzx  eax,BYTE PTR [rbp+rax*1-0xe] // Get 2nd byte into eax

    14d7:       38 c2                   cmp    dl,al        // Compare 1st and 2nd bytes

    14d9:       76 3a                   jbe    1515 <strerror@plt+0x365>    // Unsigned comparision, if dl < al jump to 1515

    14db:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]    

    14de:       48 98                   cdqe

    14e0:       0f b6 44 05 f2          movzx  eax,BYTE PTR [rbp+rax*1-0xe]   //Moves first input byte into eax

    14e5:       88 45 e6                mov    BYTE PTR [rbp-0x1a],al       // Moves lowest byte of eax into [rbp-0x1a] i.e temp 1

    14e8:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]     

    14eb:       83 c0 01                add    eax,0x1  // Adds 1 to eax

    14ee:       48 98                   cdqe

    14f0:       0f b6 44 05 f2          movzx  eax,BYTE PTR [rbp+rax*1-0xe]  // Gets next input byte into eax

    14f5:       88 45 e7                mov    BYTE PTR [rbp-0x19],al     // Moves lowest byte of eax into [rbp-0x19] i.e temp 2 

    14f8:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]     // Moves [rbp-0x14]'s value into eax

    14fb:       48 98                   cdqe

**Swapping of the 2 bytes takes place here**
    14fd:       0f b6 55 e7             movzx  edx,BYTE PTR [rbp-0x19]

    1501:       88 54 05 f2             mov    BYTE PTR [rbp+rax*1-0xe],dl

    1505:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]

    1508:       83 c0 01                add    eax,0x1

    150b:       48 98                   cdqe

    150d:       0f b6 55 e6             movzx  edx,BYTE PTR [rbp-0x1a]

    1511:       88 54 05 f2             mov    BYTE PTR [rbp+rax*1-0xe],dl
** Swapping ends here**

    1515:       83 45 ec 01             add    DWORD PTR [rbp-0x14],0x1  // Add 1 to [rbp-0x14]

    1519:       b8 04 00 00 00          mov    eax,0x4

    151e:       2b 45 e8                sub    eax,DWORD PTR [rbp-0x18]

    1521:       39 45 ec                cmp    DWORD PTR [rbp-0x14],eax  

    1524:       7c 9a                   jl     14c0 <strerror@plt+0x310>

    1526:       83 45 e8 01             add    DWORD PTR [rbp-0x18],0x1

    152a:       83 7d e8 03             cmp    DWORD PTR [rbp-0x18],0x3     // Compare [rbp-0x18] with 3

    152e:       7e 87                   jle    14b7 <strerror@plt+0x307>    // If less than or equal, jump to address 14b7

    1530:       48 8d 3d c1 0d 00 00    lea    rdi,[rip+0xdc1]        # 22f8 <strerror@plt+0x1148>

    1537:       e8 e4 fb ff ff          call   1120 <puts@plt>

    153c:       48 8d 45 f2             lea    rax,[rbp-0xe]

    1540:       ba 05 00 00 00          mov    edx,0x5

    1545:       48 8d 35 c4 2a 00 00    lea    rsi,[rip+0x2ac4]        # 4010 <strerror@plt+0x2e60>

    154c:       48 89 c7                mov    rdi,rax

    154f:       e8 1c fc ff ff          call   1170 <memcmp@plt>
```

`Summary`

[rbp-0x14]: Keeps track of the current index within a pass over the input.
[rbp-0x18]: Keeps track of the current pass number over the input.

This basically a bubble sort program.


Expected output is at address [rip+0x2ac4] i.e `0x1545 + 0x2ac4 = 4009`

![alt text](./ReverseEngineering/Images/Level4.1(1).png)

The expected value is : `fmpru`

Now we can send our input as any combination of `fmpru` and it will sort it and match the value.

![alt text](./ReverseEngineering/Images/Level4.1(2).png)

## Flag

`pwn.college{cJcYhV9_ueKjO3kuTVnM4mKkS1f.0FO1IDLzITO0czW}`




