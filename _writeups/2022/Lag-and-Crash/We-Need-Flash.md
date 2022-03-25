---
layout: writeup
category: Lag and Crash 2.0
chall_description: https://www.lagncrash.com/challenges#We%20Need%20Flash-45
points: 1000
solves: 0
tags: pwn
date: 2022-03-25
comments: false
---
## Description

Have you heard the news. Flash got defeated by Reverse Flash and he is no where to be seen. We need someone to protect the central city. We need a new Flash!

‎



## Solution

Upon connection, I got the following message from the server. So, there will be a test I have to complete.

![image](https://user-images.githubusercontent.com/62169971/156935065-81f3ffc6-3a9e-4a98-a3c8-0ec8da5b3dcb.png)

‎


To start the test, I just hit enter and then I was thrown 1 question.

![image](https://user-images.githubusercontent.com/62169971/156935075-9626be3f-5443-49f1-b99b-561a0cc2260e.png)

‎


Approximately after 2s, the following statement was shown before I got disconnected from the server. It seemed like I had to answer the question in a nick of time

![image](https://user-images.githubusercontent.com/62169971/156935085-ce09216a-aa69-46b1-bcf6-a839e97a3e3a.png)

‎


When I tried it again with a random answer, it shows the following statement before disconnecting me from the server. I also noticed that the question changes, so its not the same as the previous ones

![image](https://user-images.githubusercontent.com/62169971/156935107-2ddb6afc-1490-45f2-96a8-75fbf6eb410d.png)

‎


I decided to explore and tried to start the test again. This time I was thrown a totally different question. It was about emoji math?

![image](https://user-images.githubusercontent.com/62169971/156935117-a97f0608-eb03-4909-91ee-a4ae3278a980.png)

‎


After spamming the test multiple times, I was thrown something called Anti Bot Clearance Check. The question it asked was pretty simple. Also, I took note that the probability of it appearing was very low.

![image](https://user-images.githubusercontent.com/62169971/156935134-983c2792-6d21-4ea4-9978-fb307f5dd8b4.png)

‎


I tried spamming the test multiple times again so that I could be thrown a bot check question. When it appeared again, I decided to answer it correctly. I noticed that I was given more time to answer the anti bot questions. After a correct answer, I was finally thrown a 2nd question which is the first thing I saw when I attempted the challenge the first time (the question changes)

![image](https://user-images.githubusercontent.com/62169971/156935155-bfd14cbd-a060-4794-a69d-979ea288d559.png)

‎


So, after my observation, I realized that to answer these questions before I get kicked out, I can’t do it manually. It requires scripting. I first need to know how I can solve the emoji math & random bytes of the string.

To solve the weird-looking string, we need to decode it with base85. I know that by looking through multiple samples of that question and noticed that it is within the 85th ASCII char. 

So, from this, when I decode it:

```
.k<,#.k<,#.k=gf.k<,#.m,Ch4tA-6.k<5V/R9kW.k<,#.k<,#><XPf.k<,4/R:Oj/mBo5.k<,#.k<,#.k=gf.k<,#4=si&.k<5V/R9kW.k<,#.k<,#><XPf.k<,4/R:Oj.kY$X>q7EU.k<,#.k<,S4tA-6.k<_6>s9bh.kY$X>q7EU.k<,#.k<,S4tA-6.m,Ch4tA-6.k<5V/R9kW.k<,#.k<,#><XPf.k<,4/R:Om>:j,2.k<,#.k<,#.pG1f.k<,#4=si&.k<,#.k<5V/R8
```

I get this:

```
++++++++++[>+++++<-]>+++++.[-]++++++++++[>+++++<-]>+.[-]++++++++++[>++++<-]>++.[-]++++++++++[>+++++<-]>++.[-]++++++++++[>+++++<-]>+++.[-]++++++++++[>++++<-]>+++++.[-]++++++++++[>+++++<-]>.[-]++++++++++[>+++++<-]>++++++.[-]
```

![image](https://user-images.githubusercontent.com/62169971/156935219-e66dc990-f7b2-4cbe-b06f-f4a5cde4418f.png)

‎


From my experience, I know that is what the society calls the `Brainf*ck language`. So, by decoding that further, we get the following math sum.

![image](https://user-images.githubusercontent.com/62169971/156935243-ce0ff78b-b1ef-40c8-aafc-6ded59f75bc1.png)

‎


To automate this process, I can write a simple python script shown below. I do have to install `brainfuck_fuck` library to do this

![image](https://user-images.githubusercontent.com/62169971/156935253-ca36bfbd-c76d-428e-a0cf-b74a7c9686ef.png)

‎


Next, I needed to solve the emoji math. My hypothesis was that I must convert the Emoji Unicode bytes to decimal and then perform the math operations. So, I wrote another python script for that. So, what it does is it receives the emoji data in bytes, does some sanitization before being converted to decimal. Finally, the math is carried out.

![image](https://user-images.githubusercontent.com/62169971/156935794-670a79e2-6d67-4627-aca4-8012c12f235a.png)

‎


The only way to test my hypothesis is to try it out. So, I placed these scripts in a python socket so that they handle data directly from the server. 

![image](https://user-images.githubusercontent.com/62169971/156936267-8dd1dca6-ebc9-4563-b3be-5e24a0003beb.png)

‎


So, I placed them in a loop. Next, I had to solve the Anti-Bot question. One approach was hardcoding where the user records down every possible question for it. I didn’t do this as this was time-consuming and not effective.

Since I know I was given more time to answer the anti-bot questions, I decided to answer them manually. There will be times when we need to research the answer thus running out of time, so what I did was for those questions I failed to answer, I write it down somewhere. So, if it appears again, I could answer it quickly. 

I just wrote this 3-liner code that prompts for my input if it sees a bot question.

![image](https://user-images.githubusercontent.com/62169971/156936289-3b46fe5d-f591-4d61-b44b-a05a3e99f17c.png)

As we can see from the image below, it works like a charm

![image](https://user-images.githubusercontent.com/62169971/156936298-f18a23db-34a8-41c6-a292-243d32789b77.png)

‎


Finally, after solving 200 questions, we are shown an interesting message. It should mean the flag is close. So, I decided to use manual input for these

![image](https://user-images.githubusercontent.com/62169971/156938054-222de227-4b1f-4deb-beab-cb4033b6b8eb.png)

‎


On my 2nd attempt, I tried no command. It showed Command not found error. Then when I tried `ls`, I realized I was too late because I spent more than 5s for my 2nd command.

![image](https://user-images.githubusercontent.com/62169971/156938063-aecfb435-3e73-4c24-81a9-5a14134ea7c4.png)

‎


On my 3rd attempt, after going through the test, I tried `whoami` & `ls`. `whoami` command wasn’t found but `ls` was. It showed that the flag existed in the local directory. I crossed fingers hopping that `cat` would be a valid command

![image](https://user-images.githubusercontent.com/62169971/156938079-53041a91-5e9d-4059-88ca-523842de3f22.png)

‎


On my final attempt, I tried `ls` and `cat flag.txt` which than echoed out the flag

![image](https://user-images.githubusercontent.com/62169971/156938093-b4bb1462-f601-44c6-bce2-ddaee91d8796.png)
