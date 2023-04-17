import csv
import pygame
import os
import random

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

    
    def draw_map(self, map, floor, wall, enemies, x_offset, y_offset):
        for y in range(0, len(self.maps[map]["Floors"])):
            for x in range(0, len(self.maps[map]["Floors"][y])):
                x_pos = (x * 64) + x_offset
                y_pos = (y * 64) + y_offset
                floor.blit(self.tilesheet, (x_pos, y_pos), self.tiles[int(self.maps[map]["Floors"][y][x])])
                
        for y in range(0, len(self.maps[map]["Walls"])):
            for x in range(0, len(self.maps[map]["Walls"][y])):
                x_pos = (x * 64) + x_offset
                y_pos = (y * 64) + y_offset
                wall.blit(self.tilesheet, (x_pos, y_pos), self.tiles[int(self.maps[map]["Walls"][y][x])])

        # TODO: enemy loader

class MapDrawer:
    def __init__(self):
        loader = MapLoader()
        generator = MapGenerator()
        self.floors = pygame.Surface((10000, 10000))
        self.walls = pygame.Surface((10000, 10000)).convert_alpha()
        self.enemies = []

        self.walls.fill([0, 0, 0, 0])

        y_offset = 0
        for i in range(0, 25):
            x_offset = (i%5) * 30 * 64
            if (i+1)%5 == 1 and i != 0:
                y_offset += 20 * 64
            if generator.map[i] != 0:
                loader.draw_map("Example Map", self.floors, self.walls, self.enemies, x_offset, y_offset)



class MapGenerator:
    def __init__(self):
        self.map = []
        for i in range(0, 25):
            self.map.append(0)
        index = 12
        self.map[index] = 3

        self.generate_map(index, 2)

        for i in range(1, 26):
            print(f"{self.map[i-1]}, ", end="")
            if i%5 == 0:
                print()

    def generate_map(self, index, num):
        if num == 0:
            return

        for i in [-5, -1, 1, 5]:
            r = random.randint(0,4)
            if r != 0 and self.map[index+i] == 0:
                self.map[index+i] = num
                self.generate_map(index+i, num-1)
