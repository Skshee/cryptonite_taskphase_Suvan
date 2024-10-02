# Introduction to Commands

The Hello Hackers Module is a series designed to introduce one to the world of Linux and the command line interface.

## Basic Terminologies

**Secure Shell(ssh)** - A network protocol that allows us to connect to a host computer from a remote network through a secure encrypted medium.

**$ - Command Prompt** - It is the shell’s way of indicating that the shell is ready to accept the next command

## Challenge Goal 

The goal of this level is to invoke a command and obtain a flag after entering the right command.

After I start the challenge on my browser's Linux Luminarium,I used **ssh -i ./key hacker@dojo.pwn.college** to connect to the server where I'll be solving the challenge from my local computer network.

![Error in loading image](image.png)

As you can see once we have logged in, my username i.e suvan has changed to hacker and my hostname i.e Suvan has changed to hello-intro-to-commands.

The command that I need to enter here to obtain the flag is hello.

**Command** - hello

After entering this command, I successfully obtained the flag.

## Flag

**pwn.college{4x8mI8ENOTBDP6vNMNmIi859lGE.ddjNyUDLzITO0czW}**
