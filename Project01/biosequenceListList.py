#biosequence.py 
#Courtney Boyd last updated 28Feb2023
#Advanced Software Dev Project 01 
import sys 
import numpy as np 

def myInsert(Line, my100by2, numSegments):
    
    sequenceArrayPosition = int( Line[1] )
    
    SequenceType = Line[2]
    my100by2[1][sequenceArrayPosition] = SequenceType

    ThisSequence = Line[3]
    match SequenceType:
        case "DNA":
            if 'U' in ThisSequence: 
                print(" Error: Type entered was DNA, Sequence entered was RNA. No change made")
            else: 
                 print("Foooo")
                 my100by2[0][sequenceArrayPosition] = ThisSequence
        case "RNA":
            if 'T' in ThisSequence: 
                     print(" Error: Type entered was RNA, Sequence entered was DNA. No change made")
            else:
                 my100by2[0][sequenceArrayPosition] = ThisSequence

 
    

def myPrint(ThisStringLine):
     print("print made it")

def mySwap(ThisStringLine):
     print("swap made it")

def myTranscribe(ThisStringLine):
     print("Transcribe made it")   

def myRemove(ThisStringLine):
     print("Remove made it")   

def myCopy(ThisStringLine):
     print("Copy made it")   





####################  MAIN ##########################

numTerminalSegments = len(sys.argv)
#print("Num Term Segs: " + str(numTerminalSegments))

if numTerminalSegments == 2: 
    my100by2 = [[],[]]
    my100by2[0] = ["Unused"]*100
    my100by2[1] = ["Unused"]*100
    fileNameIndex = 1

elif numTerminalSegments == 3: 
    userInputArraySize = sys.argv[1]
    print("Array Size: " + str(userInputArraySize))
    userInputArraySize= int(userInputArraySize) 

    my100by2 = [[],[]]
    my100by2[0] = ["Unused"]*userInputArraySize
    my100by2[1] = ["Unused"]*userInputArraySize
    fileNameIndex = 2
CommandList = []

try:
    userInputFile = (str(sys.argv[fileNameIndex]))
    print("File:" +str(userInputFile))
    readIn = open(userInputFile,'r')

except FileNotFoundError:
        print ("Wrong file or wrong file path")

getLines = readIn.readlines()
numLines = len(getLines)
#print("numLines: " + str(numLines))
for k in range(0,numLines):
      SplitLine = str.split(getLines[k])
      CommandList.append(SplitLine)

#print("Command List" + str(CommandList))

for j in range(0,numLines):
    thisLine = CommandList[j]
    
    numSegments =  len(thisLine)
    firstSegment = thisLine[0]
    lineIndex = j
    match firstSegment: 
        case "insert": 
            myInsert(thisLine,my100by2, numSegments)
        case "print":
            myPrint(thisLine)
        case "swap":
              mySwap(thisLine)
        case "transcribe":
            myTranscribe(thisLine)
        case "remove":
            myRemove(thisLine)
        case "copy":
              myCopy(thisLine)
print("myFinal100by2")
print(my100by2)
              


         

      
         
      



