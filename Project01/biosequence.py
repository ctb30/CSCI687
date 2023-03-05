#biosequence.py 
#Courtney Boyd last updated 28Feb2023
#Advanced Software Dev Project 01 
import sys 
import numpy as np 

def myInsert(Line, my100by2,lineIndex):
    
    sequenceArrayPosition = int( Line[1] )
    SequenceType = Line[2]
    ThisSequence = Line[3]
    match SequenceType:
        case "DNA":
                numChars = len(ThisSequence)
                Flag = 0
                for i in range (0,numChars):
                    ThisChar = ThisSequence[i]
                    if ThisChar in ['A','C','G','T']:
                        Flag += 0 
                    else: 
                        Flag += 1 
                if Flag > 0: 
                    print("Error in line " + str(lineIndex) + "(indexing begins at zero) of input file") 
                    print("in Sequence or label")
                else:
                    my100by2[sequenceArrayPosition][1] = ThisSequence
                    my100by2[sequenceArrayPosition][0] = SequenceType
        case "RNA":
                numChars = len(ThisSequence)
                Flag = 0
                for i in range (0,numChars):
                    ThisChar = ThisSequence[i]
                    if ThisChar in ['A','C','G','U']:
                        Flag += 0 
                    else: 
                        Flag += 1 
                if Flag > 0: 
                    print("Error in line " + str(lineIndex) + "(indexing begins at zero) of input file") 
                else:
                    my100by2[sequenceArrayPosition][1] = ThisSequence
                    my100by2[sequenceArrayPosition][0] = SequenceType
        case other: 
              print("Error in line " + str(lineIndex) + "(indexing begins at zero) of input file") 
              print("in type label")

def myRemove(Line,my100by2,lineIndex):
    sequenceArrayPosition = int( Line[1] )
    if my100by2[sequenceArrayPosition][0] == 0 : 
         print("No Sequence at Position " + str(sequenceArrayPosition) + " to remove" ) 
    else:
        my100by2[sequenceArrayPosition][1] = 0
        my100by2[sequenceArrayPosition][0] = 0


def myPrint(ThisStringLine):
     print("print made it")

def mySwap(ThisStringLine):
     print("swap made it")

def myTranscribe(ThisStringLine):
     print("Transcribe made it")   



def myCopy(ThisStringLine):
     print("Copy made it")   





####################  MAIN ##########################

numTerminalSegments = len(sys.argv)

if numTerminalSegments == 2: 
    my100by2 = np.zeros((100,2), dtype=object)
    fileNameIndex = 1

elif numTerminalSegments == 3: 
    
    userInputArraySize = sys.argv[1]
    userInputArraySize= int(userInputArraySize) 
    my100by2 = np.zeros((userInputArraySize,2), dtype=object)
    fileNameIndex = 2

CommandList = []

try:
    userInputFile = (str(sys.argv[fileNameIndex]))
    readIn = open(userInputFile,'r')

except FileNotFoundError:
        print ("Wrong file or wrong file path")

getLines = readIn.readlines()
numLines = len(getLines)

for k in range(0,numLines):
      SplitLine = str.split(getLines[k])
      CommandList.append(SplitLine)


for j in range(0,numLines):
    thisLine = CommandList[j]
    
    numSegments =  len(thisLine)
    firstSegment = thisLine[0]
    lineIndex = j
    match firstSegment: 
        case "insert": 
            myInsert(thisLine,my100by2,lineIndex)
        case "remove":
            myRemove(thisLine,my100by2,lineIndex)
        case "print":
            myPrint(thisLine)
        case "swap":
              mySwap(thisLine)
        case "transcribe":
            myTranscribe(thisLine)
        case "copy":
              myCopy(thisLine)

print("TESTING PURPOSES: ")
print(my100by2)
              


         

      
         
      



