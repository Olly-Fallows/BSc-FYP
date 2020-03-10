from model import *
import random
import copy

max_size = 2

def add_layer(net):
    # Choose layer location
    pos = random.randint(1, len(net.layers)-2)
    # Determind filter dimensions
    size = []
    a = 0
    while isinstance(net.layers[pos-a], relu.relu):
        a += 1
        if a > pos:
            break
    if a > pos:
        size.append(3)
    else:
        size.append(net.layers[pos-a].filter_count())
    a = ((int(random.random()*max_size)+1)*2)+1
    size.append(a)
    size.append(a)
    # Create filters
    filters = []
    for a in range(1):#int(random.random()*10)):
        val = []
        for b in range(size[0]):
            val.append([])
            for c in range(size[1]):
                val[b].append([])
                for d in range(size[2]):
                    val[b][c].append(random.random())
        mat = matrix.matrix(val)
        flt = filter.filter(mat)
        filters.append(copy.deepcopy(flt))
    # Create layer
    lyr = layer.layer(content=filters, mutable=True, removable=True)
    # Add layer to chosen location
    net.layers.insert(pos, lyr)

def add_filter(net, layer):
    # Determind filter dimensions
    if isinstance(net.layers[layer], relu.relu):
        return
    l = net.layers[layer].content
    if len(l) == 0:
        remove_layer(net, layer)
        return
    else:
        pass
    if len(l[0].mat.mat) == 0:
        return
    size = [len(l[0].mat.mat), len(l[0].mat.mat[0]), len(l[0].mat.mat[0][0])]
    # Generate filter
    val = []
    for a in range(size[0]):
        val.append([])
        for b in range(size[1]):
            val[a].append([])
            for c in range(size[2]):
                val[a][b].append(random.random())
    flt = filter.filter(matrix.matrix(val))
    l.append(copy.deepcopy(flt))
    # Adjust next layer depth
    if layer < len(net.layers)-1:
        o=1
        while isinstance(net.layers[layer+o], relu.relu):
            o += 1
            if layer+o >= len(net.layers):
                return
        for a in net.layers[layer+o].content:
            val = []
            if len(a.mat.mat) == 0:
                remove_filter(net, layer+o, net.layers[layer+o].content.index(a))
                continue
            for b in range(len(a.mat.mat[0])):
                val.append([])
                for c in range(len(a.mat.mat[0][0])):
                    val[b].append(random.random()*0.1)
            a.mat.mat.append(copy.deepcopy(val))

def change_filter(net, layer, filter):
    flt = net.layers[layer].content[filter]
    for a in range(len(flt.mat.mat)):
        for b in range(len(flt.mat.mat[a])):
            for c in range(len(flt.mat.mat[a][b])):
                v = flt.mat.mat[a][b][c]+random.random()-0.5
                flt.mat.mat[a][b][c] = v

def remove_layer(net, layer):
    if isinstance(net.layers[layer], relu.relu):
        del net.layers[layer]
        return
    count = len(net.layers[layer].content[0].mat.mat)
    if count == 0:
        return
    del net.layers[layer]
    if layer >= len(net.layers):
        return
    o = 0
    while isinstance(net.layers[layer+o], relu.relu):
        o += 1
        if layer+o >= len(net.layers):
            return
    while len(net.layers[layer+o].content[0].mat.mat) > count:
        for a in net.layers[layer+o].content:
            del a.mat.mat[0]
    if len(net.layers[layer+o].content[0].mat.mat) == 0:
        return
    size = [len(net.layers[layer+o].content[0].mat.mat[0]),len(net.layers[layer+o].content[0].mat.mat[0][0])]
    while len(net.layers[layer+o].content[0].mat.mat) < count:
        for a in net.layers[layer+o].content:
            val = []
            for b in range(size[0]):
                val.append([])
                for c in range(size[1]):
                    val[b].append(random.random()*0.1)
            a.mat.mat.append(copy.deepcopy(val))

def remove_filter(net, layer, filter):
    if isinstance(net.layers[layer], relu.relu):
        return
    # Remove filter
    if len(net.layers[layer].content) == 1:
        remove_layer(net, layer)
        return
    del net.layers[layer].content[filter]
    if layer >= len(net.layers)-1:
        return
    # Adjust next layer depth
    o=1
    while isinstance(net.layers[layer+o], relu.relu):
        o += 1
        if layer+o >= len(net.layers):
            return
    for a in net.layers[layer+o].content:
        if len(a.mat.mat) > filter:
            del a.mat.mat[filter]

def check_empty_filters(net):
    for l in net.layers:
        if not(l.mutable):
            for f in range(len(l.content)):
                if not(isinstance(l.content[f], relu.relu)):
                    if len(f.mat.mat) == 0:
                        del l[f]

def check_empty_layers(net):
    for l in range(len(net.layers)):
        if not(net.layers[l].removable):
            if len(net.layers[l].content) == 0:
                del net.layers[l]

def mutate(net, chance=0.1):
    if chance > 1:
        chance = 0.1
    if chance < 0:
        chance = 0.1
    while chance > random.random():
        # Check for empty filters
        check_empty_filters(net)
        # Check for empty layers
        check_empty_layers(net)
        f = int(random.random()*5)
        if f == 0:
            # Add layer
            add_layer(net)
            pass
        elif f == 1:
            # Add filter
            layer = random.randint(0, len(net.layers)-2)
            if not(isinstance(net.layers[layer], relu.relu)):
                if net.layers[layer].mutable:
                    add_filter(net, layer)
        elif f == 2:
            # Change filter
            layer = random.randint(0, len(net.layers)-1)
            if not(isinstance(net.layers[layer], relu.relu)):
                if net.layers[layer].mutable:
                    filter = random.randint(0, len(net.layers[layer].content)-1)
                    change_filter(net, layer, filter)
                    pass
        elif f == 3:
            # Remove layer
            layer = random.randint(1, len(net.layers)-2)
            if isinstance(net.layers[layer], relu.relu):
                remove_layer(net, layer)
                pass
            if net.layers[layer].removable:
                remove_layer(net, layer)
                pass
        elif f == 4:
            # Remove filter
            layer = random.randint(0, len(net.layers)-2)
            if not(isinstance(net.layers[layer], relu.relu)):
                if net.layers[layer].mutable:
                    if len(net.layers[layer].content) <= 1:
                        if net.layers[layer].removable:
                            remove_layer(net, layer)
                    else:
                        filter = random.randint(0, len(net.layers[layer].content)-1)
                        remove_filter(net, layer, filter)

    # Check for empty filters
    check_empty_filters(net)
    # Check for empty layers
    check_empty_layers(net)
    return net
