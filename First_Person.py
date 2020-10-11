from Matrices import *
class First_Person:
    def __init__(self,  shader, view_matrix, model_matrix, position = Point(0,0,0)):
        self.position = position
        self.shader = shader
        self.view_matrix = view_matrix
        self.model_matrix = model_matrix
        self.cube = Cube()
        self.scale = [0.4, 0.5, 0.4]

    #could maybe just put the model matrix as a parameter
    def display(self):
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.position.x, self.position.y, self.position.z)
        self.model_matrix.add_scale(self.scale[0],self.scale[1], self.scale[2])
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()
    
    def collide(self, key, view_matrix, delta_time ):
        if key == "W":
            # view_matrix.move(0, -2 * delta_time)
            pass