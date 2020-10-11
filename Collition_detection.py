from Matrices import *

class Collition_detection:
    def __init__(self, x_translations, z_translations, char_pos_x, char_pos_z):
        self.x_translations = x_translations
        self.z_translations = z_translations
        self.char_pos_x = char_pos_x
        self.char_pos_y = char_pos_y
        self.num_of_translations = len(self.x_translations)
        self.x_collition = False
        self.z_collition = False

    def x_collition_detection(self):

        if self.character.position.x - self.cs < 0:
            print("hit edge")
        if self.character.position.x + self.cs > 10:
            print("hit edge")
        if self.character.position.z - self.cs < 0:
            print("hit edge")
        if self.character.position.z + self.cs > 10:
            print("hit edge")
        
        #### Map collitions
        for i in range(self.num_of_translations):
            # The 4 edges of a map box
            x1 = self.x_translations[i] - 0.5
            x2 = self.x_translations[i] + 0.5
            z1 = self.z_translations[i] - 0.5
            z2 = self.z_translations[i] + 0.5

            if self.character.position.x + self.cs > x1 and self.character.position.x + self.cs < x1 + 0.1 and self.character.position.z + self.cs > z1 and self.character.position.z - self.cs < z2:
                print(self.character.position.x, self.character.position.z)
                print(x1, x2, z1, z2)
            if self.character.position.x - self.cs < x2 and self.character.position.x - self.cs > x2 - 0.1 and self.character.position.z + self.cs > z1 and self.character.position.z - self.cs < z2:
                print("boom")
            if self.character.position.z + self.cs > z1 and self.character.position.z + self.cs < z1 + 0.1 and self.character.position.x + self.cs > x1 and self.character.position.x - self.cs < x2:
                print("yo")
            if self.character.position.z - self.cs < z2 and self.character.position.z - self.cs > z2 - 0.1 and self.character.position.x + self.cs > x1 and self.character.position.x - self.cs < x2:
                print("colition bby")
        
        def x_collition_detection(self):