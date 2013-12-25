import sys
import socket
import string
import time
from random import randint

HOST="irc.freenode.net"
PORT=6667
NICK="FedoraMon"
IDENT="CephonBot1"
REALNAME="CephonBot"
CHAN="#cephbot"
readbuffer=""

f = open('log.txt', 'w') #Opening the log txt file

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r!\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "I am FedoraCoinBot version Beta 1.0. !help for info"))

# Loop
while 1:
 text=s.recv(2040)
 print text # WIP Print received text to console
 user = text.split('!')
 f.write(text) # Write the text to file
 print user[0] # WIP Print the username spoken
 if text.find('PING') !=-1: # This is to respond to the server when pinged, otherwise the bot will get kicked.
	s.send("PONG %s\r\n")