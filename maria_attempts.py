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
background = pygame.image.load("/home/softdes/project-3-healthfy/Images/background.jpg")
humanoid = pygame.image.load("/home/softdes/project-3-healthfy/Images/humanoid.jpg")

# Add constants 
clock = pygame.time.Clock()
RUNNING = True
CURRENT_SCORE = 0
TIMER = pygame.USEREVENT + 1
timer_sec = 48
pygame.time.set_timer(TIMER, 1000)
font = pygame.font.SysFont(None, 100)
text = font.render(str(timer_sec), True, (0, 128, 0))
small_text = pygame.font.Font("freesansbold.ttf", 20)

def text_objects(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

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
    smallText = pygame.font.SysFont("comicsansms",10)
    text_surface, text_rectangle = text_objects("Click one of the buttoms", smallText)
    text_rectangle.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(text_surface, text_rectangle)

def action():
    pass

def score():
    pass

def health_bar():
    pygame.draw.rect(screen, green, (0, 100, 0, 0))


while RUNNING:
    screen.fill(white)
    screen.blit(background, (0, 0))
    screen.blit(humanoid, (250, 350))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == TIMER:
            timer_sec -= 1
            text = font.render(str(timer_sec), True, (0, 128, 0))
            if timer_sec == 0:
                pygame.time.set_timer(TIMER, 0)
    text_rect = text.get_rect(center = screen.get_rect().center)
    screen.blit(text, text_rect)
# Add inactive 'buttons' that change colors.
    if 44 <= timer_sec <= 46:
        pygame.draw.rect(screen, red, (300, 375, 50, 50))
    else:
        pygame.draw.rect(screen, black, (300, 375, 50, 50))
        text_surface, text_rectangle = text_objects("Talk", small_text)
        text_rectangle.center = ((300+(50/2)), 375+(50/2))
        screen.blit(text_surface, text_rectangle)
    if 40 <= timer_sec <= 42 or 30 <= timer_sec <= 35 :
        pygame.draw.rect(screen, red, (300, 315, 50, 50))
    else:
        pygame.draw.rect(screen, black, (300, 315, 50, 50))
        text_surface, text_rectangle = text_objects("Potty", small_text)
        text_rectangle.center = ((300+(50/2)), 315+(50/2))
        screen.blit(text_surface, text_rectangle)
    if 24 <= timer_sec <= 26:
        pygame.draw.rect(screen, red, (200, 375, 50, 50))
    else:
        pygame.draw.rect(screen, black, (200, 375, 50, 50))
        text_surface, text_rectangle = text_objects("Work", small_text)
        text_rectangle.center = ((200+(50/2)), 375+(50/2))
        screen.blit(text_surface, text_rectangle)
    if 15 <= timer_sec <= 20 or 28 <= timer_sec <= 30:
        pygame.draw.rect(screen, black, (100, 315, 50, 50))
    else:
        pygame.draw.rect(screen, red, (100, 315, 50, 50))
        text_surface, text_rectangle = text_objects("Sleep", small_text)
        text_rectangle.center = ((100+(50/2)), 315+(50/2))
        screen.blit(text_surface, text_rectangle)
    if 36 <= timer_sec <= 40 or 10 <= timer_sec <= 8:
        pygame.draw.rect(screen, red, (100, 375, 50, 50))
    else:
        pygame.draw.rect(screen, black, (100, 375, 50, 50))
        text_surface, text_rectangle = text_objects("Eat", small_text)
        text_rectangle.center = ((100+(50/2)), 375+(50/2))
        screen.blit(text_surface, text_rectangle)
# Add health bar visual
    pygame.draw.rect(screen, green, (0, 0, 240, 30))
    pygame.draw.rect(screen, red, (50, 0, 240, 30))
    pygame.display.flip()
    mouse = pygame.mouse.get_pos() 
pygame.display.update()
pygame.quit()