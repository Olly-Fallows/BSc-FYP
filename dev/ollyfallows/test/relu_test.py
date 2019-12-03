import unittest

from model import relu
from model import matrix

class test_relu(unittest.TestCase):

    def test_relu_apply_to_valid_matrix(self):
        rel = relu.relu()
        inMat = matrix.matrix(
            [
                [1,2,0],
                [-1,2,3],
                [-3,0.1,0]
            ]
        )
        expMat = matrix.matrix(
            [
                [1,2,0],
                [0,2,3],
                [0,0.1,0]
            ]
        )
        result = rel.apply(inMat)
        self.assertEqual(expMat, result)
