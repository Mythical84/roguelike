import math
import pygame

from animator import Animator

class Enemy:
    def __init__(self, sprite, x, y, max_health):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.max_health = max_health
        self.health = max_health
        self.hitbox = pygame.Rect(self.x - self.sprite.get_width()/2, self.y - self.sprite.get_height()/2, sprite.get_width(), sprite.get_height())
        self.been_attacked = False
        self.healthbar = pygame.Rect(self.x - self.sprite.get_width()/2, self.y - self.sprite.get_height()/2, self.sprite.get_width(), 15)
        self.animator = Animator(self)
        self.dx = 0
        self.dy = 0
        self.moving = False

    def move(self, dt, player):
        distance = math.sqrt((player.position.y - self.y)**2 + (player.position.x - self.x)**2)
        if distance > 100:
            speed = 250
            # The next two equations are courtesy of https://mathworld.wolfram.com/Circle-LineIntersection.html
            # Although it has been edited to fit my use case. (Also specifically just the math, not any of the code)
            self.dx = ((player.position.x-self.x) * speed)/math.sqrt((player.position.x-self.x)**2 + (player.position.y-self.y)**2)
            self.dy = ((player.position.y-self.y) * speed)/math.sqrt((player.position.x-self.x)**2 + (player.position.y-self.y)**2)

            self.x += self.dx * dt
            self.y += self.dy * dt
            self.moving = True
        else:
            self.moving = False

        self.hitbox.x = self.x - (self.sprite.get_width() * 1.5)/2 + player.offset.x
        self.hitbox.y = self.y - (self.sprite.get_height() * 1.5)/2 + player.offset.y

        self.healthbar.x = self.x - self.sprite.get_width()/2 + player.offset.x
        self.healthbar.y = self.y - self.sprite.get_height()/2 - 20 + player.offset.y
