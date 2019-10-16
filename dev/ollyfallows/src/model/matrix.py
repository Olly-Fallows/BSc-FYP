# This is a class to provide a basic wrapper for mult-dimensional arrays,
# it is just here for detecting dimensionallity and error checking of matrixes

class matrix:

    def __init__(val=[], dimensions=None):
        if val == [] and dimensions == None:
            raise
