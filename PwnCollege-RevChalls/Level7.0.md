# Level 7.0

## Challenge Objectives

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

I opened the challenge and ran the `babyrev-level-7-0` program.

![alt text](./ReverseEngineering/Images/Level7.0(1).png)

Now I needed to reverse the code and get the right input from the expected output.

With some help for Chatgpt, I wrote a python script that reverse engineers this code - [Babyrev-7.0](./ReverseEngineering/Codes/Level7.0.py)

## My learning

1. XOR with 0xc39eb4 means taking each byte of the target and XORing it with a repeating 3-byte key pattern (0xc3, 0x9e, 0xb4).
When i = 0: i % 3 = 0, so uses 0xc3
When i = 1: i % 3 = 1, so uses 0x9e
When i = 2: i % 3 = 2, so uses 0xb4
When i = 3: i % 3 = 0, so uses 0xc3 again

## Flag

`pwn.college{IZhOBmkGElgbuMFBRNkpS-rpEnw.01M2IDLzITO0czW}`
