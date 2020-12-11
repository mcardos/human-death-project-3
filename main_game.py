import os
import pygame
from pygame.locals import (USEREVENT, MOUSEBUTTONDOWN, QUIT)
import model
import view
import controller

# os.environ['SDL_AUDIODRIVER'] = 'alsa'
#  Initialize pygame.
pygame.init()

#  Add constants.
red = (255, 0, 0)
green = (27, 133, 27)
TIMER = USEREVENT + 1

#  Set classes to simple name.
model = model.HealthfyModel()
view = view.HealthfyView(model)
controller = controller.HealthfyController()

#  Background Music
pygame.mixer.init()
pygame.mixer.music.load('Images/Picket Fence Lol.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play(-1)

#  Set variables to change when needed.
RUNNING = True

#  Main loop:
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
    # pygame.mixer.music.play(-1)
    view.draw()
    view.display_score()
    # view.current_status()
    model.feed.draw()
    model.work.draw()
    model.talk.draw()
    model.potty.draw()
    model.sleep.draw()
    model.bomb.draw()
    pygame.draw.rect(model.screen, red, (0, 0, 240, 30))
    pygame.draw.rect(model.screen, green, (0, 0, 240*model.health/model.max_health, 30))
    pygame.display.update()
pygame.quit()
