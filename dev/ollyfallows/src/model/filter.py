# This class is a wrapper to allow a matrix to act as a kernel to be applied to
# other matrixes.
import copy
from . import matrix

class filter:

    def __init__(self, mat):
        self.mat = copy.deepcopy(mat)

    def apply(self, val):
        pass
