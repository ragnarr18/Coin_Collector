
# from OpenGL.GL import *
# from OpenGL.GLU import *
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
# from levels.Level1 import *

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
        # self.projection_matrix.set_orthographic(-2, 2, -2, 2, 0.5, 10)
        self.fov = pi / 2
        self.projection_matrix.set_perspective(self.fov , 888/ 600, 0.05, 100000)
        self.shader.set_projection_matrix(self.projection_matrix.get_matrix())

        self.cube = Cube()
        # self.character = Character(self.shader, self.model_matrix)
 
        self.view_matrix.look(Point(0.5, 0.5, 0.5), Point(1, 0.5, 0), Vector(0, 1, 0))
        # self.character.look(Point(1, 0.5,0), Point(0, 0.5, 0), Vector(0, 1, 0))
        character_pos = Point(0.5, 0.5, 0.5) + self.view_matrix.n * 0.1
        self.character = First_Person(self.shader, self.view_matrix, self.model_matrix ,character_pos)  #setting character directly behind the camera
        self.Mini_Map = Mini_Map(self.shader,self.view_matrix_top_down,self.model_matrix, self.character)
        self.clock = pygame.time.Clock()
        self.clock.tick()

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
        self.white_background = False

    def update(self):
        delta_time = self.clock.tick() / 1000.0

        # self.angle += pi * delta_time
        if self.W_key_down:
            # self.view_matrix.slide(0, 0, -1 * delta_time)
            # print("movespeed: ", -1*delta_time)
            self.view_matrix.move(0, -1 * delta_time)
            # self.character.move(0, -1 * delta_time)
            # self.character.move(0, -1 * delta_time)

        if self.S_key_down:
            # self.view_matrix.slide(0, 0, 1 * delta_time)
            self.view_matrix.move(0, 1 * delta_time)
            # self.character.move(0, 1 * delta_time)
            # self.character.move(0, 1 * delta_time)
        
        if self.A_key_down:
            # self.view_matrix.slide(-1 * delta_time, 0, 0)
            # self.view_matrix.roll(pi * delta_time)
            # self.view_matrix.move(-1 * delta_time, 0)
            self.view_matrix.yaw(pi * delta_time)
            # self.character.yaw(self.view_matrix.n)
            # self.character.yaw(pi * delta_time)
        
        if self.D_key_down:
            # self.view_matrix.slide(1 * delta_time, 0, 0)
            # self.view_matrix.roll(- pi * delta_time)
            # self.view_matrix.move(1 * delta_time, 0)
            self.view_matrix.yaw(-pi * delta_time)
            # self.character.yaw(self.view_matrix.n)
            # self.character.yaw(-pi * delta_time)
        
        # if self.T_key_down: #zoom
        #     self.fov -= 0.25 * delta_time
        
        # if self.G_key_down: #zoom
        #     self.fov += 0.25 * delta_time

        if self.E_key_down:
            self.view_matrix.yaw(-pi * delta_time)
            

        if self.Q_key_down:
            self.view_matrix.yaw(pi * delta_time)
            # self.character.yaw(pi * delta_time)
        
        if self.UP_key_down:
            self.view_matrix.pitch(-pi * delta_time)
        
        if self.DOWN_key_down:
            self.view_matrix.pitch(pi * delta_time)

        # if self.UP_key_down:
        #     self.white_background = True
        # else:
        #     self.white_background = False

        if self.Y_key_down:
            # self.view_matrix.look(Point(5.0, 7.0, 5.0), Point(5.0, 0.0, 5.0), Vector(1, 1, 0))
            self.top_down = True
        self.character.position = self.view_matrix.eye + self.view_matrix.n * 0.1
    

    def display(self):
        glEnable(GL_DEPTH_TEST)  ### --- NEED THIS FOR NORMAL 3D BUT MANY EFFECTS BETTER WITH glDisable(GL_DEPTH_TEST) ... try it! --- ###

        if self.white_background:
            glClearColor(1.0, 1.0, 1.0, 1.0)
        else:
            glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)  ### --- YOU CAN ALSO CLEAR ONLY THE COLOR OR ONLY THE DEPTH --- ###
        glViewport(0, 0, 800, 600)

        self.projection_matrix.set_perspective(self.fov , 888/ 600, 0.05, 100000)
        self.shader.set_projection_matrix(self.projection_matrix.get_matrix())

        self.shader.set_view_matrix(self.view_matrix.get_matrix())

        self.model_matrix.load_identity()
        self.cube.set_vertices(self.shader)

        Level(self.shader, self.model_matrix).display()
        self.shader.set_solid_color(1.0, 0.0, 0.0)
        self.character.display()
        if self.top_down:
            self.Mini_Map.display()
            # glClearColor(0.0, 0.0, 0.0, 1.0)
            # glClear(GL_DEPTH_BUFFER_BIT) #clear depth_buffer_bit to fit the minimap
            # glViewport(500, 0, 300, 300) #minimap size and position
            # self.shader.set_view_matrix(self.view_matrix_top_down.get_matrix())
            # self.view_matrix_top_down.look(Point(5.0, 7.0, 5.0), Point(5.0, 0.0, 5.0), Vector(1, 1, 0))
            # self.shader.set_view_matrix(self.view_matrix_top_down.get_matrix())
            # self.model_matrix.load_identity()
            # self.cube.set_vertices(self.shader)

            # Level(self.shader, self.model_matrix).display()
            
            # self.shader.set_solid_color(1.0, 0.0, 0.0)
            # self.model_matrix.push_matrix()
            
            # # print(self.n)
            # # print(self.view_matrix.eye)
            # # curr = Point(self.view_matrix.eye.x + self.view_matrix.n.x, self.view_matrix.eye.y , self.view_matrix.eye.z + self.view_matrix.n.x)
            # # print(self.view_matrix.n)
            # # curr = self.view_matrix.eye + ( self.view_matrix.u * -0.1) + (self.view_matrix.n* 0.1)
            # # curr = self.view_matrix.eye  + self.view_matrix.n * -0.2
            # # print(self.character.position)


            # self.model_matrix.add_translation(self.character.position.x, self.character.position.y, self.character.position.z)
            # self.model_matrix.add_scale(0.1 , 0.5 , 0.1)
            # self.shader.set_model_matrix(self.model_matrix.matrix)
            # self.cube.draw(self.shader)
            # self.model_matrix.pop_matrix()
            

        ###
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
            
            self.update()
            self.display()

        #OUT OF GAME LOOP
        pygame.quit()

    def start(self):
        self.program_loop()

if __name__ == "__main__":
    GraphicsProgram3D().start()