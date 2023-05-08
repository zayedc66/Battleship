#Pop-quiz
#Made by Zayed
#5 / 4 / 2023

import pygame,sys
pygame.init()

#Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


#Setup of Starting objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Smash the coke")
img_coke = pygame.image.load('coke.jpg') #with .png or .jpb included in the name
img_coke = pygame.transform.scale(img_coke, (75, 75))  #resize image Where 35 ,35 is the size, (x,y)
font = pygame.font.SysFont('Consolas', 30)
king_x=10
king_y=10


def wack():
    window.blit(font.render("You Win", True, (255,255,255)), (250, 250))
    exit = window.blit(font.render("Exit?", True, (0,0,0)), (250, 200))
    no1 = window.blit(font.render("Play Again?", True, (255,255,255)), (250, 300))
    playagn = window.blit(font.render("Play Again?", True, (0,0,0)), (300, 300))
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            ## check if cursor is on button ##
            if playagn.collidepoint(pos):
                display()
            if exit.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
            if pass:
                    (True, (king_x, king_y))
            display()
            if no1.collidepoint(pos):
                king_x=500
                king_y=500
                
def display():
    global objects, no1
    window.fill((255,255,255)) #White background
    object_draw_name=pygame.draw.rect(window,(6,57,112),(10,490,500,10)) #BORDER
    object_draw_name2=pygame.draw.rect(window,(6,57,112),(0,0,10,500))  #BORDER
    object_draw_name10=pygame.draw.rect(window,(6,57,112),(0,0,500,10)) #BORDER
    object_draw_name8=pygame.draw.rect(window,(6,57,112),(490, 10,500,500)) #BORDER
    no1=window.blit(img_coke,(king_x, king_y))
    '''no2=window.blit(img_coke,(150, 100))
    no3=window.blit(img_coke,(250, 100))
    no4=window.blit(img_coke,(350, 100))
    no5=window.blit(img_coke,(50, 230))
    no6=window.blit(img_coke,(150, 230))
    no7=window.blit(img_coke,(250, 230))
    no8=window.blit(img_coke,(350, 230))
    coke = [no1,no2,no3,no4,no5,no6,no7,no8]'''
    objects=[object_draw_name, object_draw_name2, object_draw_name10, object_draw_name8]    
display()

while True:
    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
   # dic name--True=1----False=0----->Creating a dictionary that takes a true and false and retuns a 1 and 0 respectively
        t_f_list = {True : 1, False: 0}
        #value name---pygame check if keys down---->Create a variable that is set to all the key values to see if it is up or down via True and False respectively
        key_input = pygame.key.get_pressed()
        #x-var---dic name-value name-----key Left---speed value--dic name-value name------key Right---speed value  
    wack()    
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
    
