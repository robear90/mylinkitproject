#!/usr/bin/python
'''
99% of this code is from 'cardtocloud' by BrettBuilds
https://github.com/bhileman/cardtocloud
Used under GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
'''
import sys
import smtplib
from datetime import datetime
import mraa
import os.path
import logging
import time
import ConfigParser
import os
import socket
import os
from urllib2 import urlopen, URLError, HTTPError


#assign program LED
led = mraa.Gpio(21)

#set GPIO21 to output mode
led.dir(mraa.DIR_OUT)


def CheckConnect():
    print 'checking connection'
    socket.setdefaulttimeout( 23 )
    url = 'http://google.com/'
    try :
        response = urlopen( url )
    except HTTPError:
        led.write(1)
        return 'Disconnected'
    except URLError:
        led.write(1)
        return 'Disconnected'
    else :
        html = response.read()
        responseurl = response.url
        if response.url.startswith('http://www.google'):
            return 'Connected'
        else:
            return 'Disconnected'


   
if __name__ == '__main__':
    # Check for internet connection, auto switch to AP Mode if not connected
    if CheckConnect() == 'Connected':          
        print "connected"
    else:
		print "disconnecting"
        os.system("uci set wireless.sta.disabled=1") #Disable station mode
        time.sleep(1)
        os.system("uci commit") #commit uci changes
        time.sleep(3)
        os.system("wifi") #Restarts wifi interface
		time.sleep(1)
