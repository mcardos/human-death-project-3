import random
import pygame
from pygame.locals import (USEREVENT)

pygame.init()
# Constant variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)

class HealthfyModel:
    """
    Maintains all information included in the game Healthfy.

    Attributes:
        health = An integer represeting the health of the humanoid.
        _max_health = An integer representing the maximum health of the humanoid.
        _user_score = An integer representing the score of the player.
        screen = A display surface 500 pixels wide and 500 pixels long.
        timer_sec = An integer representing the time, in seconds, of a single game.
        TIMER = An event, represented by the integer 25, that appears at 0 seconds in
        a single game.
    """
    def __init__(self):
        """
        Creates a new Healthfy instance and the buttons necessary
        to begin a game.

        Initializing the health, user score and current status of the humanoid.
        """
        self.health = 240
        self.max_health = 240
        self._user_score = 0
        self.screen = pygame.display.set_mode((500, 500))
        self.timer_sec = 48
        self.feed = Button(100, 375, "Eat", self.feeding_status, self.screen)
        self.work = Button(200, 375, "Work", self.working_status, self.screen)
        self.talk = Button(300, 375, "Talk", self.socializing_status, self.screen)
        self.potty = Button(300, 315, "Potty", self.bathroom_status, self.screen)
        self.sleep = Button(100, 315, "Sleep", self.sleeping_status, self.screen)
        self.bomb = Button(200, 315, "Binge...", self.bomb_status, self.screen)
        self.TIMER = USEREVENT + 1
        self.random_sec = random.randint(0, 48)
        self.talk_alert = False
        self.feed_alert = False
        self.potty_alert = False
        self.work_alert = False
        self.sleep_alert = False

    def feeding_status(self):
        """
        Add to the health bar if user clicks on the 'Eat'
        button when it flashes red.
        """
        if 36 <= self.get_timer_sec() <= 40 or 8 <= self.get_timer_sec() <= 10:
            if self.feed_alert == False:
                self.feed.set_to_alert()
                self.health -= 24
                self.feed_alert = True
        else:
            self.feed_alert = False
            self.feed.set_to_normal()

    def sleeping_status(self):
        """
        Add to the health bar if user clicks on the 'Sleep'
        button when it flashes red.
        """
        if 17 <= self.get_timer_sec() <= 20 or 28 <= self.get_timer_sec() <= 30:
            if self.sleep_alert == False:
                self.sleep.set_to_alert()
                self.health -= 24
                self.sleep_alert = True
        else:
            self.sleep_alert = False
            self.sleep.set_to_normal()

    def working_status(self):
        """
        Add to the health bar if user clicks on the 'Work'
        button when it flashes red.
        """
        if 24 <= self.get_timer_sec() <= 26:
            if self.work_alert == False:
                self.work.set_to_alert()
                self.health -= 48
                self.work_alert = True
        else:
            self.work_alert = False
            self.work.set_to_normal()

    def socializing_status(self):
        """
        Add to the health bar if user clicks on the 'Talk'
        button when it flashes red.
        """
        if 44 <= self.get_timer_sec() <= 46 or 4 <= self.get_timer_sec() <= 10:
            if self.talk_alert == False:
                self.talk.set_to_alert()
                self.health -= 24
                self.talk_alert = True
        else:
            self.talk_alert = False
            self.talk.set_to_normal()

    def bathroom_status(self):
        """
        Add to the health bar if user clicks on the 'Potty'
        button when it flashes red.
        """
        if 40 <= self.get_timer_sec() <= 42 or 30 <= self.get_timer_sec() <= 35:
            if self.potty_alert == False:
                self.potty.set_to_alert()
                self.health -= 24
                self.potty_alert = True
        else:
            self.potty_alert = False
            self.potty.set_to_normal()

    def bomb_status(self):
        """
        Decrease the health bar if user clicks on the "Binge..."
        button when it flashes red.
        """
        if (self.random_sec <= self.timer_sec <= self.random_sec)\
            or (3 <= self.timer_sec <= 4) \
            or (10 <= self.timer_sec <= 11):
            self.health -= 48
            self.bomb.set_to_alert()
        else:
            self.bomb.set_to_normal()

    def user_score(self):
        """
        Convert health bar to scores by multiplying it by 100.
        """
        self._user_score += self.health
        return self._user_score

    # def action(self, key):
    #     """
    #     Process user inputs and call appropiate function to update health bar.
    #     """
    #     if key == K_e:
    #         print("Humanoid Has Eaten!")
    #         self.feeding_status()
    #     if key == K_p:
    #         print("Humanoid Has used the bathroom!")
    #         self.bathroom_status()
    #     if key == K_s:
    #         print("Humanoid Has Slept!")
    #         self.sleeping_status()
    #     if key == K_w:
    #         print("Humanoid Has made money!")
    #         self.working_status()
    #     if key == K_t:
    #         print("Hi! How are you?")
    #         self.socializing_status()

    def countdown(self):
        """
        Decrease time by 1 second and if time is at 0 seconds, set timer to 0.
        """
        self.timer_sec -= 1
        if self.timer_sec == 0:
            pygame.time.set_timer(self.TIMER, 0)

    def get_timer_sec(self):
        """
        Return the current time, an integer.
        """
        return self.timer_sec




class Button:
    """
    Keep track of colors and know when the user has clicked the button
    """
    def __init__(self, x, y, name, on_click, screen):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 50
        self.name = name
        self.on_click = on_click
        self.normal_color = black
        self.alert_color = red
        self.click_color = green
        self.current_color = black
        self.screen = screen

    def set_to_alert(self):
        """
        Set current color to the alert color
        """
        self.current_color = self.alert_color

    def set_to_normal(self):
        """
        set current color to the normal color
        """
        self.current_color = self.normal_color

    def check_click(self):
        """
        set the current color to the click color when the user has clicked on the button
        """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y:
            if click[0] == 1 and self.on_click is not None:
                self.on_click()
                self.current_color = self.click_color

    def draw(self):
        """
        Create the 5 buttons with their specified colors, sizes and positions on the game screen
        """
        pygame.draw.rect(self.screen, self.current_color, (self.x, self.y, self.width, self.height))
        small_text = pygame.font.SysFont("comicsansms", 30)
        text_surface, text_rectangle = self.create_text_objects(self.name, small_text)
        text_rectangle.center = ((self.x+(self.width/2)), (self.y+(self.height/2)))
        self.screen.blit(text_surface, text_rectangle)

    def create_text_objects(self, text, font):
        """
        Create a new surface and return a specified text rendered on it.
        """
        text_surface = font.render(text, True, white)
        return text_surface, text_surface.get_rect()
