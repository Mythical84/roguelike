import math
import pygame

class Enemy:
    def __init__(self, sprite, x, y, max_health):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.max_health = max_health
        self.health = max_health
        self.hitbox = pygame.Rect(self.x - self.sprite.get_width()/2, self.y - self.sprite.get_height()/2, sprite.get_width() * 1.5, sprite.get_height() * 1.5)

    def move(self, dt, player):
        if not self.hitbox.colliderect(player.hitbox):
            speed = 250
            # The next two equations are courtesy of https://mathworld.wolfram.com/Circle-LineIntersection.html
            # Although it has been edited to fit my use case. (Also specifically just the math, not any of the code)
            dx = ((player.position.x-self.x) * speed)/math.sqrt((player.position.x-self.x)**2 + (player.position.y-self.y)**2)
            dy = ((player.position.y-self.y) * speed)/math.sqrt((player.position.x-self.x)**2 + (player.position.y-self.y)**2)

            self.x += dx * dt
            self.y += dy * dt

        self.hitbox.x = self.x - (self.sprite.get_width() * 1.5)/2 + player.offset.x
        self.hitbox.y = self.y - (self.sprite.get_height() * 1.5)/2 + player.offset.y
