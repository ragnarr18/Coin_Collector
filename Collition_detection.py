

class Collition_detection:
    def __init__(self, x_translations, z_translations, temp_char_pos):
        self.x_translations = x_translations
        self.z_translations = z_translations
        self.temp_char_pos = temp_char_pos
        self.num_of_translations = len(self.x_translations)
        self.x_collition = False
        self.z_collition = False

    def x_collition_detection(self, x_translations, z_translations, temp_char_pos):

        if self.temp_char_pos.x - self.cs < 0:
            print("hit edge")
        if self.temp_char_pos.x + self.cs > 10:
            print("hit edge")
        
        #### Map collitions
        for i in range(self.num_of_translations):
            # The 4 edges of a map box
            x1 = self.x_translations[i] - 0.5
            x2 = self.x_translations[i] + 0.5
            z1 = self.z_translations[i] - 0.5
            z2 = self.z_translations[i] + 0.5

            if self.temp_char_pos.x + self.cs > x1 and self.temp_char_pos.x + self.cs < x1 + 0.1 and self.temp_char_pos.z + self.cs > z1 and self.temp_char_pos.z - self.cs < z2:
                print(self.character.position.x, self.character.position.z)
                print(x1, x2, z1, z2)
            if self.temp_char_pos.x - self.cs < x2 and self.temp_char_pos.x - self.cs > x2 - 0.1 and self.temp_char_pos.z + self.cs > z1 and self.temp_char_pos.z - self.cs < z2:
                print("boom")

        
    def z_collition_detection(self, x_translations, z_translations, temp_char_pos):
        if self.temp_char_pos.z - self.cs < 0:
            print("hit edge")
        if self.temp_char_pos.z + self.cs > 10:
            print("hit edge")

        for i in range(self.num_of_translations):
            # The 4 edges of a map box
            x1 = self.x_translations[i] - 0.5
            x2 = self.x_translations[i] + 0.5
            z1 = self.z_translations[i] - 0.5
            z2 = self.z_translations[i] + 0.5

            if self.temp_char_pos.z + self.cs > z1 and self.temp_char_pos.z + self.cs < z1 + 0.1 and self.temp_char_pos.x + self.cs > x1 and self.temp_char_pos.x - self.cs < x2:
                print("yo")
            if self.temp_char_pos.x - self.cs < z2 and self.temp_char_pos.z - self.cs > z2 - 0.1 and self.temp_char_pos.x + self.cs > x1 and self.temp_char_pos.x - self.cs < x2:
                print("colition bby")