from Matrices import *
from Moving_Object import *
from levels.Base import Base
class Level:
    def __init__(self, shader, model_matrix, x_translations, z_translations, map_size = 20.0, map_edge = 10.0):
        self.shader = shader
        self.model_matrix = model_matrix
        self.map_size = map_size
        self.map_edge = map_edge
        self.cube = Cube()
        self.x_translations = x_translations
        self.z_translations = z_translations
        self.num_of_translations = len(self.x_translations)
        self.scale = [1.0, 1.0, 1.0]
        self.moving_obj = Moving_Object()
        self.angle = 0

    def display(self, angle):
        Base(self.shader, self.model_matrix).display()        
        # self.shader.set_solid_color(0.8, 0.2, 0.2)
        self.shader.set_material_diffuse(0.8, 0.2, 0.2)
        for i in range(self.num_of_translations):
            self.model_matrix.push_matrix()

            self.model_matrix.add_translation(self.x_translations[i], 0.5, self.z_translations[i]) #best practice, translate -> scale -> rotate
            self.model_matrix.add_scale(self.scale[0],self.scale[1], self.scale[2])       # if you mix the order, it affects differently
            self.shader.set_model_matrix(self.model_matrix.matrix)
            self.cube.draw(self.shader)
            self.model_matrix.pop_matrix()
            i += 1
        
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.moving_obj.translations.x, self.moving_obj.translations.y, self.moving_obj.translations.z) #best practice, translate -> scale -> rotate
        self.model_matrix.add_rotation_y(angle* 0.4)
        self.model_matrix.add_rotation_z(angle* 0.2) 
        self.model_matrix.add_scale(self.moving_obj.scale[0], self.moving_obj.scale[1], self.moving_obj.scale[2])       # if you mix the order, it affects differently
        # self.moving_obj.rotate()

        
        
        # self.model_matrix.add_rotation_z(angle* 0.4)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix() 
        #add tickets