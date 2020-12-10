import os
import pygame 
import model, view, controller



black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)
global timer_sec
timer_sec  = 48
TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 1000)


os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
model = model.HealthfyModel()
print(model)
view = view.HealthfyView(model)
# controller = controller.HealthfyController(model)

RUNNING = True
talk_alert = False
feed_alert = False
potty_alert = False
work_alert = False
sleep_alert = False
while RUNNING:
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == TIMER:
            timer_sec -= 1
            if timer_sec == 0:
                pygame.time.set_timer(TIMER, 0)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            model.feed.check_click()
            model.work.check_click()
            model.talk.check_click()
            model.potty.check_click()
            model.sleep.check_click()

    
    if 44 <= timer_sec <= 46 or 4 <= timer_sec <= 10:
        if talk_alert == False:
            model.talk.set_to_alert()
            model.health -= 5
            talk_alert = True
    else:
        talk_alert = False
        model.talk.set_to_normal()
        
    if 40 <= timer_sec <= 42 or 30 <= timer_sec <= 35 :
        if potty_alert == False:
            model.potty.set_to_alert()
            model.health -= 5
            potty_alert = True
    else:
        potty_alert = False
        model.potty.set_to_normal()
    if 24 <= timer_sec <= 26:
        if work_alert == False:
            model.work.set_to_alert()
            model.health -= 5
            work_alert = True
    else:
        work_alert = False
        model.work.set_to_normal()
    if 17 <= timer_sec <= 20 or 28 <= timer_sec <= 30:
        if sleep_alert == False:
            model.sleep.set_to_alert()
            model.health -= 5
            sleep_alert = True
    else:
        sleep_alert = False
        model.sleep.set_to_normal()
    if 36 <= timer_sec <= 40 or 8 <= timer_sec <= 10:
        if feed_alert == False:
            model.feed.set_to_alert()
            model.health -= 5
            feed_alert = True
    else:
        feed_alert = False
        model.feed.set_to_normal()

    view.draw()
    model.feed.draw()
    model.work.draw()
    model.talk.draw()
    model.potty.draw()
    model.sleep.draw()
    pygame.draw.rect(model.screen, red, (0, 0, 240, 30))
    pygame.draw.rect(model.screen, green, (0, 0, 240*model.health/model._max_health, 30))
    pygame.display.update()
pygame.quit()