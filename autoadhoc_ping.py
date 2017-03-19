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
import socket
import os
from urllib2 import urlopen, URLError, HTTPError

#assign program LED
#led = mraa.Gpio(21)

#set GPIO21 to output mode
#led.dir(mraa.DIR_OUT)


def CheckConnect():
    print 'checking connection'
    hostname = os.popen("route -n | grep 'UG[ \t]' | awk '{print $2}'").read()
    print "%s" %hostname
    if not hostname:               #If the IP parse comes back empty
        print "No IP, Network Error"
        pingstatus = "Network Error"
        return pingstatus

    response = os.system("ping -n 2 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"s

    return pingstatus

if __name__ == '__main__':
    # Check for internet connection, auto switch to AP Mode if not connected
    os.system("wifi_mode sta") #Restarts wifi interface
    time.sleep(25)
    if CheckConnect() == 'Network Active':
        print "connected"
    else:
        print "No access to known networks - disconnecting"
        time.sleep(3)
        os.system("wifi_mode ap") #Restarts wifi interface
