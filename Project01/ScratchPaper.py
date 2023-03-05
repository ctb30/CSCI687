import numpy as np
my100by2 = np.zeros((5,2), dtype=object)

my100by2[3][0] = "RNA"
my100by2[0][0] = "DNA"

TestSequence = "AAGGCCUU"
my100by2[3][1] = TestSequence


print("my100by2")
print(my100by2)