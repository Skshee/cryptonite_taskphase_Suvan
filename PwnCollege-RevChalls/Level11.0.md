# Level 11.0

## Challenge Objectives

Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 2 bytes in the binary, but performs an integrity check afterwards.

## Approach

Ok so this time, when I first ran the program with random offsets and hex values I got this :

![alt text](./ReverseEngineering/Images/Level11.0(1).png)

Ok so this is different from what I did in the previous levels as this time it isn't showing me the usage of "MD5 mangler" or any expected value.

**Approach 1** -  I went through the assembly and just like the previous level, I changed the "jnz" instruction to "jz" using the opcode 74, however that did not work this time. I tried some similar approaches for a few minutes but it was unsuccessful.

**Approach 2** - This time I decided to open IDA to see the graph view of the flow of the program to understand how it works more clearly. This turned out to be a very useful step.

I found a part of the code that uses the `MD5 mangler`, which did not happen during my initial execution here -

![alt text](./ReverseEngineering/Images/Level11.0(2).png)

So then I opened the assembly code, found the address at which the `jle` instruction was set and tried to change it to `jz` by using the opcode 74.

![alt text](./ReverseEngineering/Images/Level11.0(3).png)

Now I ran the program again with `Offset - 2857 and Hex value - 74` and the other I just left it as 0 and 0.

![alt text](./ReverseEngineering/Images/Level11.0(4).png)

Well this did not give me the flag, however on the bright side, I made some progress and was in the right direction.

I went through IDA again and found another interesting step.

![alt text](./ReverseEngineering/Images/Level11.0(5).png)

This is basically the same thing we did in the previous levels.

I found the address where this `jnz` instruction and changed it to `jz`.

![alt text](./ReverseEngineering/Images/Level11.0(6).png)

So now I ran the program again with :

`Offset 1 : 2857`
`Hex value : 74`

`Offset 2 : 2ae9`
`Hex value : 74`

![alt text](./ReverseEngineering/Images/Level11.0(7).png)

And tada!, I got the flag

## Flag

`pwn.college{UglNiAw8Q8siqOIReasu1pJOWOP.0VM3IDLzITO0czW}`