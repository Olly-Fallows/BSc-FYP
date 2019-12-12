from util import *
from model import *

if __name__ == "__main__":
    net = loader.network_from_string(file.load_file("../test/test-files/test.net"))
    data = matrix.matrix([
        [[1,1,1,1,1,1,1],
         [0,1,1,0,1,1,1],
         [0,1,0,0,0,0,0],
         [0,1,1,0,1,1,1],
         [0,1,0,0,0,0,0],
         [0,1,1,0,1,1,1],
         [0,1,0,1,0,0,0]]
    ])
    net.apply(data).mat
