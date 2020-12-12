import pygame, sys
import model, view
# Setup pygame/window ---------------------------------------- #
from pygame.locals import *
pygame.init()


pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)
 
font = pygame.font.SysFont(None, 20)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)
grey = (80, 80, 80)


def text_objects(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()


def button(msg,x,y,w,h,ic,ac,key=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1:
            pass        
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms", 10)
    text_surface, text_rectangle = text_objects("whatever", smallText)
    text_rectangle.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(text_surface, text_rectangle)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
def main_menu():
    click = False
    while True:
        screen.fill(white)
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button('S T A R T  G A M E', 50, 100, 200, 50, black, white)
        button('P L A Y  A S  I S A B E L L E', 50, 200, 200, 50, white, black)
        button ('P L A Y  A S  T O M', 50, 300, 200, 50, white, black)
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                tom_game()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
 
main_menu()

tom = pygame.image.load("Images/tom background.jpg")

def tom_game():
    RUNNING = True
    while RUNNING:
        screen.fill(white)
        screen.blit(tom, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            RUNNING = False
        if event.type == MOUSEBUTTONDOWN:
            button("Eat", 100, 375, 70, 50, black, green, pygame.K_e)
            button("Talk",300, 375, 70, 50, black, green, pygame.K_t)
            button("Potty",300, 315, 70, 50, black, green, pygame.K_p)
            button("Work", 200, 375, 70, 50, black, green, pygame.K_w)
            button("Sleep",100, 315, 70, 50, black, green, pygame.K_s)
        pygame.display.update()
