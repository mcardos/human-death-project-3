import view, model
import pygame
import sys

model = model.HealthfyModel()
view = view.HealthfyView(model)

# Step 1: Initialize Game Screen.
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Healthfy')

# Add colors.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)
grey = (80, 80, 80)

# Add background.
background = pygame.image.load("Images/background.jpg")
humanoid = pygame.image.load("Images/humanoid.jpg")
isabelle = pygame.image.load("Images/isabele background small.jpg")
tom = pygame.image.load("Images/tom background.jpg")

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
large_text = pygame.font.SysFont("comicsans.ttf", 115)
MENU_TEXT = pygame.font.SysFont("freesansbold.ttf", 170)

def main_menu_setup():
    pygame.mouse.get_pos()
    text_surface, text_rectangle = text_objects('HEALTHFY', MENU_TEXT)
    text_rectangle.center = (int(500/ 2), int(500/ 4))
    screen.blit(text_surface, text_rectangle)
    text_surface, text_rectangle = text_objects("Menu", large_text)
    text_rectangle.center = (int(500 * 0.98), int(500 * 0.98))
    screen.blit(text_surface, text_rectangle)
    text_surface, text_rectangle = text_objects('Created by Maria', large_text)
    text_rectangle.center = (int(500 / 2), int(500 * 0.84))
    screen.blit(text_surface, text_rectangle)
    pygame.display.update()

def _help():
        """
        Print a short summary of the game to help the player.
        """
        print("Click one of the buttoms on the screen to make the Humanoid take action")
        print("Win by not letting the health bar reach below 40%")

def main_menu():
    global ticks
    main_menu_setup()
    # while True:
    click = False
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        alt_f4 = (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE))
        if event.type == pygame.QUIT or alt_f4: sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            RUNNING = True
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_v or event.key == pygame.K_h):
            _help()
    if button('S T A R T  G A M E', 100, 375, 100, 50, black, green, pygame.K_SPACE):
        background = background
    elif button('P L A Y  A S  I S A B E L L E', 200, 375, 100, 50, black, green, pygame.K_i):
        background = isabelle
        main_menu_setup()
    elif button('P L A Y  A S  T O M', 300, 375, 100, 50, black, green, pygame.K_o):
        background = tom
        main_menu_setup()
    elif button('Q U I T  G A M E', 400, 375, 100, 50, black, green, pygame.K_q):
        sys.exit()
    pygame.display.update()
    clock.tick(60)

