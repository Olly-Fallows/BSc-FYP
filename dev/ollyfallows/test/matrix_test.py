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
        tests = ([[0,0,0],[0,1,0],[0,0,0]], [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
        for a in tests:
            try:
                mat = matrix.matrix(val=a)
            except:
                self.fail("Matrix through an error when given the parameter of "+str(a)+" for __init__")

    def test_matrix_dimensions_init(self):
        tests = ([1,1],[1,1,1],[20,5,4])
        for a in tests:
            try:
                mat = matrix.matrix(dimensions=a)
            except:
                self.fail("Matrix through an error when given the paramerter of "+str(a)+" for __init__")

    def test_matrix_zero_dimensions_init(self):
        tests = ([], [0], [0,0,0])
        failed = False
        for a in tests:
            try:
                mat = matrix.matrix(dimensions=a)
                failed = True
            except:
                pass
            if failed:
                self.fail("Matrix didn't throw an error with parameter "+str(a)+" for __init__")

    def test_matrix_negative_dimensions_init(self):
        tests = ([-5,-5,-5],[5,-5,-5],[5,5,-5])
        failed = False
        for a in tests:
            try:
                mat = matrix.matrix(dimensions=a)
                failed = True
            except:
                pass
            if failed:
                self.fail("Matrix didn't throw an error with parameter "+str(a)+" for __init__")

    def test_matrix_to_string(self):
        tests = ([[0,0,0],[0,1,0],[0,0,0]], [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
        answers = ("[[0, 0, 0], [0, 1, 0], [0, 0, 0]]", "[[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]")
        i=0
        for a in tests:
            mat = matrix.matrix(val=a)
            self.assertEqual(str(mat), answer[i])
            i += 1

        tests = ([1,1],[1,1,1],[3,3,3])
        answers = ("[[1]]", "[[[1]]]", "[[[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1]]]")
        i=0
        for a in tests:
            mat = matrix.matrix(dimensions=a)
            self.assertEqual(str(mat), answer[i])
            i += 1

    def test_matrix_get_dimensions(self):
        tests = ([[0,0,0],[0,1,0],[0,0,0]], [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
        answers = ([3,3], [3,3,3])
        i=0
        for a in tests:
            mat = matrix.matrix(val=a)
            self.assertEqual(mat.dimensions, answer[i])
            i += 1

        tests = ([1,1],[1,1,1],[3,3,3])
        i=0
        for a in tests:
            mat = matrix.matrix(dimensions=a)
            self.assertEqual(mat.dimensions, a)
            i += 1
