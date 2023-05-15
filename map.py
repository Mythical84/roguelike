import csv
import pygame
import os
import random
import json
from enemies import orc_warrior

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
                filename, extension = os.path.splitext(layer)
                if extension == ".csv":
                    self.load_layer(map, layer)
                else:
                    with open(f"./maps/{map}/map_data.json") as f:
                        text = ""
                        for line in f.readlines():
                            text += line.strip()
                        self.maps[map]["map_data"] = json.loads(text)

    def load_layer(self, map, layer):
        with open(f"./maps/{map}/{layer}") as f:
            reader = csv.reader(f)
            m = []
            for r in reader:
                m.append(r)
            
            # the string cutting is grabbing what type of layer the file is
            # its cutting the file name so that only the layer type remains
            self.maps[map][layer[len(map) + 1:][::-1][4:][::-1]] = m

    
    def draw_map(self, map, floor, wall, enemies, x_offset, y_offset, nearby_rooms):
        print(nearby_rooms)
        for y in range(0, len(self.maps[map]["Floors"])):
            for x in range(0, len(self.maps[map]["Floors"][y])):
                x_pos = (x * 64) + x_offset
                y_pos = (y * 64) + y_offset
                floor.blit(self.tilesheet, (x_pos, y_pos), self.tiles[int(self.maps[map]["Floors"][y][x])])
                
        for y in range(0, len(self.maps[map]["Walls"])):
            for x in range(0, len(self.maps[map]["Walls"][y])):
                x_pos = (x * 64) + x_offset
                y_pos = (y * 64) + y_offset - 64
                if (y == 0 or y == 1) and (x == 14 or x == 15 or x == 16 or x == 17) and nearby_rooms[0]:
                    continue
                if (y == len(self.maps[map]["Walls"]) - 1 or y == len(self.maps[map]["Walls"]) - 2) and (x == 14 or x == 15 or x == 16 or x == 17) and nearby_rooms[3]:
                    continue
                if (x == 0 or x == 1) and (y == 9 or y == 10 or y == 11 or y == 12) and nearby_rooms[1]:
                    continue
                if (x == len(self.maps[map]["Walls"][y]) - 1 or x == len(self.maps[map]["Walls"][y]) - 2) and (y == 9 or y == 10 or y == 11 or y == 12) and nearby_rooms[2]:
                    continue

                # Stop the top tan part of the wall from drawing if there is a room above, making a more seemless transition between rooms
                if y == 0 and nearby_rooms[0]:
                    continue
                wall.blit(self.tilesheet, (x_pos, y_pos), self.tiles[int(self.maps[map]["Walls"][y][x])])

        e = enemies
        for y in range(0, len(self.maps[map]["Enemies"])):
            for x in range(0, len(self.maps[map]["Enemies"][y])):
                if self.maps[map]["Enemies"][y][x] == "439":
                    x_pos = (x*64) + x_offset
                    y_pos = (y*64) + y_offset
                    e.append(orc_warrior.OrcWarrior(x_pos,y_pos))

        return e

class MapDrawer:
    def __init__(self):
        loader = MapLoader()
        generator = MapGenerator()
        self.floors = pygame.Surface((10000, 10000))
        self.walls = pygame.Surface((10000, 10000)).convert_alpha()
        self.enemies = []

        self.walls.fill([0, 0, 0, 0])

        current_map = "Example Map"

        y_offset = 0
        for i in range(0, 25):
            data = loader.maps[current_map]["map_data"]
            x_offset = (i%5) * data["width"] * 64
            if (i+1)%5 == 1 and i != 0:
                y_offset += data["height"] * 64
            if generator.map[i] != 0:
                # up, left, right, down
                nearby_rooms = [False, False, False, False]
                rooms = [-5, -1, 1, 5]
                for r in rooms:
                    try: 
                        if generator.map[i+r] != 0:
                            nearby_rooms[rooms.index(r)] = True
                    except:
                        pass
                self.enemies = loader.draw_map(current_map, self.floors, self.walls, self.enemies, x_offset+(5000 - (64 * 30 * 2)), y_offset+5000 - (64 * 18 * 2), nearby_rooms)


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
