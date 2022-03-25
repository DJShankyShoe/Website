---
layout: writeup
category: Lag and Crash 2.0
chall_description: https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/dp.png
points: 1000
solves: 1
tags: pwn
date: 2022-03-25
comments: false
---
### Upon connecting to the server, I can see that I have to select a shell. However, most of the common shells which do not exist

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/connection.png)

‎


### I tried injecting in commands however they don’t work either. 

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/command.png))

‎


### After spending some time on research, I finally got something different for the output after keying in `rbash`. I got my hints from the title (escape from prison - restrictive) and after seeing it doesn't accepts lots of commands.

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/rbash.png)

‎


### I have tried common commands, however, some doesn’t exist. This makes sense because the commands are executed in rbash (restricted bash).

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/shell.png)

‎


### From looking in the bin file, we can safely assume the files listed in there are the commands I can execute. This is because I was able to execute `ls`. To confirm this, I also executed `echo` which didn’t restrict me from doing so

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/bin.png)

‎


### I did some research on `rbash` bypass however all those methods failed. 1 of the methods included using python to spawn a shell, however, it looked like was not able to execute `python3` even though it was listed in the bin folder. 

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/python3.png)

‎


### Looking at the bin folder, one of the commands looks very suspicious that it has been deliberately placed there for something. The command was `arp`. So, I decided to list the features of it.

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/arp.png)

‎


### Looking at it, I was able to display the content of files using `-f` flag. `-v` flag can be used to verbosely display the file content -f. So, after playing around I found something a way to privilege escalate after listing `/etc/passwd` (Note: for some reason, it takes around 10s to execute `arp -f -v /etc/passwd`)
The user notroot hash was listed in passwd file

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/passwd.png)

‎


### I then use a dictionary attack to crack the hash using john the ripper. The entire processing of cracking took me between 10min-15min. 

```
john --wordlist=/usr/share/wordlists/rockyou.txt pass
```

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/john.png)

‎


### After playing around, I realised I was able to use command su located in the bin folder to execute non-restricted commands as notroot user. However, since the shell is not interactive, I must find a way to parse the password into su command thus coming up with the following command

```
echo zenisluffy | su notroot -c '<command>'
```

‎


### After some time of playing around, I realised that there was something located in notroot’s .bash_history. This could probably be the file where the flag was stored. 

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/history.png)

‎


### To locate this file, I decided to use the find command. Turns out it was located at 
```
/run/systemd/.systemd/ert73uegdjd83hddyxt.txt
```

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/find.png)

‎


### Finally, I got the flag

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/Escape%20From%20Gulag/images/flag.png)