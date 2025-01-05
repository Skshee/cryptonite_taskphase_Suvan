# Day 4 : I’m all atomic inside!

## Learning Objectives
- Learn how to identify malicious techniques using the MITRE ATT&CK framework.
- Learn about how to use Atomic Red Team tests to conduct attack simulations.
- Understand how to create alerting and detection rules from the attack tests.

**"Atomic Red Team"** is a library of simple tests to simulate attacks. 

## Identifying the Atomic Test

It is suspected that the attacked is the MITRE ATT&CK technique `T1566.001 Spearphishing`.

1. Opened up Powershell and gave the command `Invoke-AtomicTest T1566.001 -ShowDetails`. This command displays the details of all tests included in the T1566.001 Atomic.

2. The output we got was split up into multiple parts, each matching a test. Now we carry out our first test. We added the `-Checkprereq` flag which `orovides a check if all necessary components are present for testing`.

![alt text](./Images/Day4(1).png)

This shows that all prerequisites are met.

3. We do the same for `Testnumbers -2` but this not all prereqs are met and we need to install MS Word.

## Detecting the Atomic

1. Now we need to look for log entries of this attack. For that we can use `Windows Event Logs`.To make it easier to pick up the events created for this emulation, I cleaned up files from the previous test by running the command `Invoke-AtomicTest T1566.001 -TestNumbers 1 -cleanup.`

2. This VM has a System Monitor called Sysmon. We can access it on Applications and Services => Microsoft => Windows => Sysmon => Operational. Then I right clicked it and click `Clear Logs`. And then I ran the the first command Of Testnumbers 1 again

From that I found this

![alt text](./Images/Day4(2).png)

It creates these 2 files in `/tmp folder`.

3. I opened `PhisingAttachment.txt` and found the flag : `THM{GlitchTestingForSpearphishing}` which answers our first question

4. For the 2nd question we had to give the ATT&CK ID for out point of interest and the hint told me to look up for ` MITRE ATT&CK technique ID for Command and Scripting Interpreter.` I googled it and got the ID : `T1059`. Again for the 3rd question also I googled and got `T1059.003`

5. For the next question I gave the following command : `Invoke-AtomicTest T1059.003 -ShowDetails` and found this :

![alt text](./Images/Day4(3).png)

So we find that `Simulate BlackByte Ransomware Print Bombing` is the name of the Atomic test and the test number is 4.

6. I passed this command : `Invoke-AtomicTest T1059.003 -Testnumbers 4` and again went to the Event Viewer and found a File named `Wareville_Ransomware.txt`. Upon opening this file, I got the flag
`THM{R2xpdGNoIGlzIG5vdCBOaGUgZW5lbXk=}`

![alt text](./Images/Day4(4).png)





