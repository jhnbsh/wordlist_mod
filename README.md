# wordlist_mod v1.0 Help File

# Description:
This python program performs a number of user defined actions that clean/edit a provided wordlist used in dictionary based password cracking.  The input is a wordlist (dictionary) and the output is the modified wordlist based on the user’s selected actions. 

# Why is this program needed?:
Information security practitioners and penetration testers generally test authentication systems by attempting to use default or previously compromised credentials.  Many wordlists found on the open Internet contain common passwords or those exposed in a separate breach.  Use of the wordlists provides the tester a means of knowing if weak or previously compromised passwords are used on the authentication system.  This program is useful for modifying such wordlists to remove duplicate items, unnecessary white space, or return only passwords of certain lengths.  This program has been specifically designed to process extremely large wordlists and has successfully edited a 50Gb file in testing.

# Disclaimer:
This program should only be used to test authentication systems for which you own or have been given permission to test.  Do not use this program to edit wordlists which you intend to use for committing a crime.

# Prerequisites:
   Python v2 is needed to execute the program.  The following provides basic directions
   on installing Python on your respective operating system.

   Windows users: As of Windows 8.1 you will need to install Python v2.
   1. Download and install python from https://www.python.org/downloads/ . Note: Choose any version of Python that starts with "2", not "3".
   1. Select all default settings, except for on the 'Customize Python'
   screen click "Add python.exe to Path" and choose "Will be installed to local hard-drive".

   MacOS users:  None, both python and the necessary libraries should be natively installed.
		
   Linux users:  None, both python and the necessary libraries should be natively installed.

# Execution instructions  
  Run wordlist_mod from a command prompt or terminal window with:
  
    python wordlist_mod.py inputfile.txt outputfile.txt
   
  During initial execution of the program a user will be prompted for two items: steps and timing delay.
  
  The steps value is how many items you wish to process at a time.  For example, process 10 items then wait, or process 10,000 items then wait.  The timing delay value is how long the program should wait between steps.  Depending on the speed of your computer and size of your wordlist you may need to experiment with providing a timing delay to prevent a system lockup (due to exhaustion of system resources).  For small wordlists (<5Gb) it is generally safe to leave the timing delay to 0.
  
# Planned Updates:
* Python v3 support.
* Add status indicators for each action's progress.
