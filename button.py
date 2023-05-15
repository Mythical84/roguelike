import pygame

class Button:
    def __init__(self, sprite):
        self.sprite = pygame.image.load(sprite)
        self.mouse_pressed = False
        self.x = 0
        self.y = 0

    def hover(self):
        if pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height()).collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def mouse_down(self):
        if self.hover() and self.mouse_pressed and not pygame.mouse.get_pressed()[0]:
            self.mouse_pressed = False

        if self.hover() and pygame.mouse.get_pressed()[0] and not self.mouse_pressed:
            self.mouse_pressed = True
            return True
        return False

    def mouse_release(self):
        if self.hover() and self.mouse_pressed and not pygame.mouse.get_pressed()[0]:
            self.mouse_pressed = False
            return True
        return False
