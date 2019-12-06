# This file contains a collection of functions used to access different text files.
# Mostly json and csv.

import sys

def load_file(source):
    file = try_open(source, "r")
    if file == None:
        raise
    return file.read()

def try_open(source, mode, i=0):
    try:
        file = open(sys.path[i]+source)
        return file
    except:
        if i >= len(sys.path)-1:
            return None
        else:
            return try_open(source, mode, i+1)

def exists(source):
    pass

def get_folder_content(source):
    pass
