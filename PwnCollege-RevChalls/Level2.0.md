# Level 2.0

## Challenge Goals

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

Okay so I opened the challenge and ran the `babyrev-level-2-0` program.

![alt text](./ReverseEngineering/Images/Level2.0(1).png)

Okay so the interesting part here is that there is a `swap occuring between indices '0' and '2'` when we're giving the input and that is being compared.

Also we've been given our expected output in hexadecimal format - `78 73 6c 67 63`

Now we know that our input should be such that when the 0th and 2nd index are swapped, it should match the expected hexadecimal value.

Hence, all I had to do was swap the two indices - `6c 73 78 67 63`

Converting this to ASCII we get - `lsxgc`

![alt text](./ReverseEngineering/Images/Level2.0(2).png)

And tada

## Flag

`pwn.college{8FUE-kd02YsgOXSC2aaRpn_42QB.01M1IDLzITO0czW}`