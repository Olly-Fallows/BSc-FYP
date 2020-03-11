# This class is a wrapper to allow a matrix to act as a kernel to be applied to
# other matrixes.
import copy
from util import opengl
from . import matrix

class filter:

    # Constructor
    def __init__(self, mat):
        self.mat = copy.deepcopy(mat)

    # Method to apply the filter
    def apply(self, val, edge_handling=1, step=1):
        # Get the instance of opengl
        gl = opengl.opengl.get_instance()
        # Calculate the output size based on the input size
        y_size = len(val.mat[0])
        x_size = len(val.mat[0][0])
        # If used edge handling case 0, adjust output size by kernel_size-1
        if edge_handling == 0:
            y_size -= (len(self.mat.mat[0])-1)
            x_size -= (len(self.mat.mat[0][0])-1)
        # Reduce output size based on the step of the kernel
        y_size /= step
        x_size /= step
        # Put the output size into a list
        out_size = [1,int(y_size),int(x_size)]
        # Use the opengl apply shader method
        # Use the conv.glsl shader
        # Put in the size for each of the buffers
        # Pass the edge handling case
        # Pass the step size
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
