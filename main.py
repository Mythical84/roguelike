import pygame
import player
import map
from enemies import enemy

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0


map = map.MapGenerator()

img = pygame.image.load("./knight_m_idle_anim_f0.png")
img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))

player = player.Player(screen, img)

enemies = [enemy.Enemy(img, 50, 50, 3)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    player.move(dt)
    enemies[0].move(dt, player)
    screen.blit(map.floors, (player.offset.x, player.offset.y))
    screen.blit(map.walls, (player.offset.x, player.offset.y))

    pygame.draw.rect(screen, "red", enemies[0].hitbox, width=5)
    screen.blit(enemies[0].sprite, (enemies[0].x + player.offset.x - player.sprite.get_width()/2, enemies[0].y + player.offset.y - player.sprite.get_height()/2))
    pygame.draw.rect(screen, "green", player.hitbox, width=5)
    screen.blit(player.sprite, (screen.get_width()/2 - player.sprite.get_width()/2, screen.get_height()/2 - player.sprite.get_height()/2))

    player.attack(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
