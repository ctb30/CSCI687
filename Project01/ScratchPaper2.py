import numpy as np

# Create a NumPy array of zeros with shape (2, 2)
my_array = np.zeros((2, 2), dtype=object)

# Create a pointer to a string
my_pointer = "Brick"

# Save the pointer in the array at position (1, 0)
my_array[1, 0] = my_pointer

# Print the contents of the array
print(my_array)