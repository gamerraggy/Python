
import pygame

pygame.init()
screen = pygame.display.set_mode((1200,800)) #screen is a rectangle, not square!
pygame.display.set_caption("fish mouse imput")

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
chest = 1
clam = 1
ticker = 0

#load in the image and make transparent
chestImg1 = pygame.image.load("chest1.jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg1, [255,0,255])
#load in the image and make transparent
chestImg2 = pygame.image.load("chest2.jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg2, [255,0,255])

clamtop = pygame.image.load("Clamtop.png").convert_alpha()
pygame.Surface.set_colorkey (clamtop, [255,0,255])
#load in the image and make transparent
clambottom = pygame.image.load("Clambottom.png").convert_alpha()
pygame.Surface.set_colorkey (clambottom, [255,0,255])


while 1: #game loop###########################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        print(mousePos) #this is to help you know where to set these boundaries
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #check if you've clic  ked on the chest
            if mousePos[0]>238 and mousePos[0] < 355 and mousePos[1]>130 and mousePos[1]<230:
               chest = 2
            #check if you've clicked on the clam
            if mousePos[0]>598  and mousePos[0] < 718 and mousePos[1]>300 and mousePos[1]<420:
               clam = 2
        if event.type == pygame.MOUSEBUTTONUP:
            clam = 1
            chest = 1

        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos        
    
    #update/physics section----------------------

    #keep chest open for 50 game loops:
   

    #render section------------------------------
    
    screen.fill((0,0,180))# Clear the screen
    
    #draw background image
    if chest == 1:
        screen.blit(chestImg1, (240, 140))
    elif chest ==2: 
        screen.blit(chestImg2, (240, 140))

    if clam == 1:
        screen.blit(clamtop, (600, 300))
    elif clam ==2: 
        screen.blit(clambottom, (600, 300))
    
    pygame.display.flip()# Update the display

#end of game loop###################################################################
pygame.quit()

#invest in ewancoin™
