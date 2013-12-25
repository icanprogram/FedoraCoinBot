import connection

topic_version = "0.43 BINARIES & SOURCES RELEASED, UPDATE ASAP OR RISK HARD FORK!"
topic_site = "http://fedoraco.in/"
topic_random = "Now with 33% more version labels and OS X"

def update_topic(s):
	print "UPDATED"
	print "%s | %s | %s" % (topic_version, topic_site, topic_random)
	connection.set_topic(s, "%s | %s | %s" % (topic_version, topic_site, topic_random))

def setversion(s, user, _version):
	global topic_version
	if(user == "tipsfedora"):
		topic_version = _version
		update_topic(s)

def setrandom(s, user, text):
	global topic_random
	topic_random = ("%s: %s" % (user, text))
	update_topic(s)
