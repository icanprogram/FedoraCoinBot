import sys
import socket
import string
import time
from random import randint

HOST="irc.freenode.net"
PORT=6667
NICK="FedoraCoinBot420"
IDENT="CephonBot1"
REALNAME="CephonBot"
CHAN="#fedoracoin"
readbuffer=""

f = open('log.txt', 'w')
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r!\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "I am FedoraCoinBot version Alpha 0.06. !help for info"))