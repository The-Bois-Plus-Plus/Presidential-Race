from enemy_ import enemy

class jumping(enemy_):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.timer = 0
        self.life = 25
        self.damage = 7
        self.change_x = 2
        self.change_y = 5
        self.x = x
        self.y = y

    def movement(self, timer):
        self.calc_grav()
        t = 0
        
        if timer % 4 == 0:
            t = self.timer
            self.x += self.change_x
            self.y += self.change_y
        elif timer == t + 1 and t != 0:
            self.y -= self.calc_grav()
            
        

            


