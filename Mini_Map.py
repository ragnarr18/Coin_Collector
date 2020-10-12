from Matrices import *
from levels.Level1 import Level
class Mini_Map:
    def __init__(self, shader, view_matrix_top_down, model_matrix, character, slender):
        self.character = character
        self.slender = slender
        self.shader = shader
        self.view_matrix_top_down = view_matrix_top_down
        self.model_matrix = model_matrix
        self.cube = Cube()
        self.x_translations = [1.5, 2.5, 3.5, 5.5, 1.5, 1.5, 1.5, 0.5, 2.5, 2.5, 3.5, 3.5, 3.5, 9.5, 7.5, 9.5, 5.5, 6.5, 7.5, 7.5, 5.5, 7.5, 8.5, 9.5, 5.5, 7.5, 3.5, 5.5, 9.5, 1.5, 5.5, 7.5, 1.5, 2.5, 3.5, 7.5, 8.5, 9.5, 2.5, 5.5]
        self.z_translations = [1.5, 1.5, 1.5, 0.5, 2.5, 3.5, 5.5, 5.5, 3.5, 5.5, 3.5, 4.5, 5.5, 0.5, 2.5, 2.5, 3.5, 3.5, 3.5, 4.5, 5.5, 5.5, 5.5, 5.5, 1.5, 1.5, 6.5, 6.5, 6.5, 7.5, 7.5, 7.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 9.5, 9.5]
        self.num_of_translations = len(self.x_translations)

    def display(self, angle):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_DEPTH_BUFFER_BIT) #clear depth_buffer_bit to fit the minimap
        glViewport(500, 0, 300, 300) #minimap size and position
        self.shader.set_view_matrix(self.view_matrix_top_down.get_matrix())
        self.view_matrix_top_down.look(Point(5.0, 7.0, 5.0), Point(5.0, 0.0, 5.0), Vector(1, 1, 0))
        self.shader.set_view_matrix(self.view_matrix_top_down.get_matrix())
        self.model_matrix.load_identity()
        self.cube.set_vertices(self.shader)

        Level(self.shader, self.model_matrix, self.x_translations, self.z_translations).display(angle)
        self.character.display()
        self.slender.display(angle)