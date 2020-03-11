import moderngl
import numpy as np

from . import file

class opengl:

    __instance = None

    # Singleton access method
    def get_instance():
        if opengl.__instance == None:
            opengl()
        return opengl.__instance

    # Singleton constructor
    def __init__(self):
        if opengl.__instance != None:
            raise Exception("Singleton can only be declared once")
        else:
            opengl.__instance = self
        # Initialise an opengl context(Can only be done once per program)
        self.context = moderngl.create_standalone_context(require=430)

    # Method for replacing values within a shader file and compilation of said
    # shader file
    def load_shader(self, source, replacements={}):
        shader = file.load_file(source)
        for a in replacements.keys():
            shader = shader.replace(a, str(replacements[a]))
        return self.context.compute_shader(shader)

    # Function to execute a shader program
    def apply_shader(self, source, in_buffers, out_size, replacements={}):
        # Create a dict of terms to replace with given values
        rep = {
            'OUT_SIZE_X' : out_size[2],
            'OUT_SIZE_Y' : 1,
            'OUT_SIZE_Z' : 1,
            'SIZE_H'     : out_size[1]
        }
        for a in in_buffers:
            rep[a['name']+"_SIZE_X"] = a['size'][2]
            rep[a['name']+"_SIZE_Y"] = a['size'][1]
            rep[a['name']+"_SIZE_Z"] = a['size'][0]
        rep.update(replacements)

        # Compile the shader program
        shader = self.load_shader(source, rep)

        # Variables used to track buffers to ensure their memory is freed
        buffer_i = 0
        buffers = []

        # For loop for creating each input buffer
        for a in in_buffers:
            # Generate buffer with values from a numpy array
            in_buffer = self.context.buffer(np.array(a['val'], dtype=np.float32).flatten())
            # Bind the buffer to the video memory
            in_buffer.bind_to_storage_buffer(buffer_i)
            # Add the buffer to the list of buffers to be freed later
            buffers.append(in_buffer)
            # Increment the buffer index variable
            buffer_i += 1

        # Generate the output buffer
        out_buffer = self.context.buffer(np.zeros(out_size, dtype=np.float32).flatten())
        # Bind the output buffer to the video memory
        out_buffer.bind_to_storage_buffer(buffer_i)

        # Execute the shader program
        shader.run(group_x=out_size[1], group_y=1)

        # Get the values from the output buffer
        output = np.frombuffer(out_buffer.read(), dtype=np.float32)
        # Reshape the buffer from 1d to a 3d array
        output = output.reshape(out_size)

        # Iterate through all input buffers to be freed
        for a in buffers:
            a.release()
        # Free the data of the output buffer
        out_buffer.release()

        # Return the value of the output
        return output
