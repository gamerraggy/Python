#import the pygame library and initisalise the game engine
import pygame
import random
pygame.init()

#open a new window, caption it "Pong"
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("pong")

# heres the variable that runs our game loop
doExit = False

# the clock will used to control how fast the screen updates
clock = pygame.time.Clock()

#variables to hold paddle position
#these go above the game loop
p1x = 350
p1y = 475
p1Score = 0
hp = 3
#ball variables---------------------------------------------
ball_x = 350 #xposition
ball_y = 0 #yposition
ball_size = 15
bVx = 5 #x velocity (horizontal speed)
bVy = 5 #y velocity (vertical speed)

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100,250),random.randrange(100,250), random.randrange(100,250))
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50))
    def collide(self, ball_x, ball_y):
        if not self.isDead:
            if (ball_x + ball_size > self.xpos and
                ball_x < self.xpos + 100 and #width of brick is 100
                ball_y + ball_size > self.ypos and
                ball_y < self.ypos + 50): #heigh of brick is 50
                self.isDead = True
                return True
            return False
        
brick1 = brick(50,50)
brick2 = brick(200,50)
brick3 = brick(350,50)
brick4 = brick(500,50)
brick5 = brick(50,150)
brick6 = brick(200,150)
brick7 = brick(350,150)
brick8 = brick(500,150)

while not doExit: #GAME LOOP-------------------------
    
    # event queue stuff ---------------
    clock.tick(60) #set the fps
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
       
#game logic will go here --------------------------
       
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p1x-=5
    if keys[pygame.K_d]:
        p1x+=5

        
    #ball movement
    ball_x += bVx
    ball_y += bVy
       
    
        #reflect ball off sidewalls of screen
    if ball_x < 0 or ball_x + 20 > 700:
        bVx *= -1      
           
    if ball_y < 0:
        bVy *= -1
        
    if ball_y + 20 > 500:
        hp -= 1
        ball_y = p1x and p1y - 250
        if hp == 0:
            pygame.quit()
    
        
    #ball paddle reflection
    if ball_x < p1x + 125 and ball_y + 10 > p1y and ball_x > p1x - 10:
        bVy *= -1
        print("paddle hit")
    
    if brick1.collide(ball_x, ball_y):
        bVy *= -1
        
    if brick2.collide(ball_x, ball_y):
        bVy *= -1
    
    if brick3.collide(ball_x, ball_y):
        bVy *= -1
        
    if brick4.collide(ball_x, ball_y):
        bVy *= -1
   
    if brick5.collide(ball_x, ball_y):
        bVy *= -1
        
    if brick6.collide(ball_x, ball_y):
        bVy *= -1
    
    if brick7.collide(ball_x, ball_y):
        bVy *= -1
        
    if brick8.collide(ball_x, ball_y):
        bVy *= -1   
         

     # render section -----------------------------------------
     
    screen.fill((130, 18, 24)) 
           
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 125, 10), 50)
    
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_size)
    
    brick1.draw()
    brick2.draw()
    brick3.draw()
    brick4.draw()
    brick5.draw()
    brick6.draw()
    brick7.draw()
    brick8.draw()
    
           # updates the screen
           
           #display scores
    font = pygame.font.Font(None, 74) #use default fontwwwwwws
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (325,10))
    
    font = pygame.font.Font(None, 74) #use default fontwwwwwws
    text = font.render(str(hp), 1, (255, 255, 255))
    screen.blit(text, (10,10))
           
    #changes the score 
    if ball_y > 480:
        bVx *= -1
        p1Score += 1
    

           
    pygame.display.flip() #flips memory to screen
    


    #end game loop ----------------------------------------
           
pygame.quit() # when game is done close down pygame
