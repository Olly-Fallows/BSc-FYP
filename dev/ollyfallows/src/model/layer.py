import copy

from . import matrix

class layer:

    def __init__(self, content=[], edge_handling=1, step=1, mutable=False, removable=False):
        self.content = content
        self.edge_handling = edge_handling
        self.step = step
        self.mutable = mutable
        self.removable = removable

    def apply(self, val):
        result = []
        for a in self.content:
            result.append(a.apply(val, self.edge_handling, self.step)[0])
        return matrix.matrix(result)

    def filter_count(self):
        return len(self.content)
