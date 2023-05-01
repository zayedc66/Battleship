#Name: Zayed
#Date: 4/14/2023
#Custom objects code

import pygame,sys
from movement import Move_Object
pygame.init()

#Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


#Setup of Starting objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Maze")
move_pac = Move_Object(100, 100, 35, 35, 'pac.png')
move_portal = Move_Object(100, 100, 35, 35, 'portal.gif')
move_pac_group = pygame.sprite.Group()
move_pac_group.add(move_pac)
font = pygame.font.SysFont('Consolas', 30)
speed=3
done = False


def collision(object1, object2):
    return object1.colliderect(object2)


def display():
    global objects, pac, portal
    window.fill((0,0,0)) #White background
    object_draw_name=pygame.draw.rect(window,(6,57,112),(10,490,500,10)) #BORDER
    object_draw_name2=pygame.draw.rect(window,(6,57,112),(0,0,10,500))  #BORDER
    object_draw_name10=pygame.draw.rect(window,(6,57,112),(0,0,500,10)) #BORDER
    object_draw_name8=pygame.draw.rect(window,(6,57,112),(490, 10,500,500)) #BORDER
    object_draw_name3=pygame.draw.rect(window,(6,57,112),(140,10,10,100))
    object_draw_name4=pygame.draw.rect(window,(6,57,112),(10,100,80,10))
    object_draw_name5=pygame.draw.rect(window,(6,57,112),(90,60,10,50))
    object_draw_name6=pygame.draw.rect(window,(6,57,112),(50,50,50,10))
    object_draw_name7=pygame.draw.rect(window,(6,57,112),(10,140,290,10))
    object_draw_name9=pygame.draw.rect(window,(6,57,112),(150,100,100,10))
    object_draw_name11=pygame.draw.rect(window,(6,57,112),(250, 10,10,100))
    object_draw_name12=pygame.draw.rect(window,(6,57,112),(200,180,450,10))
    object_draw_name13=pygame.draw.rect(window,(6,57,112),(300,50,10,100))
    object_draw_name14=pygame.draw.rect(window,(6,57,112),(350,50,10,100))
    object_draw_name15=pygame.draw.rect(window,(6,57,112),(360, 140,500, 10))
    object_draw_name16=pygame.draw.rect(window,(6,57,112),(410,50,500,10))
    object_draw_name17=pygame.draw.rect(window,(6,57,112),(190,180,10,100))
    object_draw_name18=pygame.draw.rect(window,(6,57,112),(190,280,200,10))
    object_draw_name19=pygame.draw.rect(window,(6,57,112),(380,240,10,50))
    object_draw_name20=pygame.draw.rect(window,(6,57,112),(435,230,10,400))
    object_draw_name21=pygame.draw.rect(window,(6,57,112),(10,180,130,10))
    object_draw_name22=pygame.draw.rect(window,(6,57,112),(140, 180, 10,150))
    object_draw_name23=pygame.draw.rect(window,(6,57,112),(140,330,190,10))
    object_draw_name24=pygame.draw.rect(window,(6,57,112),(380,330,10,160))
    object_draw_name25=pygame.draw.rect(window,(6,57,112),(330, 330,10,120))
    object_draw_name26=pygame.draw.rect(window,(6,57,112),(180,440,150,10))
    object_draw_name27=pygame.draw.rect(window,(6,57,112),(170, 340,10,110))
    object_draw_name28=pygame.draw.rect(window,(6,57,112),(70,230,10,400))
    object_draw_name29=pygame.draw.rect(window,(6,57,112),(240,230,150,10))
    move_pac_group.draw(window)
    objects=[object_draw_name, object_draw_name2, object_draw_name3, object_draw_name4, object_draw_name5,
            object_draw_name6, object_draw_name7, object_draw_name8, object_draw_name9, object_draw_name10,
            object_draw_name11, object_draw_name12, object_draw_name13, object_draw_name14, object_draw_name15,
            object_draw_name16, object_draw_name17, object_draw_name18, object_draw_name19, object_draw_name20,
            object_draw_name21, object_draw_name22, object_draw_name23, object_draw_name24, object_draw_name25,
            object_draw_name26, object_draw_name27, object_draw_name28, object_draw_name29] 
       
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
                global king_y, king_x, done
                king_x=10
                king_y=10
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
    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    move_pac.key_press(5)     
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw