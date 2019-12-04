import sys
import unittest

if __name__ == "__main__":
    # Setup import from other directory
    sys.path = [sys.path[0]+"/../src/"]+sys.path

from model import layer
from model import filter

class test_layer(unittest.TestCase):

    def test_layer_apply_valid_matrix(self):
        flt = filter.filter(matrix.matrix(val=
            [
                [[0,0,0],[0,1,0],[0,0,0]],
                [[0,1,0],[1,0,1],[0,1,0]],
                [[0,0,0],[0,1,0],[0,0,0]]
            ]
        ), edge_handle="ignore")
        lyr = layer.layer([flt])
        inMat = matrix.matrix(val=
            [
                [[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,0]],
                [[0,0,1,1,1],[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,0],[1,1,1,0,0]],
                [[0,0,0,1,1],[0,0,1,1,1],[0,1,1,1,0],[1,1,1,0,0],[1,1,0,0,0]]
            ]
        )
        expResult = matrix.matrix(val=
            [
                [[],[],[]]
            ]
        )
        result = lyr.apply(inMat)
        self.assertEqual(str(expResult), str(result))

if __name__ == "__main__":
    unittest.main()
