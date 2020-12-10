import pygame

# Constant variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)
TIMER = pygame.USEREVENT + 1


class HealthfyModel:
    '''
    Keeps track of the state of the game and the humanoid, including:
        1. how many times it was fed,
        2. how many times it rested,
        3. how many times it worked,
        4. how many times it socialized,
        5. how many times it used the bathrooms

    Attributes:
        _healthbar: A float bar representing the health of the humanoid
        feeding_status: A bool representing if the humanoid is hungry or not(False)
        sleeping_status: A bool representing if the humanoid is sleepy or not(False)
        working_status: A bool representing if the humanoid needs to work or not(False)
        _current_status: A number representing the current activity of the humanoid'
        socializing_status: A bool representing if the humanoid needs to socialize or not(False)
        bathroom_status: A bool representing if the humanoid is in need of the bathroom or not(False)
    '''
    def __init__(self):
        """
        Create a new Healthfy instance. Keeps track of health bar and current status of the humanoid.
        """
        self.health = 240.0 
        self._max_health = 240
        self._user_score = 0
        self.screen = pygame.display.set_mode((500, 500))
        self.timer_sec = 48
        self.feed = Button(100, 375, "Eat", self.feeding_status, self.screen)
        self.work = Button(200, 375, "Work", self.working_status, self.screen)
        self.talk = Button(300, 375, "Talk", self.socializing_status, self.screen)
        self.potty = Button(300, 315, "Potty", self.bathroom_status, self.screen)
        self.sleep = Button(100, 315, "Sleep", self.sleeping_status, self.screen)

    
    def feeding_status(self):
        """
        Add or decrease the health bar if user clicks on the 'Eat'
        button when it flashes red.
        """
        if 36 <= self.timer_sec <= 40 or 10 <= self.timer_sec <= 8:
            print("Feeding")
            self.health += 5
                

    def sleeping_status(self):
        """
        Add or decrease the health bar if user clicks on the 'Sleep'
        button when it flashes red.
        """
        if 17 <= self.timer_sec <= 20 or 28 <= self.timer_sec <= 30:
            self.health += 5
    
    def working_status(self):
        """
        Add or decrease the health bar if user clicks on the 'Work'
        button when it flashes red.
        """
        if 24 <= self.timer_sec <= 26:
            self.health += 10

    def socializing_status(self):
        """
        Add or decrease the health bar if user clicks on the 'Talk'
        button when it flashes red.
        """
        if 44 <= self.timer_sec <= 46 or 4 <= self.timer_sec <= 10:
            self.health += 5

    def bathroom_status(self):
        """
        Add or decrease the health bar if user clicks on the 'Potty'
        button when it flashes red.
        """
        if 40 <= self.timer_sec <= 42 or 30 <= self.timer_sec <= 35:
            self.health += 5
    
    def user_score(self):
        """
        Convert health bar to scores by multiplying it by 1000.
        """
        self._user_score += self.health * 1000
    
    def action(self, key):
        """
        Process user inputs and display the action the Humanoid has taken.
        """
        if key == pygame.K_e:
            print("Humanoid Has Eaten!")
            self.feeding_status()
        if key == pygame.K_p:
            print("Humanoid Has used the bathroom!")
            self.bathroom_status()
        if key == pygame.K_s:
            print("Humanoid Has Slept!")
            self.sleeping_status()
        if key == pygame.K_w:
            print("Humanoid Has made money!")
            self.working_status()
        if key == pygame.K_t:
            print("Hi! How are you?")
            self.socializing_status()

    def countdown(self):
        self.timer_sec -= 1
        if self.timer_sec == 0:
            pygame.time.set_timer(TIMER, 0)
    
    def get_timer_sec(self):
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
        self.current_color = self.alert_color

    def set_to_normal(self):
        self.current_color = self.normal_color

    def check_click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y:
            if click[0] == 1 and self.on_click != None:
                self.on_click()
                self.current_color = self.click_color


    def draw(self):
        pygame.draw.rect(self.screen, self.current_color, (self.x, self.y, self.width, self.height))
        smallText = pygame.font.SysFont("comicsansms", 30)
        text_surface, text_rectangle = self.create_text_objects(self.name, smallText)
        text_rectangle.center = ((self.x+(self.width/2)), (self.y+(self.height/2)))
        self.screen.blit(text_surface, text_rectangle)
    
    def create_text_objects(self, text, font):
        text_surface = font.render(text, True, white)
        return text_surface, text_surface.get_rect()