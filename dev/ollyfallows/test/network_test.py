import sys
import unittest

if __name__ == "__main__":
    # Setup import from other directory
    sys.path = [sys.path[0]+"/../src/"]+sys.path

class test_network(unittest.TestCase):

    def test_network_to_string(self):
        pass

    def test_network_apply(self):
        pass

if __name__ == "__main__":
    unittest.main()
