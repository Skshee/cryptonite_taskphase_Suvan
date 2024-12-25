# Level 3.1

## Challenge Goals

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

I opened the challenge and found a program called `babyrev-level-3-1`.

The program asked for a input from the user and modified it and compared it with the license key.

So just like the previous levels, I needed to figure out what is the expected value and what modifications are being made to the input.

Like the previous levels, I opened gdb and found the functions in the program using the info functions instruction.

Even here I found `read and memcmp` PLTs so I understood that I had to find these two functions and I had to read between the lines to understand what's going on.


I opened the assembly using objdump. I am going to break down the code one by one

``` asm
    14a9:       e8 b2 fc ff ff          call   1160 <read@plt>      ; Taking in input from user

    14ae:       c7 45 ec 00 00 00 00    mov    DWORD PTR [rbp-0x14],0x0     ; Storing the value 0 at [rbp-0x14]

    14b5:       eb 42                   jmp    14f9 <strerror@plt+0x349>    ; Jumping to line 14f9

    14b7:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]     ; Moving the value at [rbp-0x14] to eax

    14ba:       48 98                   cdqe        ; Converts a signed doubleword (32-bit) in eax to a signed quadword (64-bit) in rax

    14bc:       0f b6 44 05 f2          movzx  eax,BYTE PTR [rbp+rax*1-0xe]     ; Gets first byte

    14c1:       88 45 ea                mov    BYTE PTR [rbp-0x16],al          ; al is the lowest byte of eax. [rbp-0x16] is like temp 1

    14c4:       b8 04 00 00 00          mov    eax,0x4      ; Moving the value 4 into eax

    14c9:       2b 45 ec                sub    eax,DWORD PTR [rbp-0x14]       ; 4-[rbp-0x14] and stores result back in eax

    14cc:       48 98                   cdqe    

    14ce:       0f b6 44 05 f2          movzx  eax,BYTE PTR [rbp+rax*1-0xe]     ; Gets 2nd byte

    14d3:       88 45 eb                mov    BYTE PTR [rbp-0x15],al       ; Temp 2

    14d6:       8b 45 ec                mov    eax,DWORD PTR [rbp-0x14]     

    14d9:       48 98                   cdqe

    14db:       0f b6 55 eb             movzx  edx,BYTE PTR [rbp-0x15]     ; edx = temp 2

**Swapping Occurs Here**
    14df:       88 54 05 f2             mov    BYTE PTR [rbp+rax*1-0xe],dl   ; Puts 2nd byte in first position

    14e3:       b8 04 00 00 00          mov    eax,0x4

    14e8:       2b 45 ec                sub    eax,DWORD PTR [rbp-0x14]     ; 4-[rbp-0x14] (reading backwards)

    14eb:       48 98                   cdqe

    14ed:       0f b6 55 ea             movzx  edx,BYTE PTR [rbp-0x16]      

    14f1:       88 54 05 f2             mov    BYTE PTR [rbp+rax*1-0xe],dl  ; Puts 1st byte in 2nd position
**Swapping Ends here

    14f5:       83 45 ec 01             add    DWORD PTR [rbp-0x14],0x1     ; Adds 1 to [rbp-0x14]

    14f9:       83 7d ec 01             cmp    DWORD PTR [rbp-0x14],0x1     ; Compares [rbp-0x14] with 1

    14fd:       7e b8                   jle    14b7 <strerror@plt+0x307>    ; If <= 1, jump to line 14b7

    14ff:       48 8d 3d f2 0d 00 00    lea    rdi,[rip+0xdf2]        # 22f8 <strerror@plt+0x1148>
    1506:       e8 15 fc ff ff          call   1120 <puts@plt>
    150b:       48 8d 45 f2             lea    rax,[rbp-0xe]
    150f:       ba 05 00 00 00          mov    edx,0x5
    1514:       48 8d 35 f5 2a 00 00    lea    rsi,[rip+0x2af5]        # 4010 <strerror@plt+0x2e60>
    151b:       48 89 c7                mov    rdi,rax
    151e:       e8 4d fc ff ff          call   1170 <memcmp@plt>
```

`Summary`

[rbp-0x14] - Counter
[rbp-0x16] - first byte (let's say a) 
[rbp-0x15] - second byte (let's say b) (we count this backwards)

We are basically swapping it like:
temp = b
b = a
a = temp

Then counter increases and "A" is the next value forwards and "B" is the previous value backwards.

This iteration happens twice.

So basically, this program is `reversing` the input.

Now I just need to find the expected output which is stored at address [rip+0x2af5] i.e `0x1514 + 0x2af5 = 4009` + 5 bytes.

To do this, I used the following instruction : `objdump -s --start-address=0x4009 --stop-address=0x4015 ./babyrev-level-3-1`

![alt text](./ReverseEngineering/Images/Level3.1(1).png)

This means the expected value is `jggov`

Therefore, the input should be : `voggj`

![alt text](./ReverseEngineering/Images/Level3.1(2).png)

This was correct and I got the flag.

## My Learning

1. al - Lowest 8 bits of rax
   dl - Lowest 8 bits of rdx

2. cdqe - Converts a signed doubleword (32-bit) in eax to a signed quadword (64-bit) in rax

## Flag

`pwn.college{s6i290aAY0CVkYr5ADCaHFtKaZf.0lN1IDLzITO0czW}`



