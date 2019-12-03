import moderngl
import numpy as np

from . import file

class opengl:

    __instance = None

    def get_instance():
        if opengl.__instance == None:
            opengl()
        return opengl.__instance

    def __init__(self):
        if opengl.__instance != None:
            raise Exception("Singleton can only be declared once")
        else:
            opengl.__instance = self
        self.context = moderngl.create_standalone_context(require=430)
        self.shaders = {}

    def load_shader(self, source):
        self.shaders[source] = self.context.compute_shader(file.load_file(source))

    def apply_shader(self, source, val, out_size, uniforms):
        if not(source in self.shaders.keys()):
            self.load_shader(source)
        shader = self.shaders[source]
        buffer_in = self.context.buffer(np.array(val).flattern())
        buffer_in.bind_to_storage_buffer(0)
        buffer_out = self.context.buffer(np.zeros(out_size).flattern())
        buffer_out.bind_to_storage_buffer(1)
        shader.uniforms = uniforms

        shader.run()

        output = np.frombuffer(last_buffer.read(), dtype=np.float32)
        output = output.reshape((H, W, 4))

        print(output)
