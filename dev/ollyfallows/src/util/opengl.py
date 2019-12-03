import moderngl

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
        self.shaders = []

    def load_shader(self, source):
        pass

    def apply_shader(self, val):
        pass
