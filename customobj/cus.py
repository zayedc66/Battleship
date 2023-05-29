#Name: Zayed
#Date: 4/14/2023
#Custom objects code

import pygame,sys
from movement import Move_Object
from background import Background
pygame.init()

#Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
done = False

#Setup of Starting objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Maze")
walls = pygame.sprite.Group()
walls.add(Background(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,'maze.png'))


font = pygame.font.SysFont('Consolas', 30)

move_pac = Move_Object(15, 10, 20, 20, 'pac.png')
move_pac_group = pygame.sprite.Group()
move_pac_group.add(move_pac)

endobj = Move_Object(470, 475, 25, 25, 'portal.png')
endobj_group = pygame.sprite.Group()
endobj_group.add(endobj)

def collision(object1, object2):
    return object1.colliderect(object2)

def display():
    global portal
    window.fill((150,150,155)) #White background
    walls.draw(window)
    move_pac_group.draw(window)
    endobj_group.draw(window)
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)  

def win():
    window.blit(font.render("You Win", True, (255,255,255)), (250, 250))
    exit = window.blit(font.render("Exit?", True, (255,255,255)), (250, 200))
    playagn = window.blit(font.render("Play Again?", True, (255,255,255)), (250, 300))
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            ## check if cursor is on button ##
            if exit.collidepoint(pos):
                pygame.quit()
                sys.exit()
            if playagn.collidepoint(pos):
                global man_y, man_x, done
                move_pac.rect.x = 15
                move_pac.rect.y =  10
                done = False
                display()


def gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT):
        spacer = 10
        font = pygame.font.SysFont('Consolas', 10)
        for gridX in range(0, WINDOW_WIDTH, spacer):        
            window.blit(pygame.transform.rotate(font.render(str(gridX), True, (0, 0, 0)),90),(gridX,0))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            window.blit(font.render(str(gridY), True, (0, 0, 0)), (0, gridY))
        for gridX in range(0, WINDOW_WIDTH, spacer):
            pygame.draw.line(window,(255,0,0),(gridX,0),(gridX,WINDOW_HEIGHT))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            pygame.draw.line(window,(255,0,0),(0,gridY),(WINDOW_WIDTH,gridY))    

display()
while True:
    display()
    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if collision(move_pac.rect, endobj.rect):
        done = True
        win()
    if done == False:    
        move_pac.key_press(3)
    if pygame.sprite.spritecollide(move_pac, walls, False, collided=pygame.sprite.collide_mask):
        move_pac.rect.x-=move_pac.movex
        move_pac.rect.y-=move_pac.movey
        display()
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw