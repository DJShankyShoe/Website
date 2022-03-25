import brainfuck_fuck
import socket
import re
import base64
import os

class DestroyFlash:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.content = b""

    def brain_shut(self, data):
        brain_crap = base64.a85decode(data).decode("utf-8")

        try:
            os.system(f'''python3 -c "import brainfuck_fuck; brainfuck_fuck.fuck('{brain_crap}')" > data.txt''')
            with open("data.txt", "r") as file:
                math = file.read()
            ans = str(eval(math))

        except SyntaxError:
            os.system(f'''python2 -c "import brainfuck_fuck; brainfuck_fuck.fuck('{brain_crap}')" > data.txt''')
            with open("data.txt", "r") as file:
                math = file.read()
            ans = str(eval(math))

        print(ans, end='')

        return ans.encode()

    def emoji(self, data):

        data = data.replace(b" ", b"")
        data_list = re.split(b'\+|-', data)

        math = ""
        pos = 4
        for emoji in data_list:
            math += str(int(emoji.hex(), 16))
            try:
                if data[pos] == 43:
                    math += "+"
                else:
                    math += "-"
                pos += 5
            except IndexError:
                pass

        ans = str(eval(math))
        print(ans, end='')

        return ans.encode()

    def get_content(self):
        self.content = b""
        while b"ANS" not in self.content:
            self.content += self.client.recv(4096)

        print(self.content.decode("utf-8"), end="")

        data = self.content.split(b"\n")
        for line in data:
            if b"# Anti Bot Clearance Check #" in line:
                self.manual("bot")
                break

            elif b"Question" in line:
                question = re.findall(b"Question \d+: (.*)", line)[0]

                if len(question) > 100:
                    ans = self.brain_shut(question)
                else:
                    ans = self.emoji(question)

                self.client.send(ans + b"\n")
                break


    def manual(self, pos):
        if pos == "start":
            temp_content = b''
            while b'Hit Enter to start' not in temp_content:
                temp_content = self.client.recv(4096)
                print(temp_content.decode(), end="")

            input("")
            self.client.send(b"\n")

        if pos == "bot":
            ans = (input("") + "\n").encode("utf-8")
            self.client.send(ans)

        if pos == "end":
            temp_content = b''
            while b'Hit Enter to start' not in temp_content:
                temp_content = self.client.recv(4096)
                print(temp_content.decode(), end="")

            while True:
                reply = (input("") + "\n").encode()
                self.client.send(reply)
                temp_content = self.client.recv(4096)
                print(temp_content.decode(), end="")



    def main(self):
        self.client.connect((self.server_ip, self.server_port))
        self.manual("start")
        while True:
            self.get_content()
            if b"Question 200" in self.content:
                break
        self.manual("end")


DestroyFlash("127.0.0.1", 9005).main()