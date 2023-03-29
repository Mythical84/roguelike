import pygame
import player

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0


player = player.Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    player.move(dt)
    img = pygame.image.load("./knight_m_idle_anim_f0.png")
    img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))

    screen.blit(img, (player.position.x, player.position.y))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
