
# from OpenGL.GL import *
# from math import * # trigonometry

# import sys

# from Base3DObjects import *

# class Shader3D:
#     def __init__(self):
#         vert_shader = glCreateShader(GL_VERTEX_SHADER)
#         shader_file = open(sys.path[0] + "/simple3D.vert")
#         glShaderSource(vert_shader,shader_file.read())
#         shader_file.close()
#         glCompileShader(vert_shader)
#         result = glGetShaderiv(vert_shader, GL_COMPILE_STATUS)
#         if (result != 1): # shader didn't compile
#             print("Couldn't compile vertex shader\nShader compilation Log:\n" + str(glGetShaderInfoLog(vert_shader)))

#         frag_shader = glCreateShader(GL_FRAGMENT_SHADER)
#         shader_file = open(sys.path[0] + "/simple3D.frag")
#         glShaderSource(frag_shader,shader_file.read())
#         shader_file.close()
#         glCompileShader(frag_shader)
#         result = glGetShaderiv(frag_shader, GL_COMPILE_STATUS)
#         if (result != 1): # shader didn't compile
#             print("Couldn't compile fragment shader\nShader compilation Log:\n" + str(glGetShaderInfoLog(frag_shader)))

#         self.renderingProgramID = glCreateProgram()
#         glAttachShader(self.renderingProgramID, vert_shader)
#         glAttachShader(self.renderingProgramID, frag_shader)
#         glLinkProgram(self.renderingProgramID)

#         self.positionLoc			= glGetAttribLocation(self.renderingProgramID, "a_position")
#         glEnableVertexAttribArray(self.positionLoc)

#         self.normalLoc			= glGetAttribLocation(self.renderingProgramID, "a_normal")
#         glEnableVertexAttribArray(self.normalLoc)

#         self.modelMatrixLoc			= glGetUniformLocation(self.renderingProgramID, "u_model_matrix")
#         self.viewMatrixLoc			= glGetUniformLocation(self.renderingProgramID, "u_view_matrix")
#         self.projectionMatrixLoc			= glGetUniformLocation(self.renderingProgramID, "u_projection_matrix")
#         self.colorLoc = glGetUniformLocation(self.renderingProgramID, "u_color")
        

#     def use(self):
#         try:
#             glUseProgram(self.renderingProgramID)   
#         except OpenGL.error.GLError:
#             print(glGetProgramInfoLog(self.renderingProgramID))
#             raise

#     def set_model_matrix(self, matrix_array):
#         glUniformMatrix4fv(self.modelMatrixLoc, 1, True, matrix_array)

#     def set_view_matrix(self, matrix_array):
#         glUniformMatrix4fv(self.viewMatrixLoc, 1, True, matrix_array)

#     def set_projection_matrix(self, matrix_array):
#         glUniformMatrix4fv(self.projectionMatrixLoc, 1, True, matrix_array)

#     # set a color
#     def set_solid_color(self, red,green,blue):
#         glUniform4f(self.colorLoc, red, green, blue, 1.0)

#     def set_position_attribute(self, vertex_array):
#         glVertexAttribPointer(self.positionLoc, 3, GL_FLOAT, False, 0, vertex_array)

#     def set_normal_attribute(self, vertex_array):
#         glVertexAttribPointer(self.normalLoc, 3, GL_FLOAT, False, 0, vertex_array)


from OpenGL.GL import *
from math import * # trigonometry

import sys

from Base3DObjects import *

