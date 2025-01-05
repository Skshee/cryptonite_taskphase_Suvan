# Day 1 : Maybe SOC-mas music, he thought, doesn't come from a store?

## Investigating the Website

In this level, we're investigating a website which converts Youtube Videos into .mp3 or .mp4 files.

1. 
So after I pasted a YT video link, downloaded the file and extracted it contents, I found 2 file called `song.mp3 and somg.mp3`

I tried to see what kind of files these 2 files were using the `file command` on the Linux terminal.

**Song.mp3** - This was an audio file, looked legit with no issues

**Somg.mp3** - This was a MS Windows shortcut and had command line arguments, which was suspicious

Now to see more info about the file, I used the `exiftool command`.

Exiftool is used to read the metadata of a file

![alt text](./Images/1(1).png)

Using exiftool on song.mp3, I found the artist's name and it was `Tyler Rumsbey`. Finding this was one of the goals of this challenge

I then used exiftool on somg.mp3 and found this:

![alt text](./Images/1(2).png)

2. 
Interestingly, I found that the command line arguments are coming from this Github profile : https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1'

On opening this, I found the function to send stolen info to C2 server(command and control server):

![alt text](./Images/1(3).png)


3. 
Next I needed to find out the identity of M.M.

For that I opened the commit log of M.M given on the website : https://github.com/search?q=%22Created+by+the+one+and+only+M.M.%22&type=issues

I found a conversation between M.M and another user called Bloatware and it seems like both of them were involved in this glitch.

I did more background search on M.M by opening his Github profile and opening the repository called `M.M` as it mentioned `Config files for my GitHub profile` which is basically used to setup a Github user's profile.

![alt text](./Images/1(4).png)

And there, I found out that M.M's real name is `Mayor Malware`.

4. 
Finally I needed to find out the number of commits on the Github repo where the issue was raised.

I had already found the conversationg b/w M.M and Bloatware where the issue was raised and opened that server which was `CryptoWallet-Search`.

And there I found the number of commits

![alt text](./Images/1(5).png)

And that's all we need to do for this challenge.


![alt text](./Images/1(6).png)

## My Learning 

1. What is OPSEC

2. Using Exiftool to read metadata of a file

3. A C2 server, or command and control server, is used by attackers to maintain communications with compromised systems within a target network.
