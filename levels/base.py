# from math import *

# import pygame
# from pygame.locals import *

# import sys
# import time

# from Shaders import *
import sys
sys.path.append("project34\levels")
from Matrices import *
class Base:
    def __init__(self, shader, model_matrix, map_size = 20.0, map_edge = 10.0):
        self.shader = shader
        self.model_matrix = model_matrix
        self.map_size = map_size
        self.map_edge = map_edge
        self.cube = Cube()

    def display(self):
        #floor
        self.shader.set_solid_color(2.0, 1.0, 0.0)
        self.model_matrix.push_matrix()
  
        self.model_matrix.add_translation(0.0, -0.5, 0.0)
        self.model_matrix.add_scale(self.map_size, 1.0, self.map_size)
       
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

        self.shader.set_solid_color(1.5, 0.0, 1.0)
        #Kassi 1
        self.model_matrix.push_matrix()

        self.model_matrix.add_translation(0.0, 0.5, self.map_edge - 0.5) #best practice, translate -> scale -> rotate
        self.model_matrix.add_scale(self.map_size, 1.0, 1.0)       # if you mix the order, it affects differently
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

        #Kassi 2
        self.model_matrix.push_matrix()

        self.model_matrix.add_translation(0.0, 0.5, -self.map_edge + 0.5) #best practice, translate -> scale -> rotate
        self.model_matrix.add_scale(self.map_size, 1.0, 1.0)       # if you mix the order, it affects differently
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

        #Kassi 3
        self.model_matrix.push_matrix()

        self.model_matrix.add_translation(self.map_edge - 0.5, 0.5, 0.0) #best practice, translate -> scale -> rotate
        self.model_matrix.add_scale(1.0, 1.0, self.map_size)       # if you mix the order, it affects differently
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

        #Kassi 4
        self.model_matrix.push_matrix()

        self.model_matrix.add_translation(-self.map_edge + 0.5, 0.5, 0.0) #best practice, translate -> scale -> rotate
        self.model_matrix.add_scale(1.0, 1.0, self.map_size)       # if you mix the order, it affects differently
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()