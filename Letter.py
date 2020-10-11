from Matrices import *
class Letter:
    def __init__(self,  shader, view_matrix, model_matrix, position = Point(0,0,0), color=Point(1.0, 1.0, 1.0)):
        self.position = position
        self.shader = shader
        self.view_matrix = view_matrix
        self.model_matrix = model_matrix
        self.cube = Cube()
        self.color = color
        self.scale = [0.1, 0.1, 0.1]

    def display(self):
        self.shader.set_solid_color(self.color.x, self.color.y, self.color.y)
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.position.x, self.position.y, self.position.z)
        self.model_matrix.add_scale(self.scale[0],self.scale[1], self.scale[2])
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()
    
    def pick_up(self, character_pos, n):
        #if character in reach and is looking towards the letter 
        #he can pick it up
        pass
    