---
layout: writeup
category: Lag and Crash 2.0
chall_description: https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/dp.png
points: 1000
solves: 0
tags: pwn
date: 2022-03-25
comments: false
---
### Upon connection, I got the following message from the server. So, there will be a test I have to complete.

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/connection.png)

‎


### To start the test, I just hit enter and then I was thrown 1 question.

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/1st.png)

‎


### Approximately after 2s, the following statement was shown before I got disconnected from the server. It seemed like I had to answer the question in a nick of time

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/slow.png)

‎


### When I tried it again with a random answer, it shows the following statement before disconnecting me from the server. I also noticed that the question changes, so its not the same as the previous ones

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/wrong.png)

‎


### I decided to explore and tried to start the test again. This time I was thrown a totally different question. It was about emoji math?

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/emoji.png)

‎


### After spamming the test multiple times, I was thrown something called Anti Bot Clearance Check. The question it asked was pretty simple. Also, I took note that the probability of it appearing was very low.

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/anti-bot.png)

‎


### I tried spamming the test multiple times again so that I could be thrown a bot check question. When it appeared again, I decided to answer it correctly. I noticed that I was given more time to answer the anti bot questions. After a correct answer, I was finally thrown a 2nd question which is the first thing I saw when I attempted the challenge the first time (the question changes)

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/pass.png)

‎


### So, after my observation, I realized that to answer these questions before I get kicked out, I can’t do it manually. It requires scripting. I first need to know how I can solve the emoji math & random bytes of the string.

### To solve the weird-looking string, we need to decode it with base85. I know that by looking through multiple samples of that question and noticed that it is within the 85th ASCII char. 

### So, from this, when I decoded it:

```
.k<,#.k<,#.k=gf.k<,#.m,Ch4tA-6.k<5V/R9kW.k<,#.k<,#><XPf.k<,4/R:Oj/mBo5.k<,#.k<,#.k=gf.k<,#4=si&.k<5V/R9kW.k<,#.k<,#><XPf.k<,4/R:Oj.kY$X>q7EU.k<,#.k<,S4tA-6.k<_6>s9bh.kY$X>q7EU.k<,#.k<,S4tA-6.m,Ch4tA-6.k<5V/R9kW.k<,#.k<,#><XPf.k<,4/R:Om>:j,2.k<,#.k<,#.pG1f.k<,#4=si&.k<,#.k<5V/R8
```

<h3 style="color:aqua;">‎I got this:</h3>

```
++++++++++[>+++++<-]>+++++.[-]++++++++++[>+++++<-]>+.[-]++++++++++[>++++<-]>++.[-]++++++++++[>+++++<-]>++.[-]++++++++++[>+++++<-]>+++.[-]++++++++++[>++++<-]>+++++.[-]++++++++++[>+++++<-]>.[-]++++++++++[>+++++<-]>++++++.[-]
```

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/decode.png)

‎


### From my experience, I know that is what the society calls the `Brainf*ck language`. So, by decoding that further, we get the following math sum.

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/brain.png)

‎


### To automate this process, I can write a simple python script shown below. I do have to install `brainfuck_fuck` library to do this

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/script1.png)

‎


### Next, I needed to solve the emoji math. My hypothesis was that I must convert the Emoji Unicode bytes to decimal and then perform the math operations. So, I wrote another python script for that. So, what it does is it receives the emoji data in bytes, does some sanitization before being converted to decimal. Finally, the math is carried out.

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/script2.png)

‎


### The only way to test my hypothesis is to try it out. So, I placed these scripts in a python socket so that they handle data directly from the server. 

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/script3.png)

‎


### So, I placed them in a loop. Next, I had to solve the Anti-Bot question. One approach was hardcoding where the user records down every possible question for it. I didn’t do this as this was time-consuming and not effective.

### Since I know I was given more time to answer the anti-bot questions, I decided to answer them manually. There will be times when we need to research the answer thus running out of time, so what I did was for those questions I failed to answer, I write it down somewhere. So, if it appears again, I could answer it quickly. 

### I just wrote this 3-liner code that prompts for my input if it sees a bot question.

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/script4.png)

‎


### As we can see from the image below, it works like a charm

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/script5.png)

‎


### Finally, after solving 200 questions, we are shown an interesting message. It should mean the flag is close. So, I decided to use manual input for these

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/script6.png)

‎


### On my 2nd attempt, I tried no command. It showed Command not found error. Then when I tried `ls`, I realized I was too late because I spent more than 5s for my 2nd command.

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/attempt1.png)

‎


### On my 3rd attempt, after going through the test, I tried `whoami` & `ls`. `whoami` command wasn’t found but `ls` was. It showed that the flag existed in the local directory. I crossed fingers hopping that `cat` would be a valid command

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/attempt2.png)

‎


### On my final attempt, I tried `ls` and `cat flag.txt` which than echoed out the flag

![image](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/images/solve.png)

‎



## Solution Script

![bot.py](https://raw.githubusercontent.com/DJShankyShoe/Website/master/assets/CTFs/2022/Lag-and-Crash-2.0/We%20Need%20Flash/scripts/bot.py)