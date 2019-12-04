import sys
import unittest

if __name__ == "__main__":
    # Setup import from other directory
    sys.path = [sys.path[0]+"/../src/"]+sys.path

class test_selector(unittest.TestCase):

    def test_order_based_on_fitness(self):
        pass

    def test_select_top_50_percent(self):
        pass

    def test_select_randomly_weighted_to_higher_fiteness(self):
        pass

if __name__ == "__main__":
    unittest.main()
