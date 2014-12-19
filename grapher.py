#!/usr/bin/env python

import getopt
import sys

from Database import pageinfo
from Database import userinfo
from Database import groupinfo
from Database.FAQ import helpme

"""
For this who just need to see the code:

Note a few things are assumed by me 

# You have an internet connection
# Your ISP, Admin or other internet authority figure allow you to visit facebook related websites.
"""

# Take Facebook Graph Information and Convert it into useable Intelligence.

def USERoptions(a):

    try:
        option, args = getopt.getopt(sys.argv[1:],'-h -g: -u: -p:')
    except getopt.GetoptError as ue:
        print "\n"
        print "    ERROR: %s." % ue
        helpme.HelpINFO()

    try:
        for opt, arg in option:
            
            if opt in ('-h'):
                HelpINFO()

            if opt in ('-g'):
                try:
                    groupinfo.GetgroupOSINTinfo(arg)
                except urllib2.URLError:
                    print "404: Group ID not found."

            if opt in ('-u'):
                try:
                    userinfo.GetuserOSINTinfo(arg)
                except urllib2.URLError:
                    print "404: User not found."
    
            if opt in ('-p'):
                try:
                    pageinfo.GetpageOSINTinfo(arg)
                except urllib2.URLError:
                    print "404: Page not found."

    except UnboundLocalError:
        pass

if __name__ == "__main__":
    try:
        USERoptions(sys.argv[1])
    except IndexError:
        helpme.HelpINFO()
