import unittest

from model import filter
from model import matrix

class test_filter(unittest.TestCase):

    def test_filter_empty_init(self):
        failed = False
        try:
            flt = filter.filter()
            failed = True
        except:
            pass
        if failed:
            self.fail("Filter should fail if not given parameters for __init__")

    def test_filter_not_none_matrix_init(self):
        tests = ([[0,0,0],[0,1,0],[0,0,0]], [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
        for a in tests:
            try:
                mat = matrix.matrix(val=a)
                flt = filter.filter(mat)
            except:
                self.fail("Filter through an error when given the parameter of "+str(a)+" for __init__")

    def test_filter_to_string(self):
        tests = ([[0,0,0],[0,1,0],[0,0,0]], [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
        for a in tests:
            mat = matrix.matrix(val=a)
            flt = filter.filter(mat)
            self.assertEqual(str(flt), str(mat))

    def test_filter_apply_to_valid_matrix(self):
        pass

    def test_filter_apply_to_invalid_matrix(self):
        pass
