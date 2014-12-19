#!/usr/bin/env python

def HelpINFO():
    print """    
    Basic Usage:

        ./grapher -u <username OR user ID number>
        
        ./grapher -p <page name OR page ID number>

        ./grapher -g <group ID number>

    -h      | Shows this helpful message.
    
    -g      | Get Basic Group information.
    
    -u      | Get basic User information.
    
    -p      | Get basic Page information.
    
    -------------------------------------------------------------
    Or Chain the options together for multiple streams of output.
    -------------------------------------------------------------
    
    Basic Usage of Chained Options:

    ./grapher.py -p google -u 4 -g 175153045875891

     Page Information:
     
          Page Name: Google
          Page ID: 104958162837
          Category: Website
          Founded In: 1998
          Username: Google
     
     User Profile Information:

          First Name: Mark
          Last Name: Zuckerberg
          Gender: male
          ID: 4
          Location: en_US
          Username: zuck

     Group Information:

          Group Name: Hack3rCon
          Group ID: 175153045875891
          Owner Name: Bill Gardner
          Owner ID: 531292655
    """
