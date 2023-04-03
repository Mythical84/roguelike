import pygame
import math

class Player:
    def __init__(self, screen, sprite):
        self.position = pygame.Vector2(-(screen.get_width()/2 - sprite.get_width()/2), -(screen.get_height()/2 - sprite.get_height()/2))
        
    def move(self, dt):
        y = 0
        x = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y = -1
        elif keys[pygame.K_s]:
            y = 1
        if keys[pygame.K_a]:
            x = -1
        elif keys[pygame.K_d]:
            x = 1

        denominator = math.sqrt((x*x) + (y*y))

        if (x != 0 and y != 0):
            x /= denominator
            y /= denominator

        self.position.x += x * 300 * dt
        self.position.y += y * 300 * dt

        print(self.position.x, ", ", self.position.y)
