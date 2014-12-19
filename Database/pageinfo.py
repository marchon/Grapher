#!/usr/bin/env python


import json
import urllib2
from Database.FAQ import helpme

def GetpageOSINTinfo(pageid):
    """Gather and Collect basic facebook social graph information on a page."""
    jsr = json.loads(urllib2.urlopen("https://graph.facebook.com/" + pageid).read())
        
    try:
        
        if ('gender' in jsr): # Thwarting off people who don't use it properly
            raise KeyError

        if ('gender' not in jsr):

            print "\n Page Information:\n"

            if ('name' in jsr):
                print "     Page Name:", jsr['name'] 

            if ('id' in jsr):
                print "     Page ID:", jsr['id']
        
            if ('category' in jsr):
                print "     Category:", jsr['category']
        
            if ('founded' in jsr):
                print "     Founded In:", jsr['founded']

            if ('username' in jsr):
                print "     Username:", jsr['username']
            
    except KeyError:
        print "\n    Looking user or group information ?"
        print "    Try the -u or -g option."
