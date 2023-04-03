import math

class Enemy:
    def __init__(self, sprite, x, y):
        self.health = 3
        self.sprite = sprite
        self.x = x
        self.y = y

    def move(self, dt, player):
        speed = 5
        # The next two equations are courtesy of https://mathworld.wolfram.com/Circle-LineIntersection.html
        # Although it have been edited to fit my use case. (Also specifically just the math, not any of the code)
        dx = ((player.position.x-self.x) * speed)/math.sqrt((player.position.x-self.x)**2 + (player.position.y-self.y)**2)
        dy = ((player.position.y-self.y) * speed)/math.sqrt((player.position.x-self.x)**2 + (player.position.y-self.y)**2)

        self.x += dx
        self.y += dy

        print(self.x, ", ", self.y, "e")
