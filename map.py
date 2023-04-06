import csv
import pygame
import os
from enemies import enemy

class MapLoader:
    def __init__(self):
        self.maps = {}
        self.tiles = []
        self.tilesheet = pygame.image.load("./0x72_DungeonTilesetII_v1.4.png")
        self.tilesheet = pygame.transform.scale(self.tilesheet, (self.tilesheet.get_width() * 4, self.tilesheet.get_height() * 4))
        for height in range(0, self.tilesheet.get_height(), 64):
            for width in range(0, self.tilesheet.get_width(), 64):
                self.tiles.append(pygame.Rect(width, height, 64, 64))

        for map in os.listdir("./maps"):
            self.maps[map] = {}
            for layer in os.listdir(f"./maps/{map}"):
                self.load_layer(map, layer)


    def load_layer(self, map, layer):
        with open(f"./maps/{map}/{layer}") as f:
            reader = csv.reader(f)
            m = []
            for r in reader:
                m.append(r)
            
            # the string cutting is grabbing what type of layer the file is
            # its cutting the file name so that only the layer type remains
            self.maps[map][layer[len(map) + 1:][::-1][4:][::-1]] = m

    
    def draw_map(self, map, floor, wall, enemies):
        for y in range(0, len(self.maps[map]["Floors"])):
            for x in range(0, len(self.maps[map]["Floors"][y])):
                x_pos = (x * 64)
                y_pos = (y * 64)
                floor.blit(self.tilesheet, (x_pos, y_pos), self.tiles[int(self.maps[map]["Floors"][y][x])])
                
        for y in range(0, len(self.maps[map]["Walls"])):
            for x in range(0, len(self.maps[map]["Walls"][y])):
                x_pos = (x * 64)
                y_pos = (y * 64)
                wall.blit(self.tilesheet, (x_pos, y_pos), self.tiles[int(self.maps[map]["Walls"][y][x])])

        # TODO: enemy loader

class MapGenerator:
    def __init__(self):
        loader = MapLoader()
        self.floors = pygame.Surface((10000, 10000))
        self.walls = pygame.Surface((10000, 10000)).convert_alpha()
        self.enemies = []

        self.walls.fill([0, 0, 0, 0])

        loader.draw_map("Example Map", self.floors, self.walls, self.enemies)
