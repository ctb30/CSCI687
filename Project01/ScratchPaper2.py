
#ScratchPaper2.py
ThisSequence = 'AGGTC'
numChars = len(ThisSequence)
print("numChars: " + str(numChars))
Flag = 0
for i in range (0,numChars):
    ThisChar = ThisSequence[i]
    match ThisChar: 
        case 'A':
            Flag += 0
        case 'C':
            Flag += 0
        case 'G':
            Flag += 0
        case 'T':
            Flag += 0
        case other: 
            Flag += 1 
if Flag > 0 : 
    print("Error")
if Flag == 0 : 
    print("Fill it up")
