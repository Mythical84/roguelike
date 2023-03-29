import pygame

class Tile:
    def __init__(self, tile: pygame.Surface):
        self.tile = pygame.transform.scale(tile, (tile.get_width() * 4, tile.get_height() * 4))

