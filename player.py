import pygame
import math
from animator import Animator

from enemies.enemy import Enemy

class Player:
    def __init__(self, screen, sprite):
        self.offset = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
        self.sprite = sprite
        self.hitbox = pygame.Rect(self.position.x - self.sprite.get_width()/2, self.position.y - self.sprite.get_height()/2, sprite.get_width(), sprite.get_height())
        self.sword = pygame.image.load("./weapon_regular_sword.png")
        self.sword = pygame.transform.scale(self.sword, (self.sword.get_width() * 4, self.sword.get_height() * 4))
        self.sword = pygame.transform.rotate(self.sword, -90)
        self.attacking = False
        self.attack_timer = -1
        self.health = 5
        self.animator = Animator(self)
        walk_frames = [
                pygame.image.load("./sprites/player/walk_0.png"),
                pygame.image.load("./sprites/player/walk_1.png"),
                pygame.image.load("./sprites/player/walk_2.png"),
                pygame.image.load("./sprites/player/walk_3.png")
                ]
        self.animator.add_animation(walk_frames, 10, "walk")
        idle_frames = [
                pygame.image.load("./sprites/player/idle_0.png"),
                pygame.image.load("./sprites/player/idle_1.png"),
                pygame.image.load("./sprites/player/idle_2.png")
                ]
        self.animator.add_animation(idle_frames, 10, "idle")
        self.invert = False
        

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

        if x != 0 or y != 0:
            if self.animator.get_animation() != "walk":
                self.animator.set_animation("walk")
        else:
            if self.animator.get_animation() != "idle":
                self.animator.set_animation("idle")
        if x > 0:
            self.invert = True
        elif x < 0:
            self.invert = False
        
        self.animator.flip_animation(self.invert)

        self.offset.x += x * 300 * dt
        self.offset.y += y * 300 * dt

        self.position.x -= x * 300 * dt
        self.position.y -= y * 300 * dt

    def attack(self, screen, enemies) -> (list[Enemy]):
        mouse = pygame.mouse.get_pressed()
        time = pygame.time.get_ticks()
        if mouse[0] and not self.attacking:
            self.attacking = True
            self.attack_timer = time + 500
            mx = pygame.mouse.get_pos()[0]
            my = pygame.mouse.get_pos()[1]

            px = screen.get_width()/2
            py = screen.get_height()/2

            try: 
                zx = -((px-mx) * math.sqrt(10000))/math.sqrt((px-mx)**2 + (py-my)**2)
                zy = -((py-my) * math.sqrt(10000))/math.sqrt((px-mx)**2 + (py-my)**2)
            except:
                zx = 1
                zy = 1
            self.m1 = math.atan2(zy, zx)
        elif not self.attacking:
            self.attack_timer = -1

        elapsed_time = self.attack_timer - time
        if time < self.attack_timer and self.attack_timer != 1:

            # Math from https://gamedev.stackexchange.com/questions/33709/get-angle-in-radians-given-a-point-on-a-circle
            # Specifically just the line below
            m2 = self.m1-(elapsed_time-250)/250 * math.pi/3

            rotated_sword = pygame.transform.rotate(self.sword, -m2 * (180/math.pi))
            rotated_rect = rotated_sword.get_rect(center=self.sword.get_rect(center=(math.sqrt(10000) * math.cos(m2) + 960, math.sqrt(10000) * math.sin(m2) + 540)).center)
        
            screen.blit(rotated_sword, rotated_rect)

            new_enemies = []
            for enemy in enemies:
                if rotated_rect.colliderect(enemy.hitbox) and not enemy.been_attacked:
                    enemy.health -= 1
                    enemy.been_attacked = True
                if not enemy.health == 0:
                    new_enemies.append(enemy)

            return new_enemies

        elif time > self.attack_timer:
            self.attacking = False
            for enemy in enemies:
                enemy.been_attacked = False

        return enemies
