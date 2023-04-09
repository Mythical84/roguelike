import pygame

class Animator:
    def __init__(self, object):
        self.object = object
        self.animations = {}
        self.current_animation = {}
        self.current_frame = 0
        self.frame_update = -1
        self.flip_frames = False

    def add_animation(self, frames, fps, name):
        for i in range(0, len(frames)):
            frames[i] = pygame.transform.scale(frames[i], (frames[i].get_width() * 4, frames[i].get_height() * 4))
        self.animations[name] = {"frames": frames, "fps": fps, "name": name}

    def set_animation(self, name):
        self.current_animation = self.animations[name]
        self.current_frame = 0

    def get_animation(self):
        return self.current_animation.get("name", None)

    def update_animation(self):
        if self.current_animation == {}:
            return
        if self.frame_update == -1:
            self.frame_update = pygame.time.get_ticks() + 1000/self.current_animation["fps"]
        if pygame.time.get_ticks() >= self.frame_update:
            frame = self.current_animation["frames"][self.current_frame]
            if self.flip_frames:
                self.object.sprite = pygame.transform.flip(frame, True, False)
            else:
                self.object.sprite = frame
            self.current_frame += 1
            if self.current_frame > len(self.current_animation["frames"])-1:
                self.current_frame = 0
            self.frame_update = -1

    def flip_animation(self, flip_animation):
        self.flip_frames = flip_animation
