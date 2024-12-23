# Level 4.0

## Challenge Goals

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

I opened the challenge and ran the `babyrev-level-4-0` program and got this:

![alt text](./ReverseEngineering/Images/Level3.1(2).png)

This program basically takes in user input and sorts it in increasing hexadecimal values.

The expected output in hexadecimal is : `61 6b 76 78 7a`

As we can see, this already in sorted form, therefore input : `akvxz`

![alt text](./ReverseEngineering/Images/Level4.0(2).png)

## Flag

`pwn.college{ciVBbIo_k5q7nEl4MSQAjpZpkDR.01N1IDLzITO0czW}`

