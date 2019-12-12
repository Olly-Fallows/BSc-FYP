# This is a layer that allows the relu activation function to be applied to the
# matrix that is currently going through the network
from util import opengl
from . import matrix

class relu:

    def __init__(self):
        pass

    def apply(self, val):
        gl = opengl.opengl.get_instance()
        y_size = len(val.mat[0])
        x_size = len(val.mat[0][0])
        out_size = [len(val.mat),int(y_size),int(x_size)]
        return matrix.matrix(gl.apply_shader(
            "./model/shaders/relu.glsl",
            [
                {
                    "val":val.mat,
                    "size":[len(val.mat),len(val.mat[0]),len(val.mat[0][0])],
                    "name":"IN"
                }
            ],
            out_size,
            {}
        ).tolist())
