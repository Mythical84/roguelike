from enemies.enemy import Enemy
import pygame
import math

class OrcWarrior(Enemy):
    def __init__(self, x, y):
        image = pygame.image.load("./knight_m_idle_anim_f0.png")
        image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
        super().__init__(image, x, y, 5)
        walk_sprites = [
                    pygame.image.load("./sprites/enemies/orc_warrior/walk_0.png"),
                    pygame.image.load("./sprites/enemies/orc_warrior/walk_1.png"),
                    pygame.image.load("./sprites/enemies/orc_warrior/walk_2.png"),
                    pygame.image.load("./sprites/enemies/orc_warrior/walk_3.png")
                ]
        self.animator.add_animation(walk_sprites, 10, "walk")
        self.animator.add_animation([pygame.image.load("./sprites/enemies/orc_warrior/attack_0.png")], 1, "idle")
        attack_sprites = [
                pygame.image.load("./sprites/enemies/orc_warrior/attack_0.png"),
                pygame.image.load("./sprites/enemies/orc_warrior/attack_1.png"),
                pygame.image.load("./sprites/enemies/orc_warrior/attack_2.png"),
                pygame.image.load("./sprites/enemies/orc_warrior/attack_3.png")
                ]
        self.animator.add_animation(attack_sprites, 10, "attack")

    def attack(self, player):
        distance = math.sqrt((player.position.y - self.y)**2 + (player.position.x - self.x)**2)

    def move(self, dt, player):
        super().move(dt, player)
        # TODO: prevent enemy from getting stuck on idle frame when transition
        # from idle to moving
        if self.moving:
            if self.animator.get_animation() != "walk":
                self.animator.set_animation("walk")
        else:
            if self.animator.get_animation() != "idle":
                self.animator.set_animation("idle")

        if self.dx < 0:
            self.animator.flip_animation(True)
        else:
            self.animator.flip_animation(False)
