from Matrices import *
class First_Person:
    def __init__(self, position = Point(0,0,0)):
        self.position = position
        self.u = Vector(1, 0, 0) #x
        self.v = Vector(0, 1, 0) #y
        self.n = Vector(0, 0, 1) #z

    def look(self, position, center, up):
        self.position = position
        self.n = position - center
        self.n.normalize()
        self.u = up.cross(self.n)
        self.u.normalize()
        self.v = self.n.cross(self.u)

    def move(self, del_u, del_n):
        old_eye = self.position
        old_y = self.position.y
        self.position += self.u * del_u + self.n * del_n
        self.position.y = old_y
        #making sure the y coordinate is the same as before
        difference = (self.position - old_eye).__len__()
        print(difference)

    def roll(self, angle):
        c = cos(angle)
        s = sin(angle)
        #rotate u and v vector around the n vector
        temp_u = self.u * c + self.v * s
        self.v = self.u * -s + self.v * c
        self.u = temp_u

    #up down
    def pitch(self, angle):
        c = cos(angle)
        s = sin(angle)

        #rotate n and v vector around the u vector
        # if((self.v.x >= -0.4 and s > 0)  or (self.v.x < 0.8 and s < 0)):
        if True:
            temp_n = self.n * c + self.v * s
            self.v =  self.n * -s + self.v * c
            self.n = temp_n
            # print("V: " ,self.v.x,self.v.y,self.v.z)
        # else:
        #     print(self.v.x)
        #     print(c, s)
        #     print("too far")


    def yaw(self, eye_n):
        self.position += eye_n * 0.1
        