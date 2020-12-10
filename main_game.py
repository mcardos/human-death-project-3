import pygame
from pygame.locals import (USEREVENT, MOUSEBUTTONDOWN, QUIT)
import model
import view
import controller

#  Initialize pygame.
pygame.init()

#  Add constants.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)
TIMER = USEREVENT + 1

#  Set classes to simple name.
model = model.HealthfyModel()
view = view.HealthfyView(model)
controller = controller.HealthfyController(model)

#  Set variables to change when needed.
running = True
talk_alert = False
feed_alert = False
potty_alert = False
work_alert = False
sleep_alert = False

#  Main loop:
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == TIMER:
            model.countdown()
        if event.type == MOUSEBUTTONDOWN:
            model.feed.check_click()
            model.work.check_click()
            model.talk.check_click()
            model.potty.check_click()
            model.sleep.check_click()

#  Create events at specific time intervals.
    if 44 <= model.get_timer_sec() <= 46 or 4 <= model.get_timer_sec() <= 10:
        if talk_alert == False:
            model.talk.set_to_alert()
            model.health -= 24
            talk_alert = True
    else:
        talk_alert = False
        model.talk.set_to_normal()
        
    if 40 <= model.get_timer_sec() <= 42 or 30 <= model.get_timer_sec() <= 35 :
        if potty_alert == False:
            model.potty.set_to_alert()
            model.health -= 24
            potty_alert = True
    else:
        potty_alert = False
        model.potty.set_to_normal()
    if 24 <= model.get_timer_sec()<= 26:
        if work_alert == False:
            model.work.set_to_alert()
            model.health -= 48
            work_alert = True
    else:
        work_alert = False
        model.work.set_to_normal()
    if 17 <= model.get_timer_sec() <= 20 or 28 <= model.get_timer_sec() <= 30:
        if sleep_alert == False:
            model.sleep.set_to_alert()
            model.health -= 24
            sleep_alert = True
    else:
        sleep_alert = False
        model.sleep.set_to_normal()
    if 36 <= model.get_timer_sec()<= 40 or 8 <= model.get_timer_sec() <= 10:
        if feed_alert == False:
            model.feed.set_to_alert()
            model.health -= 24
            feed_alert = True
    else:
        feed_alert = False
        model.feed.set_to_normal()

#  Draw and update all screen displays.
    view.draw()
    view.display_score()
    # view.current_status()
    model.feed.draw()
    model.work.draw()
    model.talk.draw()
    model.potty.draw()
    model.sleep.draw()
    pygame.draw.rect(model.screen, red, (0, 0, 240, 30))
    pygame.draw.rect(model.screen, green, (0, 0, 240*model.health/model._max_health, 30))
    pygame.display.flip()
    pygame.display.update()
pygame.quit()