def text_objects(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

def feeding_status():
    if 36 <= timer_sec <= 40 or 10 <= timer_sec <= 8:
        # if pygame.MOUSEBUTTONDOWN:
        print("Feeding")
        pygame.draw.rect(screen, green, (0, 0, 240, 30))
        pygame.draw.rect(screen, red, (50, 0, 240, 30))

def socializing_status():
    if 44 <= timer_sec <= 46 or 4 <= timer_sec <= 10:
        # if pygame.MOUSEBUTTONDOWN:
        print("Socializing")
        pygame.draw.rect(screen, green, (0, 0, 240, 30))
        pygame.draw.rect(screen, red, (50, 0, 240, 30))

def bathroom_status():
    if 40 <= timer_sec <= 42 or 30 <= timer_sec <= 35:
        # if pygame.MOUSEBUTTONDOWN:
        print("Bathroom")
        pygame.draw.rect(screen, green, (0, 0, 240, 30))
        pygame.draw.rect(screen, red, (50, 0, 240, 30))

def sleeping_status():
    if 17 <= timer_sec <= 20 or 28 <= timer_sec <= 30:
        # if pygame.MOUSEBUTTONDOWN:
        print("Sleeping")
        pygame.draw.rect(screen, green, (0, 0, 240, 30))
        pygame.draw.rect(screen, red, (50, 0, 240, 30))

def working_status():
    if 24 <= timer_sec <= 26:
        # if pygame.MOUSEBUTTONDOWN:
        print("Work")
        pygame.draw.rect(screen, green, (0, 0, 240, 30))
        pygame.draw.rect(screen, red, (50, 0, 240, 30))

def button(msg,x,y,w,h,ic,ac,key=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action(key)         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms", 10)
    text_surface, text_rectangle = text_objects("whatever", smallText)
    text_rectangle.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(text_surface, text_rectangle)

def action(key):
    if key == pygame.K_e:
        print("Humanoid Has Eaten!")
        feeding_status()
    if key == pygame.K_p:
        print("Humanoid Has used the bathroom!")
        bathroom_status()
    if key == pygame.K_s:
        print("Humanoid Has Slept!")
        sleeping_status()
    if key == pygame.K_w:
        print("Humanoid Has made money!")
        working_status()
    if key == pygame.K_t:
        print("Hi! How are you?")
        socializing_status()

# while RUNNING:
#     main_menu_setup()
#     screen.blit(background, (0, 0))
#     if 47 <= timer_sec <= 48:
#         pygame.draw.rect(screen, red, (300, 375, 200, 70))
#         text_surface, text_rectangle = text_objects("Menu", MENU_TEXT)
#         text_rectangle.center = ((300+(200/2)), 375+(70/2))
#         screen.blit(text_surface, text_rectangle)
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if button('S T A R T  G A M E', 100, 375, 100, 50, black, green, pygame.K_SPACE):
#                 background = background
#                 screen.blit(background, (0, 0))
#             elif button('P L A Y  A S  I S A B E L L E', 200, 375, 100, 50, black, green, pygame.K_i):
#                 background = isabelle
#                 screen.blit(background, (0, 0))
#                 main_menu_setup()
#             elif button('P L A Y  A S  T O M', 300, 375, 100, 50, black, green, pygame.K_o):
#                 background = tom
#                 screen.blit(background, (0, 0))
#                 main_menu_setup()
#             elif button('Q U I T  G A M E', 400, 375, 100, 50, black, green, pygame.K_q):
#                 sys.exit()
    
# #         pygame.draw.rect(screen, red, (300, 375, 70, 50))
# #         text_surface, text_rectangle = text_objects("Talk", small_text)
# #         text_rectangle.center = ((300+(70/2)), 375+(50/2))
# #         screen.blit(text_surface, text_rectangle)
while RUNNING:
    # main_menu()
    screen.fill(white)
    screen.blit(isabelle, (0, 0))
    screen.blit(humanoid, (250, 350))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == TIMER:
            timer_sec -= 1
            text = font.render(str(timer_sec), True, (0, 128, 0))
            if timer_sec == 0:
                pygame.time.set_timer(TIMER, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            button("Eat", 100, 375, 70, 50, black, green, pygame.K_e)
            button("Talk",300, 375, 70, 50, black, green, pygame.K_t)
            button("Potty",300, 315, 70, 50, black, green, pygame.K_p)
            button("Work", 200, 375, 70, 50, black, green, pygame.K_w)
            button("Sleep",100, 315, 70, 50, black, green, pygame.K_s)
    text_rect = text.get_rect(center = screen.get_rect().center)
    screen.blit(text, text_rect)

# Add inactive 'buttons' that change colors.
    if 44 <= timer_sec <= 46 or 4 <= timer_sec <= 10:
        pygame.draw.rect(screen, red, (300, 375, 70, 50))
        text_surface, text_rectangle = text_objects("Talk", small_text)
        text_rectangle.center = ((300+(70/2)), 375+(50/2))
        screen.blit(text_surface, text_rectangle)
    else:
        pygame.draw.rect(screen, black, (300, 375, 70, 50))
        text_surface, text_rectangle = text_objects("Talk", small_text)
        text_rectangle.center = ((300+(70/2)), 375+(50/2))
        screen.blit(text_surface, text_rectangle)
    if 40 <= timer_sec <= 42 or 30 <= timer_sec <= 35 :
        pygame.draw.rect(screen, red, (300, 315, 70, 50))
        text_surface, text_rectangle = text_objects("Potty", small_text)
        text_rectangle.center = ((300+(70/2)), 315+(50/2))
        screen.blit(text_surface, text_rectangle)
    else:
        pygame.draw.rect(screen, black, (300, 315, 70, 50))
        text_surface, text_rectangle = text_objects("Potty", small_text)
        text_rectangle.center = ((300+(70/2)), 315+(50/2))
        screen.blit(text_surface, text_rectangle)
    if 24 <= timer_sec <= 26:
        pygame.draw.rect(screen, red, (200, 375, 70, 50))
        text_surface, text_rectangle = text_objects("Work", small_text)
        text_rectangle.center = ((200+(70/2)), 375+(50/2))
        screen.blit(text_surface, text_rectangle)
    else:
        pygame.draw.rect(screen, black, (200, 375, 70, 50))
        text_surface, text_rectangle = text_objects("Work", small_text)
        text_rectangle.center = ((200+(70/2)), 375+(50/2))
        screen.blit(text_surface, text_rectangle)
    if 17 <= timer_sec <= 20 or 28 <= timer_sec <= 30:
        pygame.draw.rect(screen, red, (100, 315, 70, 50))
        text_surface, text_rectangle = text_objects("Sleep", small_text)
        text_rectangle.center = ((100+(70/2)), 315+(50/2))
        screen.blit(text_surface, text_rectangle)
    else:
        pygame.draw.rect(screen, black, (100, 315, 70, 50))
        text_surface, text_rectangle = text_objects("Sleep", small_text)
        text_rectangle.center = ((100+(70/2)), 315+(50/2))
        screen.blit(text_surface, text_rectangle)
    if 36 <= timer_sec <= 40 or 10 <= timer_sec <= 8:
        pygame.draw.rect(screen, red, (100, 375, 70, 50))
        text_surface, text_rectangle = text_objects("Eat", small_text)
        text_rectangle.center = ((100+(70/2)), 375+(50/2))
        screen.blit(text_surface, text_rectangle)
    else:
        pygame.draw.rect(screen, black, (100, 375, 70, 50))
        text_surface, text_rectangle = text_objects("Eat", small_text)
        text_rectangle.center = ((100+(70/2)), 375+(50/2))
        screen.blit(text_surface, text_rectangle)

# Add health bar visual
    # pygame.draw.rect(screen, grey, (0, 0, 240, 30))
    # pygame.draw.rect(screen, grey, (50, 0, 240, 30))
    mouse = pygame.mouse.get_pos()

    pygame.display.update()
pygame.quit()