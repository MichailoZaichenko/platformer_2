from os import walk
import pygame

def import_folder(path):
    surface_list = []
    
    for _,__,img_files in walk(path):
        for img in img_files:  
            full_path = path + '/' + img
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)

    return surface_list

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == 'jump':
            self.frames = import_folder('./assets/dust_particles/jump')
        if type == 'land':
            self.frames = import_folder('./assets/dust_particles/land')
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift