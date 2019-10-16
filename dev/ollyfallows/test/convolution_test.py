import unittest

from model import convolution

class test_convolution(unittest.TestCase):

    def test_filter_empty_init(self):
        failed = False
        try:
            conv = convolution.convolution()
            failed = True
        except:
            pass
        if failed:
            self.fail("Filter should fail if not given parameters for __init__")

    def test_convolution_not_none_filters_init(self):
        tests = ([[0,0,0],[0,1,0],[0,0,0]], [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
        for a in tests:
            try:
                mat = matrix.matrix(val=a)
                flt = filter.filter(mat)
                conv = convolution.convolution([flt])
            except:
                self.fail("Convolution through an error when given the parameter of "+str(a)+" for __init__")

    def test_filter_to_string(self):
        tests = ([[0,0,0],[0,1,0],[0,0,0]], [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
        for a in tests:
            mat = matrix.matrix(val=a)
            flt = filter.filter(mat)
            conv = convolution.convolution([flt])
            self.assertEqual(str(conv), "["+str(flt)+"]")
        flt1 = filter.filter(matrix.matrix(tests[0]))
        flt2 = filter.filter(matrix.matrix(tests[1]))
        conv = convolution.convolution([flt1, flt2])
        self.assertEqual(str(conv), "["+str(flt1)+", "+str(flt2)+"]")

    def test_convolution_apply_to_valid_matrix(self):
        pass

    def test_convolution_apply_to_invalid_matrix(self):
        pass
