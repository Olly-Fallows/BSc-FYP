import unittest

class test_layer(unittest.TestCase):

    def test_layer_empty_init(self):
        failed = False
        try:
            mat = matrix.matrix()
            failed = True
        except:
            pass
            if failed:
                self.fail("Layer should fail if not given parameters for __init__")

    def test_layer_empty_dictionary_init(self):
        failed = False
        try:
            mat = matrix.matrix([])
            failed = True
        except:
            pass
        if failed:
            self.fail("Layer should fail if given an empty dictonary for __init__")

    def test_layer_valid_dictionary_init(self):
        tests = ([[0,0,0],[0,1,0],[0,0,0]], [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
        for a in tests:
            try:
                mat = matrix.matrix(val=a)
                flt = filter.filter(mat)
                lyr = layer.layer([flt, flt, flt])
            except:
                self.fail("Filter through an error when given the parameter of "+str(a)+" for __init__")

    def test_layer_apply(self):
        pass
