# Level 9.0 

## Challenge Objectives

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 5 bytes in the binary.

## Approach

Okay so this was a very interesting challenge and it took me a few hours to crack this.

I opened the challenge and ran the `babyrev-level-9-0` program.

![alt text](./ReverseEngineering/Images/Level9.0(1).png)

And unlike the previous levels, this time it asked me for an Offset(hex) to change and the new value to go with it. Interesting....

It also did an MD5 mangle which is basically a cryptographic hash that cannot be reverse engineering (aah schmucks).

Alright so I figured out that instead of reading through the code like I did in the previous levels, this time I'll need to somehow change the instructions such that it will directly give me the flag upon execution.

1. I went through the entire assembly and couldn't figure out anything then. Then I thought of using the IDA disassembler to see it's graph and hex values 

2. IDA didn't help that much but I did find an interesting part in it

![alt text](./ReverseEngineering/Images/Level9.0(2).png)

```asm 

# Setup for memcmp call
1A86: lea     rax, [rbp+buf]          ; Loads address of buffer into rax
1A8A: mov     edx, 1Ch                ; Sets length to 28 bytes (0x1C)
1A8F: lea     rsi, EXPECTED_RESULT    ; Loads address of expected license key
1A96: mov     rdi, rax                ; First argument for memcmp (the buffer)
1A99: call    _memcmp                 ; Compares the two memory regions

# Check result
1A9E: test    eax, eax               ; Checks if memcmp returned 0 (strings match)
1AA0: jnz     short loc_1AB6         ; If not zero i,e. strings don't match, jump to 1AB6
1AA2          mov     eax, 0   
1AA7          call    win            ; Calls the "win" function
```

Now the interesting part is in line `1AA0`. There is a `jnz` instruction which means `jump if not equal to zero`. That means if the strings don't match it will jump back and not go to the win function.

But, if we convert the `jnz to jz` then it will forward us to the part where the code will behave like the strings match and calls the "win function" which eventually gives us our flag.

However, we need somehow send the appropriate instruction for the "jz" instruction. For this, we need to use `opcodes numbers`. 

`Opcodes, or operation codes, are numeric codes that tell a processor what operation to perform`.

I referred to the opcodes table and found the `opcode for jz is 74`.


So now, I just needed to change the instruction at `Offset - 1AA0 with new hex value : 74`.

![alt text](./ReverseEngineering/Images/Level9.0(3).png)

## My Learning
1. opcodes
2. Even though this level could probably be solved without it, I learnt how to use the IDA decompiler

## Flag
`pwn.college{gdDjH7lAweuu4I3Gs1exRm6twaY.01N2IDLzITO0czW}`