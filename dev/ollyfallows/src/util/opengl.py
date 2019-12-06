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

    def load_shader(self, source, replacements={}):
        shader = file.load_file(source)
        for a in replacements.keys():
            shader = shader.replace(a, str(replacements[a]))
        return self.context.compute_shader(shader)

    def apply_shader(self, source, in_buffers, out_size, replacements={}):
        rep = {
            'OUT_SIZE_X' : out_size[2],
            'OUT_SIZE_Y' : out_size[1],
            'OUT_SIZE_Z' : out_size[0]
        }
        for a in in_buffers:
            rep[a['name']+"_SIZE_X"] = a['size'][2]
            rep[a['name']+"_SIZE_Y"] = a['size'][1]
            rep[a['name']+"_SIZE_Z"] = a['size'][0]
        rep.update(replacements)


        shader = self.load_shader(source, rep)

        buffer_i = 0

        for a in in_buffers:
            in_buffer = self.context.buffer(np.array(a['val'], dtype=np.float32).flatten())
            in_buffer.bind_to_storage_buffer(buffer_i)
            buffer_i += 1

        out_buffer = self.context.buffer(np.zeros(out_size, dtype=np.float32).flatten())
        out_buffer.bind_to_storage_buffer(buffer_i)

        shader.run()

        output = np.frombuffer(out_buffer.read(), dtype=np.float32)
        output = output.reshape(out_size)

        print(output)
        return output
