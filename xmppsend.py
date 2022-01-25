#!/usr/bin/python2.7
# can create google account here https://accounts.google.com/SignUp?continue=http%3A%2F%2Fwww.google.de%2F&hl=de
# pip2.7 install xmpppy dnspython

import xmpp
import sys

# variables
to = 'USER@' ## destination address (gmail and googlemail matters!)
user="USER@DOMAIN.TLD"
pw="PASSWORD"
# whatever is here wont be send - useful if you forward syslog event hint hint ;)
whitelist = "pam_unix(cron:session):,send_ping routine terminated,A long semaphore wait:" # csv

# if no argument given, ask for message, else use argument
if len(sys.argv) == 1:
  msg = sys.stdin.readline() # raw_input('Message: ')
else: msg = sys.argv[1]

try:
  msg = msg.strip("\n") # remove trailing newline
except:
  pass

# check for whitelisted entries
for entry in whitelist.split(","):
  if entry in msg:
    sys.exit() # exit if hit

# jabber magic. login and send
jid=xmpp.protocol.JID(user)
cli=xmpp.Client(jid.getDomain(), debug=[]) # debug=True on errors
cli.connect()
cli.auth(user=jid.getNode(), password=pw, resource='rabbithole', sasl=1)

# send message
cli.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
cli.send(message)
cli.disconnect()
