import pygame
import player
import map

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0


player = player.Player()

map = map.Map()

img = pygame.image.load("./knight_m_idle_anim_f0.png")
img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))

background = pygame.Surface((10000, 10000))

background.fill("purple")

map.draw_map("maps/Example Map_Floors.csv", background)
map.draw_map("maps/Example Map_Walls.csv", background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    player.move(dt)
    screen.blit(background, (-player.position.x, -player.position.y))

    screen.blit(img, (screen.get_width()/2, screen.get_height()/2))

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    print(f"FPS: {int(clock.get_fps())}")

pygame.quit()
