# Level 1

## Challenge Goal 

Reverse engineer this challenge to find the correct license key.

## Approach

When I opened the challenge and used the ls command, I found a file called `babyrev-level-1-0`.

This is the file from which we had to reverse engineer and obtain the license key.

`Attempt 1` - So the first thing I did was analyse the strings in the program using the strings command. However, I did not obtain anything useful from this.

`Attempt 2` - Next I thought of debugging this program using gdb debugger

Then I set a breakpoint at main and ran the program.
![alt text](./Images/Level1.0(1).png)

I gave the input "n" as argument to see what happens and this is what I got.

![alt text](./Images/Level1.0(2).png)

Then I found the expected hexadecimal format of the license key. 

I converted the hexadecimal to ASCII using an online converter and got this string - `kwlpg`

I sent in this string as my argument and tada I got the flag

![alt text](./Images/Level1.0(3).png)

Upon solving this I realised, I could've simply run this program on Linux myself instead of debugging it or checking it's strings or anything and it would've have been simpler.

## My Learning

1. In general, run the program first before debugging or disassembling it
2. How to use the gdb debugger

## Flag
`pwn.college{8cKNMozEbLmPrFAphlrFM7LYEE2.0VM1IDLzITO0czW}`