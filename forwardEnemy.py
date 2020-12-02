from enemy_ import enemy

class forward(enemy_):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.timer = 0
        self.life = 20
        self.damage = 4
        self.change_x = 5
        self.change_y = 0
        self.x = x
        self.y = y

    def movement(self, timer):
        super().calc_gravity()
        self.x += self.change_x
        self.y = self.calc_gravity()

