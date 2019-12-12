# This class is a wrapper to allow a matrix to act as a kernel to be applied to
# other matrixes.
import copy
from util import opengl
from . import matrix

class filter:

    def __init__(self, mat):
        self.mat = copy.deepcopy(mat)

    def apply(self, val, edge_handling=1, step=1):
        gl = opengl.opengl.get_instance()
        y_size = len(val.mat[0])
        x_size = len(val.mat[0][0])
        if edge_handling == 0:
            y_size -= int((len(self.mat.mat[0])-1)/2)
            x_size -= int((len(self.mat.mat[0][0])-1)/2)
        y_size /= step
        x_size /= step
        out_size = [1,int(y_size),int(x_size)]
        return gl.apply_shader(
            "./model/shaders/conv.glsl",
            [
                {
                    "val":val.mat,
                    "size":[len(val.mat),len(val.mat[0]),len(val.mat[0][0])],
                    "name":"IN"
                },{
                    "val":self.mat.mat,
                    "size":[len(self.mat.mat),len(self.mat.mat[0]),len(self.mat.mat[0][0])],
                    "name":"KERNEL"
                }
            ],
            out_size,
            {"EDGE_HANDLING" : edge_handling,
             "STEP 1": "STEP "+str(step)}
        ).tolist()
