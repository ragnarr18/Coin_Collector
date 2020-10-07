from Matrices import *

from levels.Base import Base
class Level:
    def __init__(self, shader, model_matrix, map_size = 20.0, map_edge = 10.0):
        self.shader = shader
        self.model_matrix = model_matrix
        self.map_size = map_size
        self.map_edge = map_edge
        self.cube = Cube()
        self.x_translations = [1.5, 2.5, 3.5, 5.5, 1.5, 1.5, 1.5, 0.5, 2.5, 2.5, 3.5, 3.5, 3.5, 9.5, 7.5, 9.5, 5.5, 6.5, 7.5, 7.5, 5.5, 7.5, 8.5, 9.5, 5.5, 7.5, 3.5, 5.5, 9.5, 1.5, 5.5, 7.5, 1.5, 2.5, 3.5, 7.5, 8.5, 9.5, 2.5, 5.5]
        self.z_translations = [1.5, 1.5, 1.5, 0.5, 2.5, 3.5, 5.5, 5.5, 3.5, 5.5, 3.5, 4.5, 5.5, 0.5, 2.5, 2.5, 3.5, 3.5, 3.5, 4.5, 5.5, 5.5, 5.5, 5.5, 1.5, 1.5, 6.5, 6.5, 6.5, 7.5, 7.5, 7.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 9.5, 9.5]
        self.num_of_translations = len(self.x_translations)

    def display(self):
        Base(self.shader, self.model_matrix).display()

        # self.shader.set_solid_color(0.0, 0.6, 0.6)
        # self.model_matrix.push_matrix()

        # self.model_matrix.add_translation(1.0, 0.5, 1) #best practice, translate -> scale -> rotate
        # self.model_matrix.add_scale(0.5, 1.0, 0.5)       # if you mix the order, it affects differently
        # self.shader.set_model_matrix(self.model_matrix.matrix)
        # self.cube.draw(self.shader)
        # self.model_matrix.pop_matrix()
        
        self.shader.set_solid_color(0.8, 0.2, 0.2)
        for i in range(self.num_of_translations):
            self.model_matrix.push_matrix()

            self.model_matrix.add_translation(self.x_translations[i], 0.5, self.z_translations[i]) #best practice, translate -> scale -> rotate
            self.model_matrix.add_scale(1.0, 1.0, 1.0)       # if you mix the order, it affects differently
            self.shader.set_model_matrix(self.model_matrix.matrix)
            self.cube.draw(self.shader)
            self.model_matrix.pop_matrix()
            i += 1