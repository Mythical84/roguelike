import csv
import pygame

from tile import Tile

class Map:
    def __init__(self):
        self.maps = {}
        self.tiles = []
        self.tilesheet = pygame.image.load("./0x72_DungeonTilesetII_v1.4.png")
        self.tilesheet = pygame.transform.scale(self.tilesheet, (self.tilesheet.get_width() * 4, self.tilesheet.get_height() * 4))
        for height in range(0, self.tilesheet.get_height(), 64):
            for width in range(0, self.tilesheet.get_width(), 64):
                self.tiles.append(pygame.Rect(width, height, 64, 64))


        with open("maps/Example Map_Walls.csv") as f:
            reader = csv.reader(f)
            self.example_walls = []
            for r in reader:
                self.example_walls.append(r)

    def load_map(self, map):
        print("map loaded")
        with open(map) as f:
            reader = csv.reader(f)
            m = []
            for r in reader:
                m.append(r)

            self.maps[map] = m

    
    def draw_map(self, map, screen): 
        if map not in self.maps.keys():
            self.load_map(map)
        
        for y in range(0, len(self.maps[map])):
            for x in range(0, len(self.maps[map][y])):
                x_pos = (x * 64)
                y_pos = (y * 64)
                screen.blit(self.tilesheet, (x_pos, y_pos), self.tiles[int(self.maps[map][y][x])])
