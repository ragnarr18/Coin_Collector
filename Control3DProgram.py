from math import *

import pygame
from pygame.locals import *

import sys
import time

from First_Person import *
from Shaders import *
from levels.Base import Base
from levels.Level1 import Level
from Matrices import *
from Character import *
from Mini_Map import *
from Slender import *
from Collition_detection import *
class GraphicsProgram3D:
    def __init__(self):
        pygame.init() 
        pygame.display.set_mode((800,600), pygame.OPENGL|pygame.DOUBLEBUF)
        self.shader = Shader3D()
        self.shader.use()
        self.model_matrix = ModelMatrix()
        self.view_matrix = ViewMatrix()
        self.view_matrix_top_down = ViewMatrix()
        self.projection_matrix = ProjectionMatrix()
        self.Collition_detection = Collition_detection()
        self.fov = pi / 2
        self.projection_matrix.set_perspective(self.fov , 888/ 600, 0.05, 100000)
        self.shader.set_projection_matrix(self.projection_matrix.get_matrix())
        self.cube = Cube()
        self.view_matrix.look(Point(0.5, 0.5, 0.5), Point(1, 0.5, 0), Vector(0, 1, 0))
        # character_pos = Point(0.5, 0.5, 0.5) + self.view_matrix.n * 0.1
        character_pos = Point(0.5, 0.5, 0.5)
        self.character = First_Person(self.shader, self.view_matrix, self.model_matrix ,character_pos)  #setting character directly behind the camera
        self.slender = Slender(self.shader, self.view_matrix, self.model_matrix, Point(9.5, 0.5, 9.5))
        self.Mini_Map = Mini_Map(self.shader,self.view_matrix_top_down,self.model_matrix, self.character, self.slender)
        self.clock = pygame.time.Clock()
        self.clock.tick()

        #white box man stuff
        self.moveing = False
        self.direction = 0

        #Translations
        self.x_translations = [1.5, 2.5, 3.5, 5.5, 1.5, 1.5, 1.5, 0.5, 2.5, 2.5, 3.5, 3.5, 3.5, 9.5, 7.5, 9.5, 5.5, 6.5, 7.5, 7.5, 5.5, 7.5, 8.5, 9.5, 5.5, 7.5, 3.5, 5.5, 9.5, 1.5, 5.5, 7.5, 1.5, 2.5, 3.5, 7.5, 8.5, 9.5, 2.5, 5.5]
        self.z_translations = [1.5, 1.5, 1.5, 0.5, 2.5, 3.5, 5.5, 5.5, 3.5, 5.5, 3.5, 4.5, 5.5, 0.5, 2.5, 2.5, 3.5, 3.5, 3.5, 4.5, 5.5, 5.5, 5.5, 5.5, 1.5, 1.5, 6.5, 6.5, 6.5, 7.5, 7.5, 7.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 9.5, 9.5]
        self.num_of_translations = len(self.x_translations)
        
        #þannig að maður kemst ekki hálfa leið inní vegg
        self.cs = 0.2

        self.angle = 0
        self.W_key_down = False
        self.S_key_down = False
        self.A_key_down = False
        self.D_key_down = False 
        self.G_key_down = False
        self.T_key_down = False
        self.E_key_down = False
        self.Q_key_down = False
        self.UP_key_down = False
        self.DOWN_key_down = False
        self.Y_key_down = False
        self.top_down = False
        self.dead = False #when mr whitestick kills user, turn schreen red and restart

    def update(self):
        delta_time = self.clock.tick() / 1000.0
        self.angle += pi * delta_time

        if self.W_key_down:
            x = self.view_matrix.eye.x
            y = self.view_matrix.eye.y
            z = self.view_matrix.eye.z

            eye_copy = Point(x,y,z)
            temp_character_pos = self.character.collide("W", eye_copy, self.view_matrix.u, self.view_matrix.n, delta_time)
            #check collition
            self.collition = self.Collition_detection.collition_detection(self.x_translations, self.z_translations, temp_character_pos, self.character.position.x, self.character.position.z)
            #self.z_collition = self.Collition_detection.z_collition_detection(self.xd_translations, self.z_translations, temp_character_pos, self.character.position.x, self.character.position.z)
            
            #print(self.x_collition, self.z_collition)
            if self.collition == "1":
                self.view_matrix.move_z(0, -2 * delta_time)
                self.collition = False
            
            elif self.collition == "2":
                self.view_matrix.move_x(0, -2 * delta_time)
                self.collition = False
            
            # elif self.z_collition == True and self.x_collition == True:
            #     self.x_collition = False
            #     self.z_collition = False

            else:
                self.view_matrix.move(0, -2 * delta_time)
        
        if self.S_key_down:
            x = self.view_matrix.eye.x
            y = self.view_matrix.eye.y
            z = self.view_matrix.eye.z

            eye_copy = Point(x,y,z)
            temp_character_pos = self.character.collide("S", eye_copy, self.view_matrix.u, self.view_matrix.n, delta_time)
            #check collition
            self.collition = self.Collition_detection.collition_detection(self.x_translations, self.z_translations, temp_character_pos, self.character.position.x, self.character.position.z)
            #self.z_collition = self.Collition_detection.z_collition_detection(self.x_translations, self.z_translations, temp_character_pos, self.character.position.x, self.character.position.z)
            if self.collition == "1":
                self.view_matrix.move_z(0, 2 * delta_time)
                self.collition = False
            elif self.collition == "2":
                self.view_matrix.move_x(0, 2 * delta_time)
                self.collition = False
            # elif self.collition == True and self.collition == True:
            #     self.collition = False
            #     self.collition = False
            else:
                self.view_matrix.move(0, 2 * delta_time)
        
        if self.A_key_down:
            self.view_matrix.yaw(pi * delta_time)
        
        if self.D_key_down:
            self.view_matrix.yaw(-pi * delta_time)
        
        if self.E_key_down:
            self.view_matrix.yaw(-pi * delta_time)
            
        if self.Q_key_down:
            self.view_matrix.yaw(pi * delta_time)
        
        if self.UP_key_down:
            self.view_matrix.pitch(-pi * delta_time)
        
        if self.DOWN_key_down:
            self.view_matrix.pitch(pi * delta_time)

        if self.Y_key_down:
            self.top_down =  not self.top_down
        
        self.character.position = self.view_matrix.eye + self.view_matrix.n * 0.00000000000000001
        self.character.position.y = 0

        if self.moveing == False:
            self.direction = self.slender.where_to(self.x_translations, self.z_translations)
            print(self.slender.position)
            self.moveing = True
        
        if self.moveing == True:
            self.moveing = self.slender.move_to(self.direction)
            

        #self.slender.where_to()
            # print(self.character.position)
        # print(self.view_matrix.eye)

        # if angle > 2 * pi:
        #     angle -= (2 * pi)
        #print(self.character.position.x, self.character.position.y, self.character.position.z)
    
        # if self.T_key_down: #zoom
        #     self.fov -= 0.25 * delta_time

        
        # if self.G_key_down: #zoom
        #     self.fov += 0.25 * delta_time

    def display(self):
        glEnable(GL_DEPTH_TEST)  ### --- NEED THIS FOR NORMAL 3D BUT MANY EFFECTS BETTER WITH glDisable(GL_DEPTH_TEST) ... try it! --- ###
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)  ### --- YOU CAN ALSO CLEAR ONLY THE COLOR OR ONLY THE DEPTH --- ###
        glViewport(0, 0, 800, 600)
        # self.shader.set_eye_position(self.view_matrix.eye) # set eye position to eye
        
        self.projection_matrix.set_perspective(self.fov , 888/ 600, 0.05, 100000)
        self.shader.set_projection_matrix(self.projection_matrix.get_matrix())

        self.shader.set_view_matrix(self.view_matrix.get_matrix())

        self.model_matrix.load_identity()
        self.cube.set_vertices(self.shader)
        #setting light at point
        
        self.shader.set_light_position(self.view_matrix.eye)
        self.shader.set_light_position1(Point(5.0, 5.0 , 20))

        self.shader.set_light_diffuse(0.8, 0.8, 0.8) # light that is of different color
        self.shader.set_light_specular(0.5, 0.5, 0.5) # light that is of different color
        self.model_matrix.load_identity()
        self.cube.set_vertices(self.shader)

        self.shader.set_material_specular(0.5, 0.5, 0.5)
        self.shader.set_material_shininess(5.0)
        self.shader.set_material_diffuse(0.5, 0.5, 0.5)

        Level(self.shader, self.model_matrix, self.x_translations, self.z_translations).display(self.angle)
        # self.character.display()
        # self.shader.set_solid_color(1.0, 0.0, 0.0)
        # self.shader.set_material_diffuse(1.0, 0.0, 0.0)
        self.character.display()
        self.slender.display()
        if self.top_down:
            self.Mini_Map.display(self.angle)
        # print(self.character.position)
        pygame.display.flip()
       

    def program_loop(self):
        exiting = False
        while not exiting:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting!")
                    exiting = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        print("Escaping!")
                        exiting = True
                    
                    if event.key == K_w:
                        self.W_key_down = True
                    
                    if event.key == K_s:
                        self.S_key_down = True
                    
                    if event.key == K_a:
                        self.A_key_down = True

                    if event.key == K_d:
                        self.D_key_down = True
                    
                    if event.key == K_t:
                        self.T_key_down = True #zoom

                    if event.key == K_g:
                        self.G_key_down = True #zoom

                    if event.key == K_e: #rotate right
                        self.E_key_down = True

                    if event.key == K_q: #rotate left
                        self.Q_key_down = True 

                    if event.key == K_UP: #rotate left
                        self.UP_key_down = True 

                    if event.key == K_DOWN: #rotate left
                        self.DOWN_key_down = True 
                    
                    if event.key == K_y: #change cam view
                        self.Y_key_down = True

                elif event.type == pygame.KEYUP:
                    if event.key == K_w:
                        self.W_key_down = False
                    
                    if event.key == K_s:
                        self.S_key_down = False
                    
                    if event.key == K_a:
                        self.A_key_down = False

                    if event.key == K_d:
                        self.D_key_down = False

                    if event.key == K_t:
                        self.T_key_down = False

                    if event.key == K_g:
                        self.G_key_down = False
                    
                    if event.key == K_e:
                        self.E_key_down = False

                    if event.key == K_q:
                        self.Q_key_down = False 
                    
                    if event.key == K_UP:
                        self.UP_key_down = False
                    
                    if event.key == K_DOWN:
                        self.DOWN_key_down = False

                    if event.key == K_y: #change cam view
                        self.Y_key_down = False

            self.update()
            self.display()

        #OUT OF GAME LOOP
        pygame.quit()

    def start(self):
        self.program_loop()

if __name__ == "__main__":
    GraphicsProgram3D().start()