import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600)) #game window
pygame.display.set_caption("SIGMA BIRD") #game window title
clock = pygame.time.Clock() #handles FPS
font = pygame.font.Font(None, 36) #font for score
font2 = pygame.font.Font(None, 72) #larger font
bg_x1 = 0
bg_x2 = 800
xpos = 50

frameWidth = 203
frameHeight = 152
frameNum = 0
ticker = 0

pipe_image = pygame.image.load('sigmapipe.png').convert_alpha()
background_image = pygame.image.load('bonix.jpeg').convert_alpha()
birdImg = pygame.image.load('REALBLUB.png.png').convert_alpha()

score = 0 #score variable

running = True
#BIRD CLASS
class Bird:
    def __init__(self):
        self.y = 400
        self.velocity = 0
        
    def flap(self):
        self.velocity = -3 #flap
        
    def physics(self):
        self.velocity += 0.1 #gravity
        self.y += self.velocity
        
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (50, self.y, 30, 30))
#pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, 400)
        self.gap = 150 #gap size between top and bottom pipes
        self.top_pipe = pygame.transform.flip(pipe_image, False, True) #flip the pipe image for the top pipe
        self.bottom_pipe = pipe_image
        
    def move(self):
        self.x -= 2 #moves pipes to the left
        
    def draw(self):
        #calculate the top and bottom positipons
        top_height = self.height
        bottom_height = 800 - (self.height + self.gap)
        
        #draw the top pipe
        screen.blit(self.top_pipe, (self.x, top_height - self.top_pipe.get_height()))
        #draw the bottom pipe
        screen.blit(self.bottom_pipe, (self.x, self.height + self.gap))
        
def check_collision(bx, by, px, py):
    #TOP PIPE CHECK
    if bx + 30 > px and bx < px + 50 and by < py:
        return True
    #BOTTOM PIPE CHECK
    if bx + 30 > px and bx < px + 50 and by + 30 > py + 150:
        return True
    return False
        
pipes = []
spawn_pipe = 0 #timer for pipe spawn
bird = Bird()
ticker = 0
while running: #game loop-------------------------------------------------------------------------------
    clock.tick(60)
    
    ticker+=1 #increment score timer
    if ticker%10 == 0: #every 10 frames reset
        ticker = 0 #reset timer
        score += 1 #increment score
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.flap()
    bird.physics()
    
    #spawn pipes
    spawn_pipe += 1 #increment timer
    if spawn_pipe >= 150: #pipe is spawned every 150 frames
        pipes.append(Pipe(800)) #this INSTANTIATES a new pipe and puts it in the list
        spawn_pipe = 0 #reset timer
        
    #move pipes
    for pipe in pipes: #walk through list of pipes
        pipe.move() #move each pipe
        if check_collision(50, bird.y, pipe.x, pipe.height): #chechk collision with birb
            running = False #kills game if u hit a pipe
    #destroy pipes that have gone off screen
    i = len(pipes) - 1 #start at end of list
    while i >= 0:
        if pipes[i].x <= -50: #check if pipe is off screen
            pipes.pop(i) #Remove from list
        i -= 1 #this increments the while loop
    
    #render section-----------------------------------------------
    ticker+=1
    if ticker%10==0: #only change frame every 10 ticks
        frameNum+=1
    #if we are over the NUMBER of frames in our sprite reset to 0
    if frameNum>7:
        frameNum=0
    
    
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0,0))
    bg_x1 -= 2
    bg_x2 -= 2
    
    if bg_x1 <= -800:
        bg_x1 = 800
    if bg_x2 <= -800:
        bg_x2 = 800
    screen.blit(background_image, (bg_x1,0))
    screen.blit(background_image, (bg_x2,0))
    # bird.draw()
    score_text = font.render("Score:", True, (255, 255, 255))
    screen.blit(score_text, (650, 20)) #position the socre in the top right question
    score_text2 = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text2, (750, 20)) #position the socre in the top right question
    for pipe in pipes:
        pipe.draw()
    
    screen.blit(birdImg, (50, bird.y), (frameWidth*frameNum,0, frameWidth, frameHeight))
    
    pygame.display.flip()
    
# END OF GAME LOOP!!!!--------------------------------------------------------------------------------

text = font2.render("GAME OVER", True, (255, 50, 50))
screen.blit(text, (200, 200)) #positipon the socre in the top right corner
pygame.display.flip()
pygame.time.delay(2000) #delay in milliseconds


pygame.quit()

