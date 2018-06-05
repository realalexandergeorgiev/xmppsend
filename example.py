#!/usr/bin/python
# example that send you a message if your WAN IP changes (also triggers on reboot, because /tmp will be free'd. use a different path if you dont like it)
import urllib 
import subprocess

useragent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
ipfile = "/tmp/last_ip.txt"

def getSite(s): 
    opener = urllib.FancyURLopener() 
    opener.addheader('User-agent', useragent) 
    return opener.open(s).read() 

def currentWANIP(): 
    return getSite('http://www.the-i.de/').split("24px;\">")[1].split("<")[0] 

def saveWANIP(ip, f):
    f=open(f,'w')
    f.write(ip)
    f.close();

def getLastWANIP(f):
    try:
        f=open(f,'r')
        ip=f.read()
        f.close()
        return ip
    except:
        return "foobar"


if __name__ == '__main__': 
    lastip=getLastWANIP(ipfile)
    print "Last IP "+str(getLastWANIP(ipfile))
    ip=str(currentWANIP().strip())
    print "Current IP "+ip
    saveWANIP(ip, ipfile)

    if ip != lastip:
	print "Different"
	subprocess.call(['xmppsend.py', 'New IP '+str(ip)])
    else:
	print "Equal"
