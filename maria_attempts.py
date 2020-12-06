import time
import pygame

# Step 1: Initialize Game Screen.
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Healthfy')

# Add colors.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)

# Add background.
background = pygame.image.load("/home/mcardoso/project-3-healthfy/Images/background.jpg")
humanoid = pygame.image.load("/home/mcardoso/project-3-healthfy/Images/humanoid.jpg")
clock = pygame.time.Clock()
RUNNING = True
CURRENT_SCORE = 0
TIMER = pygame.USEREVENT + 1
timer_sec = 240
pygame.time.set_timer(TIMER, 1000)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects("Click one of the buttoms", smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def action():
    pass 

def score():
     pass

while RUNNING:
    # clock.tick(240)
    screen.fill(white)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == TIMER:
            if timer_sec > 0:
                timer_text = pygame.font.Font("04B_19__.ttf", 38).render('00:%02d' % timer_sec, True, black)
            else:
                pygame.time.set_timer(TIMER, 0)
        # Add inactive 'buttons' 
    pygame.draw.rect(screen, (0, 0, 0), (300, 375, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (300, 315, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (200, 375, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (100, 315, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (100, 375, 50, 50))
    pygame.display.flip()
pygame.display.update()
pygame.quit()