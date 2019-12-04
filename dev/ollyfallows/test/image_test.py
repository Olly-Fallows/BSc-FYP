import sys
import unittest

if __name__ == "__main__":
    # Setup import from other directory
    sys.path = [sys.path[0]+"/../src/"]+sys.path

class test_image(unittest.TestCase):

    def test_image_to_matrix(self):
        pass

    def test_matrix_to_image(self):
        pass

if __name__ == "__main__":
    unittest.main()
