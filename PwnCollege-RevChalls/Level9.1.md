# Level 9.1

## Challenge Objectives

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 5 bytes in the binary.

## Approach

Pretty much the same approach as the previous level, this time I did it directly from looking at the assembly instead of using IDA.

![alt text](./ReverseEngineering/Images/Level9.1(1).png)

`Offset : 21e4`
`New value : 74`

![alt text](./ReverseEngineering/Images/Level9.1(2).png)

## Flag

`pwn.college{4fOlEzParG2no08TPTHdydAMX4F.0FO2IDLzITO0czW}`