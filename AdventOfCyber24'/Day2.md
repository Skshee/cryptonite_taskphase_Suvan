# Day 2

## Investigating alerts

In this challenge, we're tasked with going through an malicious activity alert and find out whether is it True Positive or False Positive

**True +VE** - Triggers an alert and there is some malicious activity going on

**False +VE** - Triggers an alert but no malicious activity

We have been informed that an alert was issued on December 1st, 2024, between 9:00 - 9:30

1. So I opened the `Discover` tab and set the timeframe from Dec 1st 9:00:00 hrs to 9:30:00

2. I found 21 activities during this time frame. I added the following filters `host.hostname, user.name, event.category, process.command and event.outcome`.

3. Then I found that there were some suspicious powershell commands followed by an authentication which was successful.

4. Then I added the `source.IP` filter and found the IPs only showed up in authentications and it's IP was `10.0.11.11`.

5. However we don't see the initial connection, so I extended the timeline to November 29th 00:00:00

6. Now we filter out the events with `username: service-admin, event.category: authetication and NOT source.ip:10.0.11.11`

7. We find that there were a lot of brute force attempts and one of the was successful on `IP 10.0.255.1` and hostname was ADM-01. It has compromised the service-admin user and they executed a lot of Powershell commands

![alt text](./Images/dAY2(3).png)

8. Then we found the powershell command with encoded text

![alt text](./Images/Day2(1).png)

9. By putting it into Cyberchef I got this message

![alt text](./Images/Day2(2).png)

10. To find the number of failed attempts, I set the `event.category:authetication and event.outcome:failure`.

![alt text](./Images/Day2(4).png)

![alt text](image.png)

# My learning

1. Analyzing events and alerts using a SIEM (Security Information and Event Management)




