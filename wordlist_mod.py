#!/usr/bin/python

#Program: wordlist_mod v1.1
#Description: 
#This python script performs a number of selectable actions designed to clean/edit a provided wordlist used in dictionary based password cracking.  
#The input is a wordlist (dictionary) and the output is the modified wordlist based on the user's selected acitons.

#Requried modules
import sys, time, numpy as np, base64, hashlib

#Create variables
user_selection = int
varX = int
varY = int
varZ = int
varStep = int
varPP = 0
varTime = 0

#Take arguments from command line
inputfile = sys.argv[1]
outputfile = sys.argv[2]

#Open the dictionary (input file)
print "\nOpening file, for extremely large files this may take some time.\n"
my_dictionary = list(open(inputfile, 'r'))

print "\nYour file has been opened and contains this many entries:"
print len(my_dictionary)
varStep = input("\nEnter the number of steps to perform (see the README file for info): \n")
print "\nEnter the timing delay.  The recommended time delay between steps is .001 seconds (see the README file for info)."
varTime = input("Enter your desired time delay between steps: \n")
print ""

###START PROGRAM###

#Ask user for action to perform
while user_selection != 17:
  #Reset varPP to 0 from previous loops.
  varPP = 0
  print "Choose one of the following:"
  print "1.  Remove preceding white space from every item (do this first)."
  print "2.  Return only unique entries (delete duplicates) for large (>1Gb) files. Does not preserve original order."
  print "3.  Return only unique entries (delete duplicates) for small (<1Gb) files. Preserves original order."
  print "4.  Sort list alphabetically."
  print "5.  Remove a preceeding character frome every item (remove whitespace first)."
  print "6.  Capitalize only the first letter of every item (remove whitespace first)."
  print "7.  Convert all letters to uppercase for every item."
  print "8.  Convert all letters to lowercase for every item."
  print "9.  Return only items greater than X."
  print "10. Return only items less than X."
  print "11. Return only items between X and Y (inclusive)."
  print "12. Convert entries per line to base64."
  print "13. Decode entries per line from base64."
  print "14. Hash entries per line with md5."
  print "15. Hash entries per line with sha1."
  print "16. Write results to file."
  print "17. Exit. \n"
  user_selection = input("Enter a number: \n")

  #User chose to remove preceeding white space.
  if user_selection == 1:
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          my_dictionary[i2+varPP] = my_dictionary[i2+varPP].strip()
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            my_dictionary[varPP] = my_dictionary[varPP].strip()
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    print "\nDone. \n"

  #User chose to return only unique entries.   
  elif user_selection == 2:
    #Remove duplicates, numpy (np) used for large files.
    my_dictionary = np.unique(my_dictionary)
    print "\nDone. \n"

  #User chose to return only unique entries.
  elif user_selection == 3:
    #create a temp arrary.
    new_dictionary = []
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          if not my_dictionary[i2+varPP] in new_dictionary:
            #If item is not yet in new_dictionary add it. 
            new_dictionary.append(my_dictionary[i2+varPP])
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            if not my_dictionary[varPP] in new_dictionary:
              new_dictionary.append(my_dictionary[varPP])
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    my_dictionary = new_dictionary
    print "\nDone. \n"

  #User chose to sort the list alphabetically.    
  elif user_selection == 4:
    #Sort list (case sensitive)
    my_dictionary = np.sort(a=my_dictionary, kind='mergesort')
    print "\nDone. \n"
  
  #User chose to replace a re-occuring character of each entry.
  elif user_selection == 5:
    print "\nRemove a preceeding character from each string (Ex: '/'' preceeds all entries)."
    print "Note: This option removes all preceeding occurances of the item from every string (Ex: '/' and '////' are both removed).\n"
    varZ = input("What is the character that needs to be replaced? Enter as 'character' (Ex: '/'): \n")
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          my_dictionary[i2+varPP] = my_dictionary[i2+varPP].lstrip(varZ).strip()
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            my_dictionary[varPP] = my_dictionary[varPP].lstrip(varZ).strip()
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    print "\nDone. \n"

  #User chose to capitilize the first letter of each entry.
  elif user_selection == 6:
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          my_dictionary[i2+varPP] = my_dictionary[i2+varPP].capitalize()
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            my_dictionary[varPP] = my_dictionary[varPP].capitalize()
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    print "\nDone. \n"

  #User chose to convert all items to uppercase.
  elif user_selection == 7:
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          my_dictionary[i2+varPP] = my_dictionary[i2+varPP].upper()
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            my_dictionary[varPP] = my_dictionary[varPP].upper()
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    print "\nDone. \n"
  
  #User chose to convert all items to lowercase.
  elif user_selection == 8:
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          my_dictionary[i2+varPP] = my_dictionary[i2+varPP].lower()
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            my_dictionary[varPP] = my_dictionary[varPP].lower()
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    print "\nDone. \n"
  
  #User chose to return only items greater than X.
  elif user_selection == 9:
    print "\nKeep strings >= X"
    varX = input("Enter X: \n")
    #create a temp arrary.
    new_dictionary = []
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          if len(my_dictionary[i2+varPP]) >= varX:
            #If item is not yet in new_dictionary add it. 
            new_dictionary.append(my_dictionary[i2+varPP])
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            if len(my_dictionary[varPP]) >= varX:
              new_dictionary.append(my_dictionary[varPP])
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    my_dictionary = new_dictionary
    print "\nDone. \n"
  
  #User chose to return only items less than X.
  elif user_selection == 10:
    print "\nKeep strings <= X"
    varX = input("Enter X: \n")
    #create a temp arrary.
    new_dictionary = []
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          if len(my_dictionary[i2+varPP]) <= varX:
            #If item is not yet in new_dictionary add it. 
            new_dictionary.append(my_dictionary[i2+varPP])
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            if len(my_dictionary[varPP]) <= varX:
              new_dictionary.append(my_dictionary[varPP])
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    my_dictionary = new_dictionary
    print "\nDone. \n"
  
  #User chose to return only items between X and Y inclusive.
  elif user_selection == 11:
    print "\nKeep strings >= X and <=Y"
    varX = input("Enter X: \n")
    varY = input("Enter Y: \n")
    #create a temp arrary.
    new_dictionary = []
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          if len(my_dictionary[i2+varPP]) >= varX and len(my_dictionary[i2+varPP]) <= varY:
            #If item is not yet in new_dictionary add it. 
            new_dictionary.append(my_dictionary[i2+varPP])
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            if len(my_dictionary[varPP]) >= varX and len(my_dictionary[varPP]) <= varY:
              new_dictionary.append(my_dictionary[varPP])
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    my_dictionary = new_dictionary
    print "\nDone. \n"

  #User chose to convert all items to base64.
  elif user_selection == 12:
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          my_dictionary[i2+varPP] = base64.b64encode(my_dictionary[i2+varPP])
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            my_dictionary[varPP] = base64.b64encode(my_dictionary[varPP])
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    print "\nDone. \n"

  #User chose to decode all items from base64.  Note: strip() will remove preceeding spaces that might have been encoded.
  elif user_selection == 13:
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          my_dictionary[i2+varPP] = base64.b64decode(my_dictionary[i2+varPP]).strip()
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            my_dictionary[varPP] = base64.b64decode(my_dictionary[varPP]).strip()
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    print "\nDone. \n"

  #User chose to hash all items with md5.
  elif user_selection == 14:
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          my_dictionary[i2+varPP] = hashlib.md5(my_dictionary[i2+varPP]).hexdigest()
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            my_dictionary[varPP] = hashlib.md5(my_dictionary[varPP]).hexdigest()
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    print "\nDone. \n"

  #User chose to hash all items with sha1.
  elif user_selection == 15:
    #Outer loop creats groups of size len(array)/varStep.
    for i1 in range(0,len(my_dictionary),varStep):
      #Inner loop prints items from array.
      for i2 in range(varStep):
        #Condition check to prevent out-of-range errors.
        if varPP + varStep <= len(my_dictionary):
          #Print item from array.
          my_dictionary[i2+varPP] = hashlib.sha1(my_dictionary[i2+varPP]).hexdigest()
        #Condition to print any remainders due to division. 
        elif varPP + varStep > len(my_dictionary):
          #Condition to stop printing beyond the array's lenth.
          if varPP == len(my_dictionary):
            #End of array reached, print nothing.
            pass
          #Print the remaining items.
          else:
            my_dictionary[varPP] = hashlib.sha1(my_dictionary[varPP]).hexdigest()
            varPP = varPP + 1
        else:
          print "Nothing"
      #Increment what is being printed.
      varPP = varPP + varStep
      #Pause in seconds.
      time.sleep(varTime)
    print "\nDone. \n"
  
  elif user_selection == 16:
    #Write results to file.
    my_output = open(outputfile, 'w')
    for i1 in my_dictionary:
      my_output.write(('{}'*len(i1)).format(*i1) + '\n')
    my_output.close() 
    print "The file has been saved."
    print "The new length of your wordlist is ",len(my_dictionary)," lines."
    print "\nDone. \n"

  elif user_selection == 17:
    #Exit program.
    print "Exiting. \n"

  else:
    print "\nInvalid selection.  Try again.\n"

###END PROGRAM###
