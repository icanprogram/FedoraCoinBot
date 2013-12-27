import socket

HOST="irc.freenode.net"
PORT=6667
NICK="FedoraProgramBot"
IDENT="ProgramBot"
REALNAME="ProgramBot"
CHAN="#fedoracoin"
readbuffer=""

def send_channel(s, text):
	s.send("PRIVMSG %s :%s\r\n" % (CHAN, text))

def send_user(s, user, text):
	s.send("PRIVMSG %s :%s\r\n" % (user, text))

def set_topic(s, topic):
	s.send("TOPIC %s :%s\r\n" % (CHAN, topic))

def get_connection():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("NICK %s\r\n" % NICK)
	s.send("USER %s %s bla :%s\r!\n" % (IDENT, HOST, REALNAME))
	s.send("JOIN :%s\r\n" % CHAN)
	
	return s

def announce(s):
	send_channel(s, "Hello! I am ProgramBot version 1.1! Type !help for info.")
