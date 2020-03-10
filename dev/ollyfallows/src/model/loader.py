import json
from . import *
from . import relu
from . import network

def network_from_string(text):
    data = json.loads(text)
    layers = []
    for a in data:
        if a['type'] == 'conv':
            filters = []
            for b in a['filters']:
                filters.append(filter.filter(matrix.matrix(b)))
            layers.append(layer.layer(filters, int(a['edge_handling']), int(a['step']), bool(a['mutable']),
                          bool(a['removable'])))
        elif a['type'] == 'relu':
            layers.append(relu.relu())
    return network.network(layers)

def network_from_config(config):
    pass
