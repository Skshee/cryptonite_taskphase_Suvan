# Level 3.0

## Challenge Goals

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

So I opened the challenge and ran the `babyrev-level-3-0` program and it looked like this.

![alt text](./ReverseEngineering/Images/Level3.0(1).png)

So basically the input is being reversed in this program.

Our expected output in hexadecimal is `68 76 66 73 79` which means that our input should be the reverse of this.

Input : `79 73 66 76 68` in hexadecimal
        = `ysfvh`

And by giving this input, we get the flag

![alt text](./ReverseEngineering/Images/Level3.0(2).png)

## Flag

`pwn.college{oNmSYHwrQoWN3cdLn-LidTWug3w.0VN1IDLzITO0czW}`