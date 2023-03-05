import numpy as np
my100by2 = np.zeros((5,2), dtype=object)

my100by2[3][0] = "RNA"
my100by2[0][0] = "DNA"

TestSequence = "AAAGGG"
my100by2[3][1] = TestSequence

TestSequence2 = "TTAUU"
my100by2[0][1] = TestSequence2

print("my100by2")
print(my100by2)

startA = 3
startB = 1

numCharsA = len(TestSequence) 
numCharsB = len(TestSequence2)

endOfA = ""
endOfB = ""

for i in range(startA,numCharsA):
    endOfA += TestSequence[i]
for j in range(startB,numCharsB):
    endOfB += TestSequence2[j]

print("endOfA : ")
print(endOfA )
print("endOfB: ")
print(endOfB)

TestSequence = TestSequence.replace(endOfA,endOfB)
TestSequence2 = TestSequence2.replace(endOfB, endOfA)

print("Seq1: " + str(TestSequence))
print("Seq1: " + str(TestSequence2))

print("my100by2")
print(my100by2)