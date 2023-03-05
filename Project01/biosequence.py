#biosequence.py 
#Courtney Boyd last updated 05Mar2023
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
         print("Error in line " + str(lineIndex) + "(indexing begins at zero) of input file") 
         print("No Sequence at Position " + str(sequenceArrayPosition) + " to remove" ) 
    else:
        my100by2[sequenceArrayPosition][1] = 0
        my100by2[sequenceArrayPosition][0] = 0

def myCopy(Line,my100by2,lineIndex):
    PositionA = int( Line[1] )
    PositionB = int( Line[2] )
    if my100by2[PositionA][0] == 0 :
        print("Error in line " + str(lineIndex) + "(indexing begins at zero) of input file") 
        print("No Sequence at Position " + str(PositionA) + " to copy" ) 
    else: 
        my100by2[PositionB][0] = my100by2[PositionA][0]
        my100by2[PositionB][1] = my100by2[PositionA][1] 

def myPrint(Line,my100by2,lineIndex,numLines,myArraySize):
    numSegments = len(Line)
    if numSegments >= 2 : 
        ArrPosition = int(Line[1]) 
        if my100by2[ArrPosition][0] == 0 :
            print("Error in line " + str(lineIndex) + "(indexing begins at zero) of input file") 
            print("No Sequence at Position " + str(ArrPosition) + " to print" )
        else:
            print("Position: " + str(ArrPosition) + " Type: " + str(my100by2[ArrPosition][0]) + " Sequence: " + str(my100by2[ArrPosition][1])  )
    else: 
         print("***** New Print *******")
         for i in range(0,myArraySize): 
            if my100by2[i][0] == 0 :
                pass
            else: 
                print("index#"+ str(i) +" "+ str(my100by2[i][0]) +" " + str(my100by2[i][1]))
         print("***** End ********")

def mySwap(Line,my100by2,lineIndex):
    PosA = int( Line[1] )
    PosAStart = int( Line[2] )
    print("Pos A: " + str(PosA))

    PosB = int (Line[3])
    PosBStart = int (Line[4])
    print("Pos B: " + str(PosB))

    SequenceA = my100by2[PosA][1]
    print("SeqA: " + str(SequenceA))
    SequenceB = my100by2[PosB][1]
    print("SeqB: " + str(SequenceB))

    numCharsA = len(SequenceA) 
    print("NumcharsA:" + str(numCharsA))
    numCharsB = len(SequenceB)
    print("NumcharsB:" + str(numCharsB))

    endOfA = ""
    endOfB = ""

    for i in range(PosAStart,numCharsA):
        endOfA += SequenceA[i]
    for j in range(PosBStart,numCharsB):
        endOfB += SequenceB[j]

    print("endOfA : ")
    print(endOfA )
    print("endOfB: ")
    print(endOfB)

    SequenceA = SequenceA.replace(endOfA,endOfB)
    my100by2[PosA][1] = SequenceA 
    SequenceB = SequenceB.replace(endOfB, endOfA)
    my100by2[PosB][1] = SequenceB


def myTranscribe(ThisStringLine):
     print("Transcribe made it")   


####################  MAIN ##########################
numTerminalSegments = len(sys.argv)

if numTerminalSegments == 2: 
    my100by2 = np.zeros((100,2), dtype=object)
    myArraySize = 100
    fileNameIndex = 1

elif numTerminalSegments == 3: 
    
    userInputArraySize = sys.argv[1]
    myArraySize= int(userInputArraySize) 
    my100by2 = np.zeros((myArraySize,2), dtype=object)
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
    firstSegment = thisLine[0]
    lineIndex = j
    match firstSegment: 
        case "insert": 
            myInsert(thisLine,my100by2,lineIndex)
        case "remove":
            myRemove(thisLine,my100by2,lineIndex)
        case "copy":
              myCopy(thisLine,my100by2,lineIndex)
        case "print":
            myPrint(thisLine,my100by2,lineIndex,numLines,myArraySize)
        case "swap":
              mySwap(thisLine,my100by2,lineIndex)
        case "transcribe":
            myTranscribe(thisLine)