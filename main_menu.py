import pygame
import sys
import model
import view
import controller
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont(None, 20)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)
grey = (80, 80, 80)


def text_objects(text, font):
    """
    Create a new surface and return a specified text rendered on it.
        Arguements:
            text = A string representing the words that shall be rendered
            on the screen.
            font = An object representing a font type from the system fonts.
    """
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, ic, ac, key=None):
    """
    Draw buttons on the screen to represent main menu of the game.
    Arguements:
              msg = A string representing the words that shall be rendered
              x = An integer representing the horizontal(x-axis) position of
                the buttons on the screen.
              y = An integer representing the horizontal(y_axis) of the buttons
                on the screen.
              w = An integer showing that the horizontal length of the
                buttons.
              h = An integer showing that the vertical length of the
                buttons (50 pixels).
             ic = Color of the text displayed on the button
             ac = Color on the background on of the button
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1:
            pass
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    text_surface, text_rectangle = text_objects(msg, smallText)
    text_rectangle.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surface, text_rectangle)


click = False


def main_menu():
    """
    Present the user with three buttons that directs to the chosen game.
    """
    click = False
    while True:
        screen.fill(white)
        mx, my = pygame.mouse.get_pos()
        button('S T A R T  G A M E', 50, 100, 200, 50, black, grey)
        button('P L A Y  A S  I S A B E L E', 50, 200, 200, 50, black, grey)
        button('P L A Y  A S  T O M', 50, 300, 200, 50, black, grey)
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                start_game()
        if button_2.collidepoint((mx, my)):
            if click:
                isabele_game()
        if button_3.collidepoint((mx, my)):
            if click:
                tom_game()
#  When to change click to True.
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


#  Add constant variable.
TIMER = USEREVENT + 1

#  Set classes to simple name.
model = model.HealthfyModel.get_instance()
view = view.HealthfyView(model)
controller = controller.HealthfyController()

#  Add background music.
pygame.mixer.init()
pygame.mixer.music.load('Audio/Picket Fence Lol.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play(-1)

#  Add posible backdrops.
tom = pygame.image.load("Images/tom background.jpg")
isabele = pygame.image.load("Images/isabele background small.jpg")
background = pygame.image.load("Images/background.jpg")


def start_game():
    """
    Play the game with the default background.
    """
    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                RUNNING = False
            if event.type == TIMER:
                model.countdown()
            if event.type == MOUSEBUTTONDOWN:
                model.feed.check_click()
                model.work.check_click()
                model.talk.check_click()
                model.potty.check_click()
                model.sleep.check_click()
                model.bomb.check_click()
#  Create events at specific time intervals.
        model.socializing_status()
        model.bathroom_status()
        model.working_status()
        model.sleeping_status()
        model.feeding_status()
        model.bomb_status()
#  Draw and update all screen displays.
        view.draw(background)
        view.display_score()
        view.display_message()
        model.feed.draw()
        model.work.draw()
        model.talk.draw()
        model.potty.draw()
        model.sleep.draw()
        model.bomb.draw()
        pygame.draw.rect(model.screen, red, (0, 0, 240, 30))
        pygame.draw.rect(model.screen, green, (
            0, 0, 240 * model.health / model.max_health, 30
        ))
        pygame.display.update()
    pygame.quit()


def isabele_game():
    """
    Play the game with the background of Isabelle from Animal Crossing.
    """
    running = True
    while running:
        screen.fill(white)
        screen.blit(tom, (0, 0))
#  Main loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                RUNNING = False
            if event.type == TIMER:
                model.countdown()
            if event.type == MOUSEBUTTONDOWN:
                model.feed.check_click()
                model.work.check_click()
                model.talk.check_click()
                model.potty.check_click()
                model.sleep.check_click()
                model.bomb.check_click()
#  Create events at specific time intervals.
        model.socializing_status()
        model.bathroom_status()
        model.working_status()
        model.sleeping_status()
        model.feeding_status()
        model.bomb_status()
#  Draw and update all screen displays.
        view.draw(isabele)
        view.display_score()
        view.display_message()
        model.feed.draw()
        model.work.draw()
        model.talk.draw()
        model.potty.draw()
        model.sleep.draw()
        model.bomb.draw()
        pygame.draw.rect(model.screen, red, (0, 0, 240, 30))
        pygame.draw.rect(model.screen, green, (
            0, 0, 240 * model.health / model.max_health, 30
        ))
        pygame.display.update()
    pygame.quit()


def tom_game():
    """
    Play the game with Tom as the background.
    """
    RUNNING = True
    while RUNNING:
        screen.fill(white)
        screen.blit(tom, (0, 0))
#  Main loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                RUNNING = False
            if event.type == TIMER:
                model.countdown()
            if event.type == MOUSEBUTTONDOWN:
                model.feed.check_click()
                model.work.check_click()
                model.talk.check_click()
                model.potty.check_click()
                model.sleep.check_click()
                model.bomb.check_click()
#  Create events at specific time intervals.
        model.socializing_status()
        model.bathroom_status()
        model.working_status()
        model.sleeping_status()
        model.feeding_status()
        model.bomb_status()
#  Draw and update all screen displays.
        view.draw(tom)
        view.display_score()
        view.display_message()
        model.feed.draw()
        model.work.draw()
        model.talk.draw()
        model.potty.draw()
        model.sleep.draw()
        model.bomb.draw()
        pygame.draw.rect(model.screen, red, (0, 0, 240, 30))
        pygame.draw.rect(model.screen, green, (
            0, 0, 240 * model.health / model.max_health, 30
        ))
        pygame.display.update()
    pygame.quit()


#  Call main_menu.
if __name__ == "__main__":
    main_menu()
