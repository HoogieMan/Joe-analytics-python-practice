# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import random
def montyhall(iterations):
    firstpicksuccess = 0    
    switchsuccess = 0   
    for x in range(0,iterations):
        doorlist = [1,2,3]
        picklist = list(doorlist)
        picklist2 = list(doorlist)
        cpick1 = randint(1,4)
        carloc = randint(1,4)        
        if carloc == cpick1:        
            picklist.remove(cpick1)
            revealedD = picklist[randint(0,2)]
            firstpicksuccess +=1
        else:
            picklist.remove(cpick1)
            picklist.remove(carloc)
            revealedD = picklist[0]
        picklist2.remove(cpick1)
        picklist2.remove(revealedD)
        cpick2 = picklist2[0]
        if cpick2 == carloc:
            switchsuccess +=1
    print ("Correct first pick " + str(firstpicksuccess) + " out of " +
        str(iterations) + " times.")    
    print ("Correct switching pick " + str(switchsuccess) + " out of " + 
        str(iterations) + " times.")
    return switchsuccess    