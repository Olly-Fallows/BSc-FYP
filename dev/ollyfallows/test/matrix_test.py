import unittest

from model import matrix

class test_matrix(unittest.TestCase):

    def test_matrix_empty_init(self):
        failed = False
        try:
            mat = matrix.matrix()
            failed = True
        except:
            pass
        if failed:
            self.fail("Matrix should fail if not given parameters for __init__")

    def test_matrix_empty_list_init(self):
        for a in ([],[[]],[[[[[]]]]],None):
            failed = False
            try:
                mat = matrix.matrix(val=a)
                failed = True
            except:
                pass
            if failed:
                print(a)
                self.fail("Matrix should fail with parameter '"+str(a)+"' for __init__")

    def test_matrix_not_empty_list_init(self):
        pass

    def test_matrix_dimensions_init(self):
        pass

    def test_matrix_zero_dimensions_init(self):
        pass

    def test_matrix_negative_dimensions_init(self):
        pass

    def test_matrix_to_string(self):
        pass

    def test_matrix_get_dimensions(self):
        pass
