
<p><a href="https://tryhackme.com/room/alfred"><img src="https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/Platforms/TryHackMe/Alfred/pb.png" alt="Alfred"/></a></p><br>

<p>Learning how to exploit a common misconfiguration on a widely used automation server (Jenkins - This tool is used to create continuous integration/continuous development pipelines that allow developers to automatically deploy their code once they made change to it). After which, we'll use an interesting privilege escalation method to get full system access. 

Since this is a Windows application, we'll be using <a href="https://github.com/samratashok/nishang">Nishang</a> to gain initial access. The repository contains a useful set of scripts for initial access, enumeration and privilege escalation. In this case, we'll be using the <a href="https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1">reverse shell scripts</a></p>
