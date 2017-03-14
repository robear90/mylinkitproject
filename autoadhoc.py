#!/usr/bin/python
'''
Code is based off of 'cardtocloud' by BrettBuilds
https://github.com/bhileman/cardtocloud
Used under GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
'''
import sys
import smtplib
from datetime import datetime
#import mraa
import os.path
import logging
import time
import ConfigParser
import os
import socket
import os
from urllib2 import urlopen, URLError, HTTPError

#assign program LED
#led = mraa.Gpio(21)

#set GPIO21 to output mode
#led.dir(mraa.DIR_OUT)


def CheckConnect():
    print 'checking connection'
    socket.setdefaulttimeout( 23 )
    url = 'http://google.com/'
    try :
        response = urlopen( url )
    except HTTPError:
     #   led.write(1)
        return 'Disconnected'
    except URLError:
     #   led.write(1)
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
    os.system("wifi_mode sta") #Restarts wifi interface
    time.sleep(25)
    if CheckConnect() == 'Connected':
        print "connected"
    else:
        print "No access to known routers - disconnecting!"
        time.sleep(3)
        os.system("wifi_mode ap") #Restarts wifi interface
