import json
from . import *
from . import relu
from . import network

# Function to load a network from a string
def network_from_string(text):
    # Convert the string to a json object
    data = json.loads(text)
    # List of layers
    layers = []
    # Iterate through each layer as represented in the json structure
    for a in data:
        # Check if layer is of type conv or relu
        if a['type'] == 'conv':
            # If of type conv then create a list of filters for that layer
            filters = []
            for b in a['filters']:
                filters.append(filter.filter(matrix.matrix(b)))
            # Add layer to the list of layers with relevant information
            layers.append(layer.layer(filters, int(a['edge_handling']), int(a['step']), bool(a['mutable']),
                          bool(a['removable'])))
        elif a['type'] == 'relu':
            # If of type relu initialise a relu layer object
            layers.append(relu.relu())
    # Initialise network object using the layer list
    return network.network(layers)
