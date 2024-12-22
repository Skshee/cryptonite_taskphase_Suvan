# Level 1.1

## Challenge Goals

Reverse engineer this challenge to find the correct license key.

## Approach

So I opened the challenge and ran the `babyrev-level-1-1` program and it basically asked for a key and compared it to some hidden value and gave us the flag if it was correct.

![alt text](./ReverseEngineering/Images/Level1.1(1).png)

`Attempt 1` - Firstly I used the `strings` command to see what string files are there and maybe there's a chance our key is there. However, there wasn't any useful strings (Or was there....).

`Attempt 2` - Then I used the `gdb decompiler` to run the decompile the code. I spent a lot of time trying to figure something out here. However, I noticed two strange things when I was using gdb
1. There was no main function 

2. I wasn't able to set any breakpoints and most of the instructions were unusable(maybe it was done on purpose).

3. The absence of main function got me questioning how this program is actually running. Then I used the following `info functions` to see all functions in the program.

![alt text](./ReverseEngineering/Images/Level1.1(2).png)

Okay so first thing, they're all PLT(Procedure Linkage Table) files.

PLT files are basically dynamically linked entries that can call external library functions like printf,read etc.

And I saw there are 3 functions that might be useful : `read, puts and memcmp`

`Attempt 3` - Having gotten some idea abt the code and it's functions, I decided to open it's binary file as gdb couldn't help much.

I went through the entire assembly code using objdump searching for any calls to `memcmp` as that is the function that compares the values.

![alt text](image.png)
 
So what's happening here is the program takes in input from the user and compares it with the value stored at address `[rip+0x2b46]` where rip is the instructional pointer.

It takes 5 bytes from [rbp-0xe] and compares them with another memory location using memcmp.

So now I just had to find what value is stored at the given address.

Address = 0x14c3 + 0x2b46 = 0x4010

For this I used the following instruction - ` objdump -s --start-address=0x4010 --stop-address=0x4015 ./babyrev-level-1-1`

And this is the output I got

![alt text](./ReverseEngineering/Images/Level1.1(4).png)

Therefore, the string **hjtmd** must be our key.

![alt text](./ReverseEngineering/Images/Level1.1(5).png)

And yay, that worked.

## My learning

1. I learnt how to get information abt functions in gdb and what PLTs are

2. Objdump and how to search for certain addresses in objdump

## Flag

`pwn.college{k8r0DsoiLuvAwF1LSXvh66k3Tj8.0lM1IDLzITO0czW}`

