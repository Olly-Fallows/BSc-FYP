# This is a grouping of layers to allow for controlled execution of a network

class network:

    def __init__(self, layers=[]):
        self.layers = layers

    def apply(self, val):
        step = val
        for a in self.layers:
            step = a.apply(step)
            print(step.mat)
            print()
        return step

    def layer_count(self):
        return len(self.layers)
