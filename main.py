import pygame
import math
import player
import map
from enemies import orc_warrior

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0


map = map.MapGenerator()

img = pygame.image.load("./knight_m_idle_anim_f0.png")
img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))

player = player.Player(screen, img)

enemies = [orc_warrior.OrcWarrior(50, 50)]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    player.move(dt)
    for enemy in enemies:
        enemy.move(dt, player)
        enemy.attack(player)
        enemy.animator.update_animation()
    screen.blit(map.floors, (player.offset.x, player.offset.y))
    screen.blit(map.walls, (player.offset.x, player.offset.y))

    for enemy in enemies:
        pygame.draw.rect(screen, "red", enemy.healthbar)
        healthbar = (enemy.healthbar.x, enemy.healthbar.y, (enemy.healthbar.width/enemy.max_health) * enemy.health, enemy.healthbar.height)
        pygame.draw.rect(screen, "green", healthbar)
        screen.blit(enemy.sprite, (enemy.x + player.offset.x - player.sprite.get_width()/2, enemy.y + player.offset.y - player.sprite.get_height()/2))

    screen.blit(player.sprite, (screen.get_width()/2 - player.sprite.get_width()/2, screen.get_height()/2 - player.sprite.get_height()/2))
    player.animator.update_animation()

    enemies = player.attack(screen, enemies)

    pygame.draw.rect(screen, 0x4C4E52, (screen.get_width()/2 - 200, 880, 200, 200))
    font = pygame.font.SysFont("Comic Sans", 30)
    screen.blit(font.render("health: " + str(player.health), False, (255, 255, 255)), (screen.get_width()/2-140, 965))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
