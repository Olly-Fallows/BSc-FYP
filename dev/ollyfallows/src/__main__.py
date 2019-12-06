from util import opengl
from model import *

if __name__ == "__main__":
    gl = opengl.opengl.get_instance()
    gl.apply_shader(
        "./model/shaders/conv.glsl",
        [
            {
                "val":[[[1,1,1],[1,-1,1],[1,1,1]]],
                "size":[1,3,3],
                "name":"IN"
            },{
                "val":[[[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0]]],
                "size":[1,5,5],
                "name":"KERNEL"
            }
        ],
        [1,3,3],
        {"EDGE_HANDLING" : 1}
    )
