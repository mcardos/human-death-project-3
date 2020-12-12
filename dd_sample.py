import pygame
from pygame.locals import *
import time
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((500, 500))
sysfont = pygame.font.get_default_font() # the type of font to use freesansbold.ttf
font = pygame.font.SysFont(None, 50)

class Healthfyview:

    def feed_text():
        sleep_font = pygame.font.SysFont('chalkduster.ttf', 50)
        sleep_img = sleep_font.render('The Humanoid is eating', True, RED)
        screen.blit(sleep_img, (20, 40))

    def sleep_text():
        sleep_font = pygame.font.SysFont('chalkduster.ttf', 50)
        sleep_img = sleep_font.render('The Humanoid is sleeping', True, RED)
        screen.blit(sleep_img, (20, 80))

    def work_text():
        sleep_font = pygame.font.SysFont('chalkduster.ttf', 50)
        sleep_img = sleep_font.render('The Humanoid is working', True, RED)
        screen.blit(sleep_img, (20, 120))
    
    def socialize_text():
        sleep_font = pygame.font.SysFont('chalkduster.ttf', 50)
        sleep_img = sleep_font.render('The Humanoid is having fun', True, RED)
        screen.blit(sleep_img, (20, 160))
    
    def potty_text():
        sleep_font = pygame.font.SysFont('chalkduster.ttf', 50)
        sleep_img = sleep_font.render('The Humanoid is pooping', True, RED)
        screen.blit(sleep_img, (20, 200))

running = True
background = pygame.image.load("Images/background.jpg")

view = Healthfyview
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(WHITE)
    screen.blit(background, (0,0))
    view.feed_text()
    view.sleep_text()
    view.work_text()
    view.socialize_text()
    view.potty_text()
    pygame.display.update()

pygame.quit()