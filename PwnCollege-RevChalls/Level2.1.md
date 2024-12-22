# Level 2.1

## Challenge Goals

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

Alright so I ran the `babyrev-level-2-1` challenge program and this time it did not show what modifications were being done to the input and what the expected value is.

So like babyrev 1-1 I understood that it's time to open the assembly and understand it

1. First I opened `gdb` and used the `info functions` command to get information about the functions being used in the program. I found two interesting functions : `1-read and 2-memcmp`

2. I opened the assembly and found both the read and memcmp functions.

``` asm
    14a9:       e8 b2 fc ff ff          call   1160 <read@plt>
    14ae:       0f b6 45 f3             movzx  eax,BYTE PTR [rbp-0xd]
    14b2:       88 45 f0                mov    BYTE PTR [rbp-0x10],al
    14b5:       0f b6 45 f6             movzx  eax,BYTE PTR [rbp-0xa]
    14b9:       88 45 f1                mov    BYTE PTR [rbp-0xf],al
    14bc:       0f b6 45 f1             movzx  eax,BYTE PTR [rbp-0xf]
    14c0:       88 45 f3                mov    BYTE PTR [rbp-0xd],al
    14c3:       0f b6 45 f0             movzx  eax,BYTE PTR [rbp-0x10]
    14c7:       88 45 f6                mov    BYTE PTR [rbp-0xa],al
    14ca:       48 8d 3d 27 0e 00 00    lea    rdi,[rip+0xe27]        # 22f8 <strerror@plt+0x1148>
    14d1:       e8 4a fc ff ff          call   1120 <puts@plt>
    14d6:       48 8d 45 f2             lea    rax,[rbp-0xe]
    14da:       ba 05 00 00 00          mov    edx,0x5
    14df:       48 8d 35 2a 2b 00 00    lea    rsi,[rip+0x2b2a]        # 4010 <strerror@plt+0x2e60>
    14e6:       48 89 c7                mov    rdi,rax
    14e9:       e8 82 fc ff ff          call   1170 <memcmp@plt>
```

`movx` - Move with Zero-Extend" instruction. Moves a value from source to destination and zero extends to fill the register.

14ae:       0f b6 45 f3             movzx  eax,BYTE PTR [rbp-0xd]
14b2:       88 45 f0                mov    BYTE PTR [rbp-0x10],al

This basically moves the value at [rbp-0xd] to lower bytes of the 32 bit eax register
And then the value of al (the lower 8 bits of eax) is moved into the byte located at [rbp-0x10]


So overall, this piece of code `swaps 1st and 4th indices` of the input.

The expected value is the value at location - [rip+0x2b2a] i.e `0x14df + 0x2b2a = 0x4010`

I found the value at this register using the following instruction:`objdump -s --start-address=0x4010 --stop-address=0x4016 ./babyrev-level-2-1`

![alt text](./ReverseEngineering/Images/Level2.1(1).png)

This means that `esgqo` is our expected value after swapping occurs b/w 1st and 4th index.

Therefore, input should be:`eogqs`

![alt text](./ReverseEngineering/Images/Level2.1(2).png)

And from this, I got the flag.

## My Learning

1. Learnt about `al` and `movx`

## Flag

`pwn.college{wrp5FXSgeeTqpmxlDX0M1aS7niq.0FN1IDLzITO0czW}`

