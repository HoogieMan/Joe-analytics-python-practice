pathToDocs = 'C:/Users/Christian/Documents/College schoolwork/Senior/Spring 2011/OPIM 311/Case3'
doc = 'eBayUNGCRr4final.txt'
    
def getDaFile(pathToDocs, doc):
    filename = pathToDocs + '/' + doc
    
    getDaFile = open(filename,'r')
    lines = getDaFile.readlines()
    for line in lines:
        print(line.strip())
    getDaFile.close()  

getDaFile(pathToDocs, doc)
