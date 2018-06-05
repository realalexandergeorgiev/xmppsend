#!/usr/bin/python
# can create google account here https://accounts.google.com/SignUp?continue=http%3A%2F%2Fwww.google.de%2F&hl=de

import xmpp
import sys

# destination address (gmail and googlemail makes a difference!) 
to = 'alex@somejabberserver.org'


# if no argument given, ask for message, else use argument
if len(sys.argv) == 1: msg = sys.stdin.read() # raw_input('Message: ')
else: msg = sys.argv[1]

# domain, use ('gmail.com',debug=[]) for no debug info
client = xmpp.Client('gmail.com')
# server + port (5222 and 443 work)
client.connect(server=('talk.google.com', 443))
# sasl=1 for old servers, resource=optional description
client.auth(user='myUser!', password='myPass!', resource='home', sasl=0)
 
# send message
client.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
client.send(message)
