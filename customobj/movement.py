import pygame
import sys
#custom object for copys of walls
class Wall(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,wallColor/load_path):
        super().__init__() 
        img_load = pygame.image.load(img_load) 
        self.image = pygame.transform.scale(img_load , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        