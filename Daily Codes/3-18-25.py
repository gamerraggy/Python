import pygame
import random
pygame.init()  
pygame.display.set_caption("snowfall")  # sets the window title
screen = pygame.display.set_mode((500, 500))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

#----------------------------class snowflake------------------------------------------
class Snowflake:
    #constructor for class snowflake
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
    def move(self):
        #self.xpos += random.randrange(-2, 3) #makes the snowflake move a random amount left or right
        self.ypos -= random.randrange(0, 3) #makes the snowflake move a random amount up or down
        if self.ypos == 0:
            self.ypos = random.randrange(499, 500) #resets the snowflake's position to the top of the screen once it's reached the bottom

    def draw(self):
        pygame.draw.circle(screen, (176, 255, 247), (self.xpos, self.ypos), 5) #draw flakes

#----------------------------------------------------------------------


#create a bunch of snowflakes
flakeBag = [] #list to hold a bunch of snowflake objects
for i in range(500):
    flakeBag.append(Snowflake(random.randrange(0, 500), random.randrange(0, 500)))#creates a snowflake and puts it in the list


while(1): #omg game lup---------
    clock.tick(60) #FPS
    
    #physics section----
    
    #move flakes
    for i in range(len(flakeBag)):
        flakeBag[i].move()
         
                      

    #render section---
    screen.fill((0,0,0))
    
    for i in range(len(flakeBag)):
        flakeBag[i].draw() #draws every snowflake in the list

 
    
    pygame.display.flip()#this actually puts the pixel on the screen
   
pygame.quit()
