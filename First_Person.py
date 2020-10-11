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
    
    def collide(self, key, eye, u, n, delta_time ):
        old_y = eye.y
        if key == "W":
            eye += u * 0 + n * (-2* delta_time)
            
        if key == "S":
            old_y = eye.y
            eye += u * 0 + n * (2 * delta_time)

        eye.y = old_y
        temp_character_pos = eye + n * 0.00000000000000001
        return temp_character_pos
