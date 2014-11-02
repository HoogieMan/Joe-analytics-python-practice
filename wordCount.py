# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:45:26 2014

@author: cjhooger
"""
import re

##accesses the file, prepares it for reading, and removes punctuation##
daFile = "C:\Users\IBM_ADMIN\Documents\Python practice\Text Analytics\evolutionofbeauty.txt"
textfile = open(daFile, "r")
daString = textfile.read()
daList = re.split('\W+',daString)

##zips two lists together to create a dictionary of the full text file##
seq1 = range(0,len(daList))
seq2 = daList
wordDict = dict(zip(seq2, seq1))

##accesses the keywordFile, which has words of interest (WOI) which we'll scan##
keywordFile = "C:\Users\IBM_ADMIN\Documents\Python practice\Text Analytics\keywordList.txt"
textKeywords = open(keywordFile, "r")
keywordString = textKeywords.read()
keywordList = re.split('\W+',keywordString)

#for item in keywordList:
#    #count = 0
#    for word in daList:
#        if item == word.lower():
#            #count+=1
#    #print "The word '" + item + "' occurs " + str(count) + " times."
#            print wordDict[word]
            
#x = -1
#for word in daList:
#    x+=1
#    for item in keywordList:
#        if item == word.lower():
#            print str(daList[x-1]) + " " + str(daList[x]) + " " + str(daList[x+1])

##scans through the text file looking for the WOIs, then
##prints a few words before/after the WOIs to show context           
x = -1
for word in daList:
    x+=1
    for item in keywordList:
        if item == word.lower():
            selection = daList[x-5:x+6]
            print ' '.join(selection)