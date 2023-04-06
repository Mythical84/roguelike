import pygame
import math

class Player:
    def __init__(self, screen, sprite):
        self.offset = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
        self.sprite = sprite
        self.hitbox = pygame.Rect(self.position.x - self.sprite.get_width()/2, self.position.y - self.sprite.get_height()/2, sprite.get_width(), sprite.get_height())
        self.sword = pygame.image.load("./weapon_regular_sword.png")
        self.attacking = False
        self.attack_timer = -1

    def move(self, dt):
        y = 0
        x = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y = 1
        elif keys[pygame.K_s]:
            y = -1
        if keys[pygame.K_a]:
            x = 1
        elif keys[pygame.K_d]:
            x = -1

        denominator = math.sqrt((x*x) + (y*y))

        if (x != 0 and y != 0):
            x /= denominator
            y /= denominator

        self.offset.x += x * 300 * dt
        self.offset.y += y * 300 * dt

        self.position.x -= x * 300 * dt
        self.position.y -= y * 300 * dt

    def attack(self, screen):
        mouse = pygame.mouse.get_pressed()
        time = pygame.time.get_ticks()
        if mouse[0] and not self.attacking:
            self.attacking = True
            self.attack_timer = time + 5000
        elif not self.attacking:
            self.attack_timer = -1

        if time < self.attack_timer:
            screen.blit(self.sword, (50, 50))