class Shader3D:
    def __init__(self):
        vert_shader = glCreateShader(GL_VERTEX_SHADER)
        shader_file = open(sys.path[0] + "/simple3D.vert")
        glShaderSource(vert_shader,shader_file.read())
        shader_file.close()
        glCompileShader(vert_shader)
        result = glGetShaderiv(vert_shader, GL_COMPILE_STATUS)
        if (result != 1): # shader didn't compile
            print("Couldn't compile vertex shader\nShader compilation Log:\n" + str(glGetShaderInfoLog(vert_shader)))

        frag_shader = glCreateShader(GL_FRAGMENT_SHADER)
        shader_file = open(sys.path[0] + "/simple3D.frag")
        glShaderSource(frag_shader,shader_file.read())
        shader_file.close()
        glCompileShader(frag_shader)
        result = glGetShaderiv(frag_shader, GL_COMPILE_STATUS)
        if (result != 1): # shader didn't compile
            print("Couldn't compile fragment shader\nShader compilation Log:\n" + str(glGetShaderInfoLog(frag_shader)))

        self.renderingProgramID = glCreateProgram()
        glAttachShader(self.renderingProgramID, vert_shader)
        glAttachShader(self.renderingProgramID, frag_shader)
        glLinkProgram(self.renderingProgramID)

        self.positionLoc			= glGetAttribLocation(self.renderingProgramID, "a_position")
        glEnableVertexAttribArray(self.positionLoc)

        self.normalLoc			= glGetAttribLocation(self.renderingProgramID, "a_normal")
        glEnableVertexAttribArray(self.normalLoc)

        self.modelMatrixLoc			= glGetUniformLocation(self.renderingProgramID, "u_model_matrix")
        self.viewMatrixLoc			= glGetUniformLocation(self.renderingProgramID, "u_view_matrix")
        self.projectionMatrixLoc			= glGetUniformLocation(self.renderingProgramID, "u_projection_matrix")
        # self.colorLoc = glGetUniformLocation(self.renderingProgramID, "u_color")
        self.eyePosLoc = glGetUniformLocation(self.renderingProgramID, "u_eye_position")

        self.lightPosLoc = glGetUniformLocation(self.renderingProgramID, "u_light_position")
        self.lightPosLoc1 = glGetUniformLocation(self.renderingProgramID, "u_light_position1") #2
        self.lightPosLoc2 = glGetUniformLocation(self.renderingProgramID, "u_light_position2") #2 

        self.lightDiffuseLoc = glGetUniformLocation(self.renderingProgramID, "u_light_diffuse")
        self.lightSpecularLoc = glGetUniformLocation(self.renderingProgramID, "u_light_specular")
        self.lightDiffuseLoc1 = glGetUniformLocation(self.renderingProgramID, "u_light_diffuse1")
        self.lightSpecularLoc1 = glGetUniformLocation(self.renderingProgramID, "u_light_specular1")
        self.lightDiffuseLoc2 = glGetUniformLocation(self.renderingProgramID, "u_light_diffuse2")
        self.lightSpecularLoc2 = glGetUniformLocation(self.renderingProgramID, "u_light_specular2")

        self.materialDiffuseLoc = glGetUniformLocation(self.renderingProgramID, "u_mat_diffuse")
        self.materialSpecularLoc = glGetUniformLocation(self.renderingProgramID, "u_mat_specular")
        self.materialShininessLoc = glGetUniformLocation(self.renderingProgramID, "u_mat_shininess")


        

    def use(self):
        try:
            glUseProgram(self.renderingProgramID)   
        except OpenGL.error.GLError:
            print(glGetProgramInfoLog(self.renderingProgramID))
            raise

    def set_model_matrix(self, matrix_array):
        glUniformMatrix4fv(self.modelMatrixLoc, 1, True, matrix_array)

    def set_view_matrix(self, matrix_array):
        glUniformMatrix4fv(self.viewMatrixLoc, 1, True, matrix_array)

    def set_projection_matrix(self, matrix_array):
        glUniformMatrix4fv(self.projectionMatrixLoc, 1, True, matrix_array)

    def set_eye_position(self, position):
        glUniform4f(self.eyePosLoc, position.x, position.y, position.z, 1)

    def set_light_position(self, position):
        glUniform4f(self.lightPosLoc, position.x, position.y, position.z, 1)
    
    def set_light_position1(self, position):
        glUniform4f(self.lightPosLoc1, position.x, position.y, position.z, 1)
    
    def set_light_position2(self, position):
        glUniform4f(self.lightPosLoc2, position.x, position.y, position.z, 1)

    def set_light_diffuse(self, red, green, blue):
        glUniform4f(self.lightDiffuseLoc, red, green, blue, 1.0)
    
    def set_light_diffuse1(self, red, green, blue):
        glUniform4f(self.lightDiffuseLoc1, red, green, blue, 1.0)
    
    def set_light_diffuse2(self, red, green, blue):
        glUniform4f(self.lightDiffuseLoc2, red, green, blue, 1.0)
    
    def set_light_specular(self, red, green, blue):
        glUniform4f(self.lightSpecularLoc, red, green, blue, 1.0)
    
    def set_light_specular1(self, red, green, blue):
        glUniform4f(self.lightSpecularLoc1, red, green, blue, 1.0)

    def set_light_specular2(self, red, green, blue):
        glUniform4f(self.lightSpecularLoc2, red, green, blue, 1.0)

    def set_material_diffuse(self, red, green, blue):
        glUniform4f(self.materialDiffuseLoc, red, green, blue, 1.0)

    def set_material_specular(self, red, green, blue):
        glUniform4f(self.materialSpecularLoc, red, green, blue, 1.0)
    
    def set_material_shininess(self,shininess):
        glUniform1f(self.materialShininessLoc, shininess)

    def set_position_attribute(self, vertex_array):
        glVertexAttribPointer(self.positionLoc, 3, GL_FLOAT, False, 0, vertex_array)

    def set_normal_attribute(self, vertex_array):
        glVertexAttribPointer(self.normalLoc, 3, GL_FLOAT, False, 0, vertex_array)

