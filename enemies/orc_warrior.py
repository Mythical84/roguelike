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
        self.attack_timer = -1

    def attack(self, player):
        distance = math.sqrt((player.position.y - self.y)**2 + (player.position.x - self.x)**2)
        if distance <= 100:
            if self.attack_timer == -1:
                self.attack_timer = pygame.time.get_ticks() + 2000
                self.animator.set_animation("attack")
            if pygame.time.get_ticks() > self.attack_timer:
                player.health -= 1
                self.attack_timer = -1
        else:
            self.attack_timer = -1

    def move(self, dt, player):
        if self.animator.get_animation() == "attack" and self.animator.current_frame < 3:
            self.healthbar.x = self.x - self.sprite.get_width()/2 + player.offset.x
            self.healthbar.y = self.y - self.sprite.get_height()/2 - 20 + player.offset.y
            return
        super().move(dt, player)
        # TODO: prevent enemy from getting stuck on idle frame when transition
        # from idle to moving

        # TODO: prevent enemy healthbar from sticking to player
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
