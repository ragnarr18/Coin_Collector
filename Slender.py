import random

import pygame
from pygame.locals import *

import sys
import time

from Matrices import *

class Slender:
    def __init__(self,  shader, view_matrix, model_matrix, position = Point(0,0,0), color=Point(1.0, 1.0, 1.0)):
        self.position = position
        self.shader = shader
        self.view_matrix = view_matrix
        self.model_matrix = model_matrix
        self.cube = Cube()
        self.color = color
        self.scale = [0.2, 0.6, 0.2]

        self.clock = pygame.time.Clock()
        self.clock.tick()

        self.last_x = 0.0
        self.last_z = 0.0

    def display(self, angle):
        # self.shader.set_solid_color(self.color.x, self.color.y, self.color.y)
        # búkur
        self.shader.set_material_diffuse(self.color.x, self.color.y, self.color.y)
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.position.x, self.position.y, self.position.z)
        self.model_matrix.add_scale(self.scale[0],self.scale[1], self.scale[2])
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()
        # fætur
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.position.x - 0.1, self.position.y - 0.4, self.position.z)
        self.model_matrix.add_scale(0.1, 0.4, 0.1)
        self.model_matrix.add_rotation_x(angle* 1)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.position.x + 0.1, self.position.y - 0.4, self.position.z)
        self.model_matrix.add_scale(0.1, 0.4, 0.1)
        self.model_matrix.add_rotation_x(angle* 1)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()
        # hendur
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.position.x - 0.2, self.position.y + 0.1, self.position.z)
        self.model_matrix.add_scale(0.3, 0.1, 0.1)
        self.model_matrix.add_rotation_y(angle* 1)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.position.x + 0.2, self.position.y + 0.1, self.position.z)
        self.model_matrix.add_scale(0.3, 0.1, 0.1)
        self.model_matrix.add_rotation_y(angle* 1)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

        # haus
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(self.position.x, self.position.y + 0.5, self.position.z)
        self.model_matrix.add_scale(0.2, 0.2, 0.2)
        self.model_matrix.add_rotation_y(angle* 1)
        self.model_matrix.add_rotation_z(angle* 1) 
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

    
    def where_to(self, x_translations, z_translations):
        self.x_translations = x_translations
        self.z_translations = z_translations
        # 1 = +z ; 2 = -x ; 3 = -z ; 4 = +x
        self.last_x = self.position.x
        self.last_z = self.position.z
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
        
        num_of_options = len(directions) - 1
        n = randint(0, num_of_options)
        #print(directions[n])
        #print(directions)
        # print(directions)
        # print(n)
        # print(directions[n])
        return directions[n]

    def move_to(self, direction):
        delta_time = self.clock.tick() / 1000.0
        self.direction = direction
        #make him move to random positions to begin with
        #when he is close enough to the user, then he starts following the users movement
        #print(self.direction)
        #self.view_matrix.move(0, -2 * delta_time)
        if self.direction == "1":
            self.position.z += 2 * delta_time
            if self.position.z >= self.last_z + 1:
                self.position.z = self.last_z + 1
                return False
        if self.direction == "2":
            self.position.x += -2 * delta_time
            if self.position.x <= self.last_x - 1:
                self.position.x = self.last_x - 1
                return False
        if self.direction == "3":
            self.position.z += -2 * delta_time
            if self.position.z <= self.last_z - 1:
                self.position.z = self.last_z - 1
                return False
        if self.direction == "4":
            self.position.x += 2 * delta_time
            if self.position.x >= self.last_x + 1:
                self.position.x = self.last_x + 1
                return False
        return True
    