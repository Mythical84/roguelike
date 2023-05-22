# roguelike
# Tyler Artinger
# 5/19/23
# A roguelike game
# I pledge on my honor not to lie cheat steal plagiarize or vandalize

import pygame
import player
import map
from enemies import orc_warrior
from button import Button
import os
import sys

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

dt = 0

map = map.MapDrawer()

img = pygame.image.load("./knight_m_idle_anim_f0.png")
img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))

player = player.Player(screen, img)

enemies = map.enemies

replay = Button("./restart.png")


heart = pygame.image.load("./heart_full.png")
heart = pygame.transform.scale(heart, (heart.get_width() * 4, heart.get_height() * 4))

half_heart = pygame.image.load("./heart_half_full.png")
half_heart = pygame.transform.scale(half_heart, (half_heart.get_width() * 4, half_heart.get_height() * 4))

empty_heart = pygame.image.load("./heart_empty.png")
empty_heart = pygame.transform.scale(empty_heart, (empty_heart.get_width() * 4, empty_heart.get_height() * 4))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player.health <= 0 or len(enemies) == 0:
        screen.fill("black")
        replay.x = screen.get_width()/2 - replay.sprite.get_width()/2
        replay.y = screen.get_height()/2+replay.sprite.get_height()
        screen.blit(replay.sprite, (replay.x, replay.y))
        if replay.mouse_down():
            # TODO: Come up with a better way to reset the game
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
        pygame.display.flip()
        continue

    if player.health <= 0:
        font = pygame.font.SysFont("Comic Sans", 100)
        text = font.render("Game Over", False, (255, 255, 255)) 
        screen.blit(text, (screen.get_width()/2 - text.get_width()/2, screen.get_height()/2))
    elif len(enemies) == 0:
        font = pygame.font.SysFont("Comic Sans", 100)
        text = font.render("You Win! You defeated all the enemies!", False, (255, 255, 255)) 
        screen.blit(text, (screen.get_width()/2 - text.get_width()/2, screen.get_height()/2))

    screen.fill("purple")

    player.move(dt, map.walls)

    screen.blit(map.floors, (player.offset.x, player.offset.y))
    screen.blit(map.walls, (player.offset.x, player.offset.y))
    
    for enemy in enemies:
        enemy.move(dt, player, map.walls)
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

    if player.health == 1:
        screen.blit(half_heart, (0, 0))
    elif player.health >= 2:
        screen.blit(heart, (0, 0))

    if player.health < 3:
        screen.blit(empty_heart, (heart.get_width() + 10, 0))
    elif player.health >= 4:
        screen.blit(heart, (heart.get_width() + 10, 0))
    elif player.health == 3:
        screen.blit(half_heart, (heart.get_width() + 10, 0))

    if player.health == 6:
        screen.blit(heart, ((heart.get_width() + 10) * 2, 0))
    elif player.health == 5:
        screen.blit(half_heart, ((heart.get_width() + 10) * 2, 0))
    elif player.health < 5:
        screen.blit(empty_heart, ((heart.get_width() + 10) * 2, 0))


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
