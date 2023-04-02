import pygame

class Tile:
    def __init__(self, tile: pygame.Surface, x, y):
        self.tile = pygame.transform.scale(tile, (tile.get_width() * 4, tile.get_height() * 4))
        self.x = x
        self.y = y

    def attach_animator(self, animator):
        self.animator = animator
        animator.set_tile()

    def set_tile(self, tile: pygame.Surface):
        self.tile = pygame.transform.scale(tile, (tile.get_width() * 4, tile.get_height() * 4))
