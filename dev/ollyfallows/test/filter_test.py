import sys
import unittest

if __name__ == "__main__":
    # Setup import from other directory
    sys.path = [sys.path[0]+"/../src/"]+sys.path

from model import filter
from model import matrix

class test_filter(unittest.TestCase):

    def test_filter_to_string(self):
        tests = ([[0,0,0],[0,1,0],[0,0,0]], [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
        for a in tests:
            mat = matrix.matrix(val=a)
            flt = filter.filter(mat)
            self.assertEqual(str(flt), str(mat))

    def test_filter_apply(self):
        flt = filter.filter(matrix.matrix(val=
            [
                [[0,0,0],[0,1,0],[0,0,0]],
                [[0,1,0],[1,0,1],[0,1,0]],
                [[0,0,0],[0,1,0],[0,0,0]]
            ]
        ), edge_handle="ignore")
        inMat = matrix.matrix(val=
            [
                [[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,0]],
                [[0,0,1,1,1],[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,0],[1,1,1,0,0]],
                [[0,0,0,1,1],[0,0,1,1,1],[0,1,1,1,0],[1,1,1,0,0],[1,1,0,0,0]]
            ]
        )
        expResult = matrix.matrix(val=
            [[],[],[]]
        )
        result = flt.apply(inMat)
        self.assertEqual(str(expResult), str(result))

if __name__ == "__main__":
    unittest.main()
