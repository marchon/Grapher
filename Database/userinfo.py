#!/usr/bin/env python


import json
import urllib2
from Database.FAQ import helpme

def GetuserOSINTinfo(userid):
    """Gather and Collect basic facebook social graph information on a user."""
    
    jsr = json.loads(urllib2.urlopen("https://graph.facebook.com/" + userid).read())
    
    try:
            
        if ('owner' in jsr):
            raise KeyError

        if ('checkins' in jsr):
            raise KeyError

        if ('category' in jsr):
            raise KeyError
        
        if ('category' not in jsr):
            
            print "\n User Profile Information:\n" # Denotes what information you're looking at.
            
            if ('first_name' in jsr):
                print "     First Name:", jsr['first_name']
            
            if ('middle_name' in jsr):
                print "     Middle Name:", jsr['middle_name']

            if ('last_name' in jsr):
                print "     Last Name:", jsr['last_name']
        
            if ('gender' in jsr):
                print "     Gender", jsr['gender']
        
            if ('id' in jsr):
                print "     ID:", jsr['id']
        
            if ('locale' in jsr):
                print "     Location:", jsr['locale']
        
            if ('username' in jsr):
                print "     Username:", jsr['username']
    
            print "\n"

    except KeyError:
        print "\n    Looking for page or group information ?"
        print "    Try the -p or -g option."
