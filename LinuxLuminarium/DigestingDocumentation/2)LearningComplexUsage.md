# Learning Complex Usage

## Challenge Objective

While using most commands is straightforward, the usage of some commands can get quite complex. For example, the arguments to commands like sed and awk, are entire programs in an esoteric programming language!


 Somewhere on the spectrum between cd and awk are commands that take arguments to their arguments.

 For example - find command takes  a specified filename argument to its **"-name"** argument.

 "find -name my_filename"

 Similarly,  many other commands are analogous.

 ## Challenge Goals

**Here is this level's documentation for /challenge/challenge:**

Welcome to the documentation for /challenge/challenge! This program allows you to print arbitrary files to the terminal, when given the **--printfile argument**. The argument to the --printfile argument is the path of the flag to read. For example, **"/challenge/challenge --printfile /challenge/DESCRIPTION.md"** will print out the description of the level!

So in this challenge, I have to run the /challenge/challenge program with the argument **"--printfile"**  and the flag file. The flag file is located at **"/flag"**.

This basically prints the contents of the "/flag" file.

**Command**-  /challenge/challenge --printfile /flag

From this we successfully get the flag.

## Flag

**pwn.college{IhNSOVqCWPNvaKE5GjU1lOnygnM.dVjM5QDLzITO0czW}**

