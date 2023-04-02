class Enemy:
    def __init__(self, sprite, x, y):
        self.health = 3
        self.sprite = sprite

    def register_enemy(self, sprite_list):
        sprite_list.append(self)
