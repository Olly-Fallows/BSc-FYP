# This is a grouping of layers to allow for controlled execution of a network
from . import *

class network:

    def __init__(self, layers=[]):
        self.layers = layers

    # Function to apply all layers onto data
    def apply(self, val):
        step = val
        for a in self.layers:
            step = a.apply(step)
        return step

    def layer_count(self):
        return len(self.layers)

    # A function to convert the network into a printable format
    def __str__(self):
        s = ""
        for a in self.layers:
            if isinstance(a, layer.layer):
                for b in a.content:
                    s += str(b.mat.mat)+"\n"
            else:
                s += "Relu\n"
            s += "====================\n"
        return s

    # Function to convert the network into a json format for saving
    def json(self):
        first = True
        s = "["
        for l in self.layers:
            if not(first):
                s += ","
            first = False
            if isinstance(l, relu.relu):
                pass
            else:
                s += "{"
                s += "\"type\":\"conv\","
                s += "\"edge_handling\":"+str(l.edge_handling)+","
                s += "\"step\":\""+str(l.step)+"\","
                s += "\"mutable\":\""+str(l.mutable)+"\","
                s += "\"removable\":\""+str(l.removable)+"\","
                s += "\"filters\":["
                first1 = True
                for a in l.content:
                    if not(first1):
                        s += ","
                    first1 = False
                    s += str(a.mat.mat)
                s += "]"
                s += "}"
        s += "]"
        return s
