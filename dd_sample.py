
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
background = pygame.image.load("Images/background.jpg")
humanoid = pygame.image.load("Images/humanoid.jpg")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
timer_sec = 10
text = font.render(str(timer_sec), True, (0, 128, 0))
RUNNING = True
CURRENT_SCORE = 0
TIMER = pygame.USEREVENT + 1
score_value = 0

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

def display_score(x, y):
    score = font.render("Score : " + str(score_value), True, green)
    screen.blit(score, (x, y))

def update_score(score, high_score):
	if score > high_score:
		high_score = score
	return high_score

while RUNNING:
    clock.tick(60)
    screen.fill(white)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == TIMER:
            timer_sec -= 1
            text = font.render(str(timer_sec), True, (0, 128, 0))
            if timer_sec == 0:
                pygame.time.set_timer(TIMER, 0)
                # display_score(10,10)
                # pygame.display.update() 
                print("Score equals 0")
   
    text_rect = text.get_rect(center = screen.get_rect().center)
    screen.blit(text, text_rect)
    
        # Add inactive 'buttons' 
    pygame.draw.rect(screen, black, (300, 375, 50, 50))
    pygame.draw.rect(screen, black, (300, 315, 50, 50))
    pygame.draw.rect(screen, black, (200, 375, 50, 50))
    pygame.draw.rect(screen, black, (100, 315, 50, 50))
    pygame.draw.rect(screen, black, (100, 375, 50, 50))
    pygame.display.flip()
   
pygame.display.update()
pygame.quit()