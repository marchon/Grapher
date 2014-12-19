#!/usr/bin/env python


import json
import urllib2
from Database.FAQ import helpme

def GetgroupOSINTinfo(groupid):
    
    jsr = json.loads(urllib2.urlopen("https://graph.facebook.com/" + groupid).read())
    
    try:
        # Group Stuff
        if ('checkins' in jsr):
            raise KeyError

        if ('gender' in jsr):
            raise KeyError

        if ('gender' not in jsr):
            print "\n Group Information:\n"
            
            if ('name' in jsr):
                print "     Group Name:", jsr['name']
            
            if ('id' in jsr):
                print "     Group ID:", jsr['id']

                # Group Owner things
            
            if ('owner' not in jsr):
                pass

            if ('owner' in jsr):
                OwnerStuff = jsr['owner']
           
                if ('name' in OwnerStuff):
                    print "     Owner Name:", OwnerStuff['name']
        
                if ('id' in OwnerStuff):
                    print "     Owner ID:", OwnerStuff['id']
    
            print "\n"
        
    except KeyError:
        print "\n    Looking for page and or user information ?"
        print "    Try the -p or -u option."
