import sys
import socket
import string
import time
from random import randint
import pprint
import connection
import functions
import topichandler

def main():
	f = open('log.txt', 'w') #Opening the log txt file

	s = connection.get_connection()
	topichandler.update_topic(s)
	connection.announce(s)

	# Loop
	while 1:
		text = s.recv(2040)
		print text # WIP Print received text to console
		user = text.split('!')[0][1:]
		f.write(text) # Write the text to file
		print user # WIP Print the username spoken
		if text.find('PING') !=-1: # This is to respond to the server when pinged, otherwise the bot will get kicked.
			s.send("PONG %s\r\n")
		if text.find('!help') !=-1:
			functions.list(s)
		if text.find('!hashrate') !=-1:
			functions.printnetworkhash(s)
		if text.find('!pools') !=-1:
			functions.printpools(s, user)
		if text.find('!getdifficulty') !=-1:
			functions.printdifficulty(s)
		if text.find('price') !=-1:
			functions.printexchanges(s)
		if text.find('!credits') !=-1:
			functions.credits(s)
		if text.find('!exchanges') !=-1:
			functions.printexchanges(s)
		if text.find('!tip') !=-1:
			functions.tips(s)
		if text.find('!settopic') !=-1:
			topichandler.setrandom(s, user, text[text.find('!settopic')+10:])
		if text.find('!setversion') !=-1:
			topichandler.setversion(s, user, text[text.find('!setversion')+12:])
		if text.find('!restoretopic') !=-1:
			topichandler.update_topic(s)

main()