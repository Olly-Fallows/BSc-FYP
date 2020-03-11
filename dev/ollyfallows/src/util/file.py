# This file contains a collection of functions used to access different text files.
# Mostly json and csv.

import sys

# Function for loading a file from an unknown root directory
def load_file(source):
    # Open file in read format
    file = try_open(source, "r")
    # Check a file was opened
    if file == None:
        raise
    # Read data from the file
    s = file.read()
    # Close the file
    file.close()
    # Return read data
    return s

# Function for writing to a file2
def write_file(source, data):
    # Open the file in write mode
    f = open(source, "w")
    # Check a file was opened
    if f == None:
        raise
    # Write the data
    f.write(data)
    #Close the file
    f.close()

# Recursive function for open a file from an unknown root directory
def try_open(source, mode, i=0):
    # Try statement to catch if the wrong root is used
    try:
        # Try to open the file with root within the path at index i
        file = open(sys.path[i]+source)
        # If successful return the opened file
        return file
    except:
        # If all path elements have been tried return an error
        if i >= len(sys.path)-1:
            t, v, tb = sys.exc_info()
            raise v
        # If not all path elements have been tried, try opening with file with
        # i++ element
        else:
            return try_open(source, mode, i+1)
