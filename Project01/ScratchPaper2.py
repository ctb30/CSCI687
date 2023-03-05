
#ScratchPaper2.py
ThisSequence = 'AGBGTHH' #CHANGE ME

numChars = len(ThisSequence)
print("numChars: " + str(numChars))
Flag = 0
for i in range (0,numChars):
    ThisChar = ThisSequence[i]
    if ThisChar in ['A','C','G','T']:
        Flag += 0 
    else: 
        print("fail: "+ ThisChar)
        Flag += 1 
if Flag > 0: 
    print("FOOFOO")
else:
    print("Good")