---
layout: writeup
category: Lag and Crash 2.0
chall_description: https://www.lagncrash.com/challenges#Escape%20From%20Gulag-44
points: 1000
solves: 1
tags: pwn
date: 2022-03-25
comments: false
---
## Description

Batman has sentenced Joker to Gulag for lifetime. If you want to be heavily rewarded, help Joker break out from Gulag.

‎



## Solution

Upon connecting to the server, I can see that I have to select a shell. However, most of the common shells which do not exist

![image](https://user-images.githubusercontent.com/62169971/158009638-46e2b521-d9c0-4f2e-a7e0-0d7626f23524.png)

‎


I tried injecting in commands however they don’t work either. 

![image](https://user-images.githubusercontent.com/62169971/158009649-556c3b0f-3ad6-4391-87a8-6aba734a50af.png)

‎


So, after spending some time on research, I finally got something different for the output after keying in `rbash`. I got my hints from the title (escape from prison - restrictive) and after seeing it doesn't accepts lots of commands.

![image](https://user-images.githubusercontent.com/62169971/158009690-508961e4-ab4e-43b9-af47-98c8ae6d2c3f.png)

‎


So, I have tried common commands, however, some doesn’t exist. This makes sense because the commands are executed in rbash (restricted bash).

![image](https://user-images.githubusercontent.com/62169971/158009698-e5170669-5d44-4a66-9b66-12cd7a61b1a3.png)

‎


So, from looking in the bin file, we can safely assume the files listed in there are the commands I can execute. This is because I was able to execute `ls`. To confirm this, I also executed `echo` which didn’t restrict me from doing so

![image](https://user-images.githubusercontent.com/62169971/158009783-1fd675c8-837d-4f94-b122-6143280c0fbe.png)

‎


I did some research on `rbash` bypass however all those methods failed. 1 of the methods included using python to spawn a shell, however, it looked like was not able to execute `python3` even though it was listed in the bin folder. 

![image](https://user-images.githubusercontent.com/62169971/158009798-4ce9d5f5-d4a6-4574-9368-7ce8f81bb880.png)

‎


Looking at the bin folder, one of the commands looks very suspicious that it has been deliberately placed there for something. The command was `arp`. So, I decided to list the features of it.

![image](https://user-images.githubusercontent.com/62169971/158009807-39691316-6556-43bc-8dbd-55a78b32dd49.png)

‎


Looking at it, it looked like I was able to display the content of files using `-f` flag. `-v` flag can be used to verbosely display the file content -f. So, after playing around I found something a way to privilege escalate after listing `/etc/passwd` (Note: for some reason, it takes around 10s to execute `arp -f -v /etc/passwd`)
The user notroot hash was listed in passwd file

![image](https://user-images.githubusercontent.com/62169971/158009855-9dc6a29a-9a98-4b24-8c74-3e115b910480.png)

‎


I then use a dictionary attack to crack the hash using john the ripper. The entire processing of cracking took me between 10min-15min. 

`john --wordlist=/usr/share/wordlists/rockyou.txt pass`

![image](https://user-images.githubusercontent.com/62169971/158009865-3f53e250-c9af-49f0-ab3c-b116545d4cb0.png)

‎


After playing around, I realised I was able to use command su located in the bin folder to execute non-restricted commands as notroot user. However, since the shell is not interactive, I must find a way to parse the password into su command thus coming up with the following command

`echo zenisluffy | su notroot -c '<command>'`

‎


After some time of playing around, I realised that there was something located in notroot’s .bash_history. This could probably be the file where the flag was stored. 

![image](https://user-images.githubusercontent.com/62169971/158009872-813de3fe-79fd-4bd3-8c23-cdaa61ab1695.png)

‎


To locate this file, I decided to use the find command. Turns out it was located at `/run/systemd/.systemd/ert73uegdjd83hddyxt.txt`

![image](https://user-images.githubusercontent.com/62169971/158009881-5cb9c299-377b-42ad-a521-66f30d495987.png)

‎


Finally, I got the flag

![image](https://user-images.githubusercontent.com/62169971/158009886-15f0572d-e9e5-4221-996d-9538af4b442e.png)