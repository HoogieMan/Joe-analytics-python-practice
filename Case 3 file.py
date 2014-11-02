def getDaFile(pathToDocs, doc):
    filenamePath = pathToDocs + '/' + doc
    daFile = open(filenamePath,'r')
    contents = daFile.read()
    daFile.close()
    return contents


import os

def report1(pathToDocs, pathToQueryFile):

    dirList = os.listdir(pathToDocs)
    print dirList

    os.path.split(pathToQueryFile)
    (filepath, queryfname) = os.path.split(pathToQueryFile)
    queryList = getDaFile(pathToDocs, queryfname).split()
    print queryList
    
    myFile = open('output.txt','w')
    myFile.write('File' + ',' + queryfname)
    myFile.write('\n')
    
    for filename in dirList:
        print filename
        fileList = getDaFile(pathToDocs, filename).split()
        #print fileList
        daWordCount = 0
        for word in fileList:
            for item in queryList:
                if word == item:
                    daWordCount = daWordCount + 1
        print daWordCount
        myFile.write(filename + ',' + str(daWordCount))
        myFile.write('\n')
    return dirList


def report2(pathToDocs, pathToQueryFile, lowercase):
    dirList = os.listdir(pathToDocs)
    print dirList

    os.path.split(pathToQueryFile)
    (filepath, queryfname) = os.path.split(pathToQueryFile)
    queryList = getDaFile(pathToDocs, queryfname).split()
    print queryList
    
    myFile = open('output.txt','w')
    myFile.write('File' + ',' + queryfname)
    myFile.write('\n')
    
    for filename in dirList:
        print filename
        fileString = getDaFile(pathToDocs, filename)
        if lowercase == True:
            loweredString = fileString.lower()
            loweredList = loweredString.split()
            #print loweredList
            daWordCount = 0
            for word in loweredList:
                for item in queryList:
                    if word == item:
                        daWordCount = daWordCount + 1
        elif lowercase == "":
            loweredString = fileString.lower()
            loweredList = loweredString.split()
            daWordCount = 0
            for word in loweredList:
                for item in queryList:
                    if word == item:
                        daWordCount = daWordCount + 1
        else:
            fileList = fileString.split()
            daWordCount = 0
            for word in fileList:
                for item in queryList:
                    if word == item:
                        daWordCount = daWordCount + 1
        print daWordCount
        myFile.write(filename + ',' + str(daWordCount))
        myFile.write('\n')
    return dirList
        
#report2(pathToDocs, pathToQueryFile, True)


def report3(pathToDocs, pathToConceptFiles,lowercase):
## part 1 --- list of filenames under pathToDocs##
    dirList = os.listdir(pathToDocs)
    print dirList

## part 2 --- list of filenames in pathToConceptFiles##
    dirConceptList = os.listdir(pathToConceptFiles)
    print dirConceptList
      
## part 3 --- create output file and write headers ##
    myFile = open('output.txt','w')
    myFile.write('File_Name' + ',' + 'File_Length' + ',')
    for queryFileName in dirConceptList:
        myFile.write(queryFileName + ',')
    myFile.write('\n')
    
## part4 --- processing it all##
    queryCounter = 0
    for queryFile in dirConceptList:
        pathToQueryFile = pathToConceptFiles + '/' + queryFile
        (filepath, queryFileName) = os.path.split(pathToQueryFile) 
        wordList = getDaFile(pathToConceptFiles, queryFileName).split()
        print wordList
        fileCounter = 0
        for filename in dirList:
            
            print filename
            fileString = getDaFile(pathToDocs, filename)
            if lowercase == True:
                loweredString = fileString.lower()
                loweredList = loweredString.split()
                #print loweredList
                daWordCount = 0
                for word in loweredList:
                    for item in wordList:
                        if word == item:
                            daWordCount = daWordCount + 1
            elif lowercase == "":
                loweredString = fileString.lower()
                loweredList = loweredString.split()
                daWordCount = 0
                for word in loweredList:
                    for item in wordList:
                        if word == item:
                            daWordCount = daWordCount + 1
            else:
                fileList = fileString.split()
                daWordCount = 0
                for word in fileList:
                    for item in wordList:
                        if word == item:
                            daWordCount = daWordCount + 1
            print daWordCount
            
## part 5 --- writing to output file ##
            if queryCounter == 0:
                myFile.write(filename + ',' + str(len(fileString)) + ',' + str(daWordCount))
                myFile.write('\n')
            elif queryCounter == 1:
                if fileCounter == 0:
                    myFile.close()
                    myFile = open('output.txt','a')
                    myFile.write(','','',' + str(daWordCount))
                else:
                    myFile.write(','','',' + str(daWordCount))
                myFile.write('\n')
            elif queryCounter == 2:
                if fileCounter == 0:
                    myFile.close()
                    myFile = open('output.txt','a')
                    myFile.write(','','','',' + str(daWordCount))
                else:
                    myFile.write(','','','',' + str(daWordCount))
                myFile.write('\n')
            fileCounter = fileCounter + 1        
        queryCounter = queryCounter + 1
#report3(pathToDocs, pathToConceptFiles, True)

