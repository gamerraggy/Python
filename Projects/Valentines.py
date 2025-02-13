import pygame

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Valentine's Day Card")
screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font('freesansbold.ttf', 32)
img = pygame.image.load("dog3.jpg")
img2 = pygame.image.load("dog4.jpg")
RED = (255, 0, 0)
ORANGE = (255, 98,0)
class Heart:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, surface):
        left_circle_center = (self.x - 20, self.y)
        right_circle_center = (self.x + 20, self.y)
        triangle_points = [(self.x - 40, self.y + 5),
                           (self.x + 40, self.y + 5),
                           (self.x, self.y + 50)]
        
        pygame.draw.circle(surface, self.color, left_circle_center, 20)
        pygame.draw.circle(surface, self.color, right_circle_center, 20)
        pygame.draw.polygon(surface, self.color, triangle_points)

class Flower:
    def __init__(self,x,y,color):
            self.x = x
            self.y = y
            self.color = color

    def draw(self, surface):
        center_circle = (self.x , self.y -20)
        petal1 = (self.x + 20, self.y)
        petal2 = (self.x + 20, self.y - 40)
        petal3 = (self.x - 20, self.y)
        petal4 = (self.x - 20, self.y - 40)

        pygame.draw.circle(surface, (RED), (petal1), 20) 
        pygame.draw.circle(surface, (RED), (petal2), 20) 
        pygame.draw.circle(surface, (RED), (petal3), 20) 
        pygame.draw.circle(surface, (RED), (petal4), 20)
        pygame.draw.circle(surface, (ORANGE), (center_circle), 20) 

# Create instances of Heart
heart1 = Heart(100, 200, (250, 0, 0))
heart2 = Heart(300, 200, (250, 0, 0))  # You can ask students to change positions and colors
heart3 = Heart(500, 200, (250, 0, 0))  # You can ask students to change positions and colors
heart4 = Heart(700, 200, (250, 0, 0))  # You can ask students to change positions and colors

flower1 = Flower(100, 350, (250, 250, 0))
flower2 = Flower(400, 350, (250, 250, 0))
flower3 = Flower(700, 350, (250, 250, 0))
# Draw everything
heart1.draw(screen)
heart2.draw(screen)
heart3.draw(screen)
heart4.draw(screen)

flower1.draw(screen)
flower2.draw(screen)
flower3.draw(screen)

text1 = font.render('I Love You!', True, (250, 100, 100))
text2 = font.render('Happy Valentines Day', True, (250, 0, 0), (200, 150, 150))
screen.blit(text1, (200, 100))
screen.blit(text2, (400, 500))
screen.blit(img, (0, 400))
screen.blit(img2, (500, 550))

pygame.display.flip()
pygame.time.wait(5000)
