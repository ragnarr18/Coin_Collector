from Matrices import *
class Character:
    def __init__(self, shader, model_matrix, x=0.1 , y=1.0 , z=0.1, color=Point(0.5, 0.9, 0.9)):
        self.shader = shader
        self.model_matrix = model_matrix
        # self.map_size = map_size
        # self.map_edge = map_edge
        self.cube = Cube()
        self.color = color
        self.x = x
        self.y = y
        self.z = z
        self.position = Point(0,0,0)
        self.u = Vector(1, 0, 0) #x
        self.v = Vector(0, 1, 0) #y
        self.n = Vector(0, 0, 1) #z
        self.camera_point = Point()
        
        # self.camera_position


    def display(self):
        self.shader.set_solid_color(self.color.x, self.color.y, self.color.y)
        self.model_matrix.push_matrix()

        self.model_matrix.add_translation(self.position.x, self.position.y, self.position.z) #best practice, translate -> scale -> rotate
        self.model_matrix.add_scale(self.x, self.y, self.z)       # if you mix the order, it affects differently
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()
        print("character position: " , self.position.x, ",",self.position.y, ",",self.position.z)
    
    def look(self, eye, center, up):
        self.position = eye
        self.n = eye - center
        self.n.normalize()
        self.u = up.cross(self.n)
        self.u.normalize()
        self.v = self.n.cross(self.u)

    def move(self, del_u, del_n):
        self.position += self.u * del_u + self.n * del_n

    def yaw(self, angle):
        c = cos(angle)
        s = sin(angle)
        #rotate n and u vector around the v vector
        temp_n = self.n * c + self.u * s
        self.u =  self.n * -s + self.u * c
        self.n = temp_n