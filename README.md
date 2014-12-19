Grapher
=======

Grab basic but effective facebook social graph information on Groups, Users and Pages.

Basic Usage:

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


Developer note:

      The most important information outputed from 'grapher' is the "ID" Section,
      with the "ID" number of an account you can:
                  
                  1. Keep track of your targets accounts on a non-named basis.
                  2. Continuously track your target even if your target changes his or her name (Static ID).
                  3. Leverage this open facebook feature for your OSINT Gathering/Analysis.

Happy hacking!
  
LICENSE AGREEMENT:

Guerrilla Warfare Free License ("GWFL") v. 1.0

1. You're free to modify this software to YOUR liking or leave it as is.

2. This software comes as is, and may or may not receive any additional updates, Contact the developer for more help.

3. The initial download and use of this software constitutes that you adhere and are comply to the writing of this user agreement.

4. The Developer is NOT at ALL under any circumstances responsible for YOUR actions or the actions of any other third part instances that maybe use this software for any illegal or nefarious activities.
