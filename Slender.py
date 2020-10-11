import random

from Matrices import *

class Slender:
    def __init__(self,  shader, view_matrix, model_matrix, position = Point(0,0,0), color=Point(1.0, 1.0, 1.0)):
        self.position = position
        self.shader = shader
        self.view_matrix = view_matrix
        self.model_matrix = model_matrix
        self.cube = Cube()
        self.color = color
        self.scale = [0.2, 1.4, 0.2]

    def display(self):
        self.shader.set_solid_color(self.color.x, self.color.y, self.color.y)
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.position.x, self.position.y, self.position.z)
        self.model_matrix.add_scale(self.scale[0],self.scale[1], self.scale[2])
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()
    
    def where_to(self, x_translations, z_translations):
        self.x_translations = x_translations
        self.z_translations = z_translations
        # 1 = +z ; 2 = -x ; 3 = -z ; 4 = +x
        directions = ['1','2', '3', '4']
        if self.position.x == 9.5: #3 áttir í boði 1,2,3
            directions.remove('4')
        if self.position.x == 0.5: #3 áttir í boði 1,2,4
            directions.remove('2')
        if self.position.z == 9.5: #3 áttir í boði 2,3,4
            directions.remove('1')
        if self.position.z == 0.5: #3 áttir í boði 1,2,4
            directions.remove('3')
        self.num_of_translations = len(self.x_translations)
        for i in range(self.num_of_translations):
            try:
                if self.position.x - 1.0 == self.x_translations[i] and self.position.z == self.z_translations[i]:
                    directions.remove('2')
                if self.position.x + 1.0 == self.x_translations[i] and self.position.z == self.z_translations[i]:
                    directions.remove('4')
                if self.position.z - 1.0 == self.z_translations[i] and self.position.x == self.x_translations[i]:
                    directions.remove('3')
                if self.position.z + 1.0 == self.z_translations[i] and self.position.x == self.x_translations[i]:
                    directions.remove('1')
            except ValueError:
                print("Cant remove number that doesnt exist in list")
        num_of_options = len(directions)
        n = randint(0, num_of_options)
        print(directions)
        print(n)
        print(directions[n])
        return directions[n]

        


    def move_to(self, position):
        #make him move to random positions to begin with
        #when he is close enough to the user, then he starts following the users movement
        print(position)
        #self.view_matrix.move(0, -2 * delta_time)
    