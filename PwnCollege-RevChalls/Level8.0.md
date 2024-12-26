# Level 8.0

## Challenge Objectives

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.

## Approach

I opened the challenge and ran the `babyrev-level-8-0` program.

![alt text](./ReverseEngineering/Images/Level8.0(1).png)

Okay a lot of the steps are unnecessary to reverse engineer this challenge.

Essentially, we just have to sort the final expected value and reverse it.

After doing that I got these hexadecimal values - `7a, 79, 78, 78, 78, 77, 77, 76, 76, 75, 74, 74, 73, 71, 6e, 6e, 6d, 6b, 6a, 6a, 69, 69, 69, 68, 67, 67, 67, 66, 66, 65, 65, 65, 65, 64, 64, 63`

On converting to ASCII we get this - `zyxxxwwvvuttsqnnmkjjiiihgggffeeeeddc`

And I got the flag

![alt text](./ReverseEngineering/Images/Level8.0(2).png)

## Flag

`pwn.college{caViYdn29I9bHEjc0vfC-OccD6o.0VN2IDLzITO0czW}`