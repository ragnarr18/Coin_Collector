from Matrices import *
from levels.Level1 import Level
class Mini_Map:
    def __init__(self, shader, view_matrix_top_down, model_matrix, character):
        self.character = character
        self.shader = shader
        self.view_matrix_top_down = view_matrix_top_down
        self.model_matrix = model_matrix
        self.cube = Cube()

    def display(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_DEPTH_BUFFER_BIT) #clear depth_buffer_bit to fit the minimap
        glViewport(500, 0, 300, 300) #minimap size and position
        self.shader.set_view_matrix(self.view_matrix_top_down.get_matrix())
        self.view_matrix_top_down.look(Point(5.0, 7.0, 5.0), Point(5.0, 0.0, 5.0), Vector(1, 1, 0))
        self.shader.set_view_matrix(self.view_matrix_top_down.get_matrix())
        self.model_matrix.load_identity()
        self.cube.set_vertices(self.shader)

        Level(self.shader, self.model_matrix).display()
        self.shader.set_solid_color(1.0, 0.0, 0.0)
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.character.position.x, self.character.position.y, self.character.position.z)
        self.model_matrix.add_scale(0.1 , 0.5 , 0.1)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()