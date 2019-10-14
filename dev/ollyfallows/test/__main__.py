import unittest
import sys

if __name__ == "__main__":

    # Setup import from other directory
    sys.path = [sys.path[0]+"../src/"]+sys.path

    # Import all tests from files
    from file_test import test_file
    from filter_test import test_filter
    from matrix_test import test_matrix
    from image_test import test_image
    from layer_test import test_layer
    from mutator_test import test_mutator
    from network_test import test_network
    from population_test import test_population
    from selector_test import test_selector

    unittest.main()
