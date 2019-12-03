import unittest

from neat import mutator
import model

class test_mutator(unittest.TestCase):

    def test_add_layer(self):
        net1 = generate_basic_network()
        net2 = mutator.add_layer(net1)
        self.assertEqual(net2.layer_count(), net1.layer_count()+1)

    def test_add_filter(self):
        net1 = generate_basic_network()
        net2 = mutator.add_filter(net1, 0)
        self.assertEqual(net2.layers[0].filter_count(), net1.layers[0].filter_count()+1)

    def test_change_filter(self):
        net1 = generate_basic_network()
        net2 = mutator.change_filter(net1, 0, 0)
        self.assertNotEqual(str(net1.layers[0].content[0]), str(net2.layers[0].content[0]))

    def test_remove_layer(self):
        net1 = generate_basic_network()
        net2 = mutator.remove_layer(net, 0)
        self.assertEqual(net1.layer_count(), net2.layer_count()+1)

    def test_remove_filter(self):
        net1 = generate_basic_network()
        net2 = mutator.remove_filter(net, 0, 0)
        self.assertEqual(net1.layers[0].filter_count(), net2.layers[0].filter_count()+1)

    def test_mutate_inmutable_layer(self):
        net1 = generate_basic_network()
        failed = False
        try:
            net2 = mutator.add_filter(net1, 2)
            failed = True
        except:
            pass
        if failed:
            self.fail("Shouldn't be able to add filter to inmutable layer")
        failed = False
        try:
            net2 = mutator.change_filter(net1, 2, 0)
            failed = True
        except:
            pass
        if failed:
            self.fail("Shouldn't be able to change filter in inmutable layer")
        failed = False
        try:
            net2 = mutator.remove_filter(net1, 2, 0)
            failed = True
        except:
            pass
        if failed:
            self.fail("Shouldn't be able to remove filter from inmutable layer")


    def test_remove_unremovable_layer(self):
        net1 = generate_basic_network()
        failed = False
        try:
            net2 = mutator.remove_layer(net1, 2)
            failed = True
        except:
            pass
        if failed:
            self.fail("Shouldn't be able to remove unremovable layer")

def generate_basic_network():
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
    return net
