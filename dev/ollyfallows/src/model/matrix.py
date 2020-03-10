# This is a class to provide a basic wrapper for mult-dimensional arrays,
# it is just here for detecting dimensionallity and error checking of matrixes
# Matrix coords are done zyx not xyz, this is an arbitery decision
import copy

class matrix:

    # Constructor
    def __init__(self, val=[], dimensions=None):
        # Check that a either of the parameters have been filled
        if (val == [] or val == None) and (dimensions == None or dimensions == []):
            raise
        # Check if the values have been provided
        if dimensions == None:
            self.mat = copy.deepcopy(val)
        # Generate a matrix of requested size
        else:
            if len(dimensions) == 3:
                if dimensions[0] == 0 or dimensions[1] == 0 or dimensions[2] == 0:
                    raise
                self.mat = []
                for a in range(dimensions[2]):
                    self.mat.append([])
                    for b in range(dimensions[1]):
                        self.mat[a].append([])
                        for c in range(dimensions[0]):
                            self.mat[a][b].append(0)
            elif len(dimensions) == 2:
                if dimensions[0] == 0 or dimensions[1] == 0:
                    raise
                self.mat = []
                for a in range(dimensions[1]):
                    self.mat.append([])
                    for b in range(dimensions[0]):
                            self.mat[a].append(0)
            elif len(dimensions) == 1:
                if dimensions[0] == 0:
                    raise
                self.mat = []
                for a in range(dimensions[0]):
                    self.mat.append(0)
