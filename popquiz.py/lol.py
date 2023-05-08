import pygame
import random

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("smash")
icon = pygame.image.load('diet.jpg')
pygame.display.set_icon(icon)

ball = pygame.image.load('coke.jpg')
ballrect = ball.get_rect()
ballrect.x = random.randrange(0, 500)
ballrect.y = random.randrange(0, 200)

def player():
    window.blit(ball, ballrect)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ballrect.collidepoint(event.pos):
                ballrect.x = random.randrange(0, 1100)
                ballrect.y = random.randrange(0, 600)

    window.fill((255, 255, 255))
    player()
    pygame.display.update()