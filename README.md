# wordlist_mod v1.0 Help File

# Description:
This python script performs a number of user defined actions which clean/edit a provided wordlist used in dictionary based password cracking.  The input is a wordlist (dictionary) and the output is the modified wordlist based on the user’s selected actions. 

# Why is this program needed?:
Information security practioners and penetration testers generally test authentication systems by attempting to use default or previously compromised credentials.  Many wordlists found on the open Internet contain common passwords or those exposed in seperate breach.  Use of the wordlists provices the tester a means of knowing if weak or previously compromosied passwords are used on the authenticaiton system.  This program is useful for modifying such wordlists to remove duplicate items, unncessary white space, or return only passwords of certain lenths.

This program should only be used to test authentication systems for which you own or have been givnen permission to test.

# Prerequisites:
   Python v2 is needed to execute the script.  The following provides basic directions
   on installing Python on your respective operating system.

   Windows users: As of Windows 8.1 you will need to install Python v2, then dnspython.
   1. Download and install python from https://www.python.org/downloads/ . Note: Choose any version of Python that starts with "2", not "3".
   1. Select all default settings, except for on the 'Customize Python'
   screen click "Add python.exe to Path" and choose "Will be installed to local hard-drive".

   MacOS users: Linux users:  None, both python and the necessary libraries should be natively installed.
		
   Linux users:  None, both python and the necessary libraries should be natively installed.

# Execution instructions  
  Run wordlist_mod from a command prompt or terminal window with:
  
    python wordlist_mod.py inputfile.txt outputfile.txt
    
# Planned Updates:
* Python v3 support.
* Add status indicators for each action's progress.
