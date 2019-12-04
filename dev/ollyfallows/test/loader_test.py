import sys
import unittest

if __name__ == "__main__":
    # Setup import from other directory
    sys.path = [sys.path[0]+"/../src/"]+sys.path

from model import loader

class test_loader(unittest.TestCase):

    def test_network_from_string(self):
        pass

    def test_network_from_config(self):
        config = {
            'layers':[
                {"type":"conv", "conv_count":3, "conv_dim":[7,7,3], "conv_edge_handling":"pad-0", "mutable":True, "removable":True},
                {"type":"relu", "mutable":False, "removable":True},
                {"type":"conv", "conv_count":1, "conv_dim":[2,2,3], "conv_step":2, "conv_edge_handling":"ignore", "mutable":False, "removable":False},
                {"type":"relu", "mutable":False, "removable":True},
                {"type":"conv", "conv_count":5, "conv_dim":[7,7,1], "conv_edge_handling":"pad-0", "mutable":True, "removable":True},
                {"type":"relu", "mutable":False, "removable":True},
            ],
            'mutation_rate':0.1
        }
        net = loader.network_from_config(config)
        self.assertEqual(net.layer_count(), 6)

if __name__ == "__main__":
    unittest.main()
