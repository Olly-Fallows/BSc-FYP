import sys
import unittest

if __name__ == "__main__":
    # Setup import from other directory
    sys.path = [sys.path[0]+"/../src/"]+sys.path

import model
from neat import population

class test_population(unittest.TestCase):

    def test_generate_population_from_size_and_config(self):
        pass

    def test_load_population_from_folder(self):
        pass

    def test_get_species_count(self):
        pass

if __name__ == "__main__":
    unittest.main()
