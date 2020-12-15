import pygame
from pygame.locals import (USEREVENT, MOUSEBUTTONDOWN, QUIT)
import model
import view
import controller


#  Initialize pygame.
pygame.init()

#  Add constant variables.
red = (255, 0, 0)
green = (27, 133, 27)
TIMER = USEREVENT + 1
background = pygame.image.load("Images/background.jpg")

#  Set classes to simple name.
model = model.HealthfyModel()
view = view.HealthfyView(model)
controller = controller.HealthfyController()

#  Add background music.
pygame.mixer.init()
pygame.mixer.music.load('Images/Picket Fence Lol.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play(-1)

#  Main loop:
RUNNING = True
while RUNNING:
    model.screen.fill((250, 250, 250))
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
    # view.current_status()
    model.feed.draw()
    model.work.draw()
    model.talk.draw()
    model.potty.draw()
    model.sleep.draw()
    model.bomb.draw()
    pygame.draw.rect(model.screen, red, (0, 0, 240, 30))
    pygame.draw.rect(model.screen, green, (
        0, 0, 240*model.health/model.max_health, 30
    ))
    pygame.display.update()
pygame.quit()
