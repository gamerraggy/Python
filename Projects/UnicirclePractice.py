import pygame
import math

pygame.init()
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Concentric Arc Circles")

# Define colors
BLACK      = (0, 0, 0)
red        = (255, 0, 0)
orange     = (255, 165, 0)
yellow     = (255, 255, 0)
chartreuse = (127, 255, 0)
green      = (0, 255, 0)
cyan       = (0, 255, 255)
blue       = (0, 0, 255)
purple     = (160, 32, 240) 
magenta    = (255, 0, 255)
rose       = (255, 105, 180)
maroon     = (128, 0, 0)
teal       = (0, 128, 128)

# Fill background with black
screen.fill(BLACK)

# Inner Circle
pygame.draw.arc(screen, orange,     (200, 150, 400, 400), math.pi/2,     math.pi,      12)
pygame.draw.arc(screen, red,     (200, 150, 400, 400), 0, math.pi/2,      12)
pygame.draw.arc(screen, yellow,     (200, 150, 400, 400), math.pi, 3*math.pi/2,      12)
pygame.draw.arc(screen, green,     (200, 150, 400, 400), 3*math.pi/2, 0,      12)

# Middle Circle 
pygame.draw.arc(screen, purple,  (180, 130, 440, 440), 7*math.pi/4,  9*math.pi/4,  12)
pygame.draw.arc(screen, blue,  (180, 130, 440, 440), 5*math.pi/4,  7*math.pi/4,  12)
pygame.draw.arc(screen, cyan,  (180, 130, 440, 440), 3*math.pi/4,  5*math.pi/4,  12)
pygame.draw.arc(screen, green,  (180, 130, 440, 440), 1*math.pi/4,  3*math.pi/4,  12)

# Outer Circle 
pygame.draw.arc(screen, red,        (160, 110, 480, 480), 0,            math.pi/6,      12)
pygame.draw.arc(screen, teal,        (160, 110, 480, 480),11*math.pi/6 ,        0,      12)
pygame.draw.arc(screen, maroon,        (160, 110, 480, 480),  5*math.pi/3, 11*math.pi/6 ,    12)
pygame.draw.arc(screen, rose,        (160, 110, 480, 480),  3*math.pi/2, 5*math.pi/3 ,    12)
pygame.draw.arc(screen, magenta,    (160, 110, 480, 480), 4*math.pi/3,  3*math.pi/2,    12)
pygame.draw.arc(screen, purple,    (160, 110, 480, 480), 7*math.pi/6,  4*math.pi/3,    12)
pygame.draw.arc(screen, blue,    (160, 110, 480, 480), math.pi,  7*math.pi/6,    12)
pygame.draw.arc(screen, cyan,    (160, 110, 480, 480), 5*math.pi/6,  math.pi,    12)
pygame.draw.arc(screen, green,    (160, 110, 480, 480), 2*math.pi/3,  5*math.pi/6,    12)
pygame.draw.arc(screen, chartreuse,    (160, 110, 480, 480), math.pi/2,  2*math.pi/3,    12)
pygame.draw.arc(screen, yellow,    (160, 110, 480, 480), math.pi/3,  math.pi/2,    12)
pygame.draw.arc(screen, orange,    (160, 110, 480, 480), math.pi/6,  math.pi/3,    12)

pygame.display.flip()

# Main loop to keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
