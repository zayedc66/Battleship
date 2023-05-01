import pygame 
import sys
#custom object for copys of walls 
class Background(pygame.sprite.Sprite):
    def _init_(self, startx, startY ,width, height, load_path):
        super()._init_()
        img_load = pygame. image.load(load_path)
        self.image = pygame.transform.scale(img_load, (width, height)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startx, startY))
    