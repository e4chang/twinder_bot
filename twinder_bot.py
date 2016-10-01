# twinder_bot.py

import re
import socket
from time import sleep

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "twinder_bot"
PASS = "oauth:u55e0hl74cp4767wxo21tuvqcmmb1m"
CHAN = "#twinder_bot"
JOIN_CMD = "!join"
LEAVE_CMD = "!leave"
CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

s = socket.socket()
s.connect((HOST, PORT))

s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

while True:
    response = s.recv(1024).decode("utf-8")

    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0) # return the entire match
        message = CHAT_MSG.sub("", response)
        if message.strip() == JOIN_CMD:
            print("Joining chat")
        if message.strip() == LEAVE_CMD:
            print("Leaving chat")
        print(username + ": " + message)

    sleep(0.1)
