import json
import requests
import connection

def printpools(s, user):
	url = 'http://cphn.ml/res/pools.json'
	resp = requests.get(url=url)
	pools = json.loads(resp.content)
	connection.send_user(s, user, "I know about these pools:")
	for pool in pools:
		verified = 'yes' if pool['verified'] else 'no'
		connection.send_user(s, user, "\t%s: fee %i%%, verified: %s, url: %s" % (pool['name'], pool['fee'], verified, pool['url']))

def printnetworkhash(s):
	url = 'http://fedoracore.x64.me/index.php?page=api&action=public'
	resp = requests.get(url=url)
	stats = json.loads(resp.content)
	connection.send_channel(s, "The current network hashrate is %s M/s" % (int(stats['network_hashrate'])/1000000))

def printblockcount(s):
	url = 'http://fedorachain.info/chain/Fedora/q/getblockcount'
	block = requests.get(url=url).content
	connection.send_channel(s, block)

def credits(s):
	connection.send_channel(s, "My creators are Cephon and icanprogram!")

def printdifficulty(s):
	url = 'http://fedorachain.info/chain/Fedora/q/getdifficulty'
	diff = requests.get(url=url).content
	connection.send_channel(s, diff)

def printexchanges(s):
	connection.send_channel(s, "You can't put a price on euphoria.")

def tips(s):
	connection.send_channel(s, "Please send your tips to:")
	connection.send_channel(s, "EM2CUbsmB5wLqDfd5ji71DAWo7mryXEo2U.")
	connection.send_channel(s, "or EXyrAaLMj8wEDx5oWvZKvKfN4ciH2YN4jj")

def list(s):
	connection.send_channel(s, "These are the main bot comamnds:")
	connection.send_channel(s, "\t!hashrate: Shows the current network hashrate")
	connection.send_channel(s, "\t!pools: Shows currently active pools (maintained by Cephon)")
	connection.send_channel(s, "\t!getblockcount: Shows the current block number")
	connection.send_channel(s, "\t!getdifficulty: Shows the current difficulty")
	connection.send_channel(s, "\t!exchanges: Shows the current worth of 1 TIP in USD")
	connection.send_channel(s, "\t!settopic: Tell everyone in the channel what's on your mind")
	connection.send_channel(s, "\t!credits: Find out who made this bot!")
	connection.send_channel(s, "\t!tip: Show the address to tip us at!")
	connection.send_channel(s, "\tExtra Commands can be found at [pastebin link]")
