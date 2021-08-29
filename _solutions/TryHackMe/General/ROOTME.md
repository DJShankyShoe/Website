---
layout: solution
category: TryHackMe
contest_code: General
contest_name: General
problem_code: ROOTME
problem_name: RootMe
comments: false
tags: web linux privilege-escalation
date: 2021-08-29
---

### Nmap scan shows that ssh and apache services are running

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/nmap.png)

‎


### The page was visited and didn't showed anything much. Thus gubuster enumeration was used to determine hidden directories and interesting directories was found

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/gobuster.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/index.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/uploads.png)

<p style="color:orange;">So if anything was uploaded on panels page, the file could be seen on uploads page</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/panel.png)

‎


### Thus, a meterpreter reverse php was created to get a shell from the machine by uploading it through the panel site and executing it by visiting the uploaded php page

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/payload.png)

<p style="color:orange;">However, when we tried to upload it, we get an error saying php files are not allowed in Portuguese</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/error.png)

<p style="color:orange;">Thus, it means it is either doing some sort of validation. To bypass this we can use burpsuite to intercept the traffic and modify the MIME type. Another method I used for file bypass was to rename the extension to another valid php extension called php5. In the end, it was successful</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/success.png)

<p style="color:orange;">We can see our file in the uploaded directory</p>

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/stored.png)

‎


### Next we can open the shell.php5 in the browser and a meterpreter shell will be obtained and this is how we get the first flag

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/shell.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/flag1.png)

‎


### Next step is to perform some enumeration for privilege escalation. One good tool I have used was linpeas thus I if have uploaded and executed that and got interesting results where python is executed with SUID bit set to 1.

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/suid.png)

‎


### We can that advantage of that by executing a shell through python that will then return us a root shell. <a href="https://gtfobins.github.io/">GtfoBins</a> shows how you can do this. After getting a root shell, we would be able to retrieve the last flag

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/gtfo.png)

![Image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/RootMe/flag2.png)
