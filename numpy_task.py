"""
Compulsory Task 1
"""

"""
np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float) 
- uses incorrect syntax with () instead of [[]] to make 
two-dimensional array and the dtype=float argument 
should be oustside the provided array arguments
"""

# Import the NumPy library.
import numpy as np

# Creates 2D array with all elements stored as floating-point numbers.
array = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)

# Displays the array.
print("\n", array)

"""
a = np.array([0, 0, 0]) -  Creates a one-dimensional 
array which contains three elements in a single row. 
a = np.array([[0, 0, 0]]) - Creates a two-dimensional 
array which contains one row and three columns.
"""

# Creates 1D array.
a = np.array([0, 0, 0])

# Displays the array.
print("\n", a)

# Creates 2D array.
a = np.array([[0, 0, 0]])

# Displays the array.
print("\n", a)

# Creates a 3x4x4 array with values 1 - 48.
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)

# Displays the array.
print("\nArray:\n\n", arr)

# Extract the value 20.0.
value = arr[1, 0, 3]

# Displays the extracted value.
print("\nExtracted value:", value)

# Extract all columns in 3rd row of 1st block.
column_array = arr[0, 2, :]

# Displays the extracted columns.
print("\nExtracted columns:", column_array)

# Extract all columns and all rows in the third block.
block_array = arr[2, :, :]

# Displays the extracted block.
print("\nExtracted block:\n", block_array)

# Extract values from first two columns of second row on all blocks.
values_array = arr[:, 1, 0:2]

# Displays the extracted values.
print("\nExtracted values:\n", values_array)

# Extract and reverse last two columns of all rows in the thrid block.
reverse_array = arr[2, :, -1:1:-1]

# Displays the extracted and reversed columns.
print("\nExtracted reverse columns:\n", reverse_array)

# Extract and reverse 1st column of all blocks.
column1_array = arr[:, ::-1, 0]

# Displays the extracted and reversed 1st columns.
print("\nExtracted 1st reverse columns:\n", column1_array)

# Extract 1st & 4th column, of 1st row, 1st block & 4th row, 3rd block.
slice_array = arr[[0,2], [0, 3], 0::3]

# Displays the extracted columns.
print("\nExtracted 1st and last columns:\n", slice_array)

# Extract 3rd & 4th rows in 2nd block; & 1st & 2nd rows in 3rd block.
row_array = arr[[1, 1, 2, 2], [2, 3, 0, 1]]

# Displays the extracted rows.
print("\nExtracted rows:\n", row_array)
