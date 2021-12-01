---
layout: solution
category: TryHackMe
contest_code: General
contest_name: General
problem_code: AGENT_SUDO
problem_name: Agent Sudo
comments: false
tags: enumeration brute-force
date: 2021-12-01
---

### Basic nmap scan results show that, the machine is running 3 services: ssh, ftp, http

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/nmap.png)

‎


### The page was visited and some interesting information was shown. Thus to gain access to the page, all the alphabets were tried in the user-agent field. There is a faster way to do this using burpsuite bruteforce. 
### Burpsuite proxy was turned on, and the traffic was intercepted. It is then sent to Intruder for a bruteforce attack. Some configurations were made to initiate a bruteforce attack on the User-Agent Field to try all the possible alphabets

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/burp.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/burp_intru.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/burp_crack.png)

<p style="color:orange;">Once the attack was started, the results shows that alphabets C & R in the user-agent field will show a different length page.</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/burp_results.png)

<p style="color:orange;">Thus these pages were visited. First page that was visited was alphabet R in the user agent. It doesn't show anything interesting.</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/result1.png)

<p style="color:orange;">However the 2nd page that was visited with the alphabet C shows us the actual username of the user is chris and he has a weak password</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/result2.png)

‎


### Since we know who the actual username and we know that he has a weak password, we can conduct a dictionary attack on ftp using his username. Thus allowing us to access the contents of his ftp account and retrieve interesting info

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/hydra.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/ftp.png)

‎


### We know steganography was used, thus I used stegoveritas to retrieve any hidden content or files from the png image first. It then extracted a zip file that was carved into the image (the extraction was saved into results directory).
### However, the zip files is encrypted with a password

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/steg.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/7z.png)

‎


### Thus to crack the password of the zip file, zip2john was used and cracked using john the ripper retrieving the password for the zip file and finally extracting the contents of the zip file

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/john.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/result3.png)

‎


### The content `QXJlYTUx`  looks very weird. It might be encoded in base64 and after decoding it, it gives us a text. I then used this text as a passphrase to retrieve the content from the jpeg file using steghide. We then received an interesting message.

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/result4.png)

‎


### Since we know that the site is running ssh, an attempt was made to establish a successful connection with the credentials we got.  That’s how we get the first flag.

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/ssh.png)

‎


### Lastly we need to perform privilege escalation to retrieve the last flag an enumeration was performed including the use of linpeas on the machine after it was uploaded using ncat. 

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/enum.png)

<p style="color:orange;">This permission tells as that james can execute `/bin/bash` as any user except root.</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/nc.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/vuln.png)

<p style="color:orange;">This tells us that, sudo version is 1.8.21 which is highlighted in red that tells us it might be vulnerable. Exploitdb shows that it is vulnerable to security bypass</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/exploitdb.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/exploit.png)

<p style="color:orange;">Thus, by trying the exploit we are able to get root shell and retrieve the final flag</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Agent%20Sudo/priv.png)
