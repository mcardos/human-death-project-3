import pygame
import sys
from pygame.locals import *
import time
import os 


os.environ["SDL_AUDIODRIVER"]= "dsp"
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)
global timer_sec
timer_sec  = 48
TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 1000)


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
        self.health = 200.0      # Current Health
        self._maxHealth = 200    # Max Health
        self._healthDashes = 20  # Max Displayed dashes
        self._user_score = None
        timer_sec = 48
        self.screen = pygame.display.set_mode((500,500))
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
        if 36 <= timer_sec <= 40 or 10 <= timer_sec <= 8:
            print("Feeding")
            self.health += 5
                

    def sleeping_status(self):
        """
        Add or decrease the health bar if user clicks on the 'Sleep'
        button when it flashes red.
        """
        if 17 <= timer_sec <= 20 or 28 <= timer_sec <= 30:
            self.health += 5
    
    def working_status(self):
        """
        Add or decrease the health bar if user clicks on the 'Work'
        button when it flashes red.
        """
        if 24 <= timer_sec <= 26:
            self.health += 5

    def socializing_status(self):
        """
        Add or decrease the health bar if user clicks on the 'Talk'
        button when it flashes red.
        """
        if 44 <= timer_sec <= 46 or 4 <= timer_sec <= 10:
            self.health += 5

    def bathroom_status(self):
        """
        Add or decrease the health bar if user clicks on the 'Potty'
        button when it flashes red.
        """
        if 40 <= timer_sec <= 42 or 30 <= timer_sec <= 35:
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
        print("ALERT", self.name)


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
        pygame.draw.rect(self.screen, self.current_color,(self.x,self.y,self.width,self.height))
        small_text = pygame.font.SysFont("comicsansms",30)
        text_surface, text_rectangle = self.create_text_objects(self.name, small_text)
        text_rectangle.center = ( (self.x+(self.width/2)), (self.y+(self.height/2)) )
        self.screen.blit(text_surface, text_rectangle)
    
    def create_text_objects(self, text, font):
        text_surface = font.render(text, True, white)
        return text_surface, text_surface.get_rect()


class HealthfyView:
    """
    Displays the current game (the current status of the humanoid, face, and health bar)
    and the inputs/buttons to the player.

    Attributes:
        _healthbar: A float bar representing the health of the humanoid
        _current_status: A number representing the current activity of the humanoid
        buttons: A list of 5 numbers that represent each activity
    """

    def __init__(self, model):
        """
        Initialize the view class.
        """
        self.model = model
        self.screen = model.screen
        pygame.display.set_caption('Healthfy')
        self.background = pygame.image.load("Images/background.jpg")
        self.humanoid = pygame.image.load("Images/humanoid.jpg")


    def text_objects(self, text, font):
        text_surface = font.render(text, True, white)
        return text_surface, text_surface.get_rect()

    def draw(self):
        """ Draw the current game state to the screen """
       
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.humanoid, (250, 350))
        font = pygame.font.SysFont(None, 100)
        text = font.render(str(timer_sec), True, (0, 128, 0))
        text_rect = text.get_rect(center = self.screen.get_rect().center)
        self.screen.blit(text, text_rect)



    def set_timer(self):
        timer_sec -= 1
        if timer_sec == 0:
            pygame.time.set_timer(TIMER, 0)
      

    def buttons(self):
        """
        Display the 5 buttons to the user.
        """
        pass

    def current_status(self):
        """
        Display the activity currently being performed by the humanoid. 
        """
        print(f"Humanoid is currently {model.process_input}\n Try to keep them alive.")
     
      
    def display_score(self):
        """
        Display the top score and the current score to the player.
        """
        score = font.render(f"Score: {HealthfyModel().user_score}")


class HealthfyController:
    """
    Get the inputs from the user.

    Attributes:
        _quit_game: Command to exit the game
        get_input: Gets the user input of an integer from 1 to 5
        user_score: Adds or decreases the user score based on the inputs.
        _help: Print short summary of the game.
        _invalid_input: Print short message telling the user to input another command.
    """

    def __init__(self, HealthfyModel):
        """
        docstring
        """
        pass

    


    def get_input(self): # USe as help function instead since we're already handling user input in a different method
        """
        Gets the input from the player and translates it into one of the 5 commands.

        Returns:
            A string with the current status of the humanoid and an updated healthbar.
        """
        player_input = input(
            "What is your command? (or enter h for help, q to quit): ")
        stripped_input = player_input.strip()
        if stripped_input == "q":
            self._quit_game()
        elif stripped_input == "h":
            self._help()

    def handle_event(self, event):
        """
        """
        if event.type == KEYDOWN:
            if event.key == pygame.K_e:
                print("Has Eaten!") # Will replace this with what happens to the game. 
                # Add other Key board presses e.g S, B, W

    
    def _quit_game(self):
        """
        Print a message and quit the game by exiting the program.
        """
        print('You quit.')
        sys.exit()

    def _help(self):
        """
        Print a short summary of the game to help the player.
        """
        print("Click one of the buttoms on the screen to make the Humanoid take action")
        print("Win by not letting the health bar reach below 40%")
    
    def _invalid_input(self):
        """
        Print an error message stating that the input to the controller was
        invalid in some way and for the user to input another command.
        """
        print("Invalid input. Please try again. Enter h for help or q to quit.")



if __name__ == '__main__':
    pygame.init()
    size = (500, 500)
    model = HealthfyModel()
    print(model)
    view = HealthfyView(model)
    controller = HealthfyController(model)
    
    running = True
    talk_alert = False
    feed_alert = False
    potty_alert = False
    work_alert = False
    sleep_alert = False
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
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
                model.health -= 10
                talk_alert = True
        else:
            talk_alert = False
            model.talk.set_to_normal()
            
        if 40 <= timer_sec <= 42 or 30 <= timer_sec <= 35 :
            if potty_alert == False:
                model.potty.set_to_alert()
                model.health -= 10
                potty_alert = True
        else:
            potty_alert = False
            model.potty.set_to_normal()
        if 24 <= timer_sec <= 26:
            if work_alert == False:
                model.work.set_to_alert()
                model.health -= 20
                work_alert = True
        else:
            work_alert = False
            model.work.set_to_normal()
        if 17 <= timer_sec <= 20 or 28 <= timer_sec <= 30:
            if sleep_alert == False:
                model.sleep.set_to_alert()
                model.health -= 10
                sleep_alert = True
        else:
            sleep_alert = False
            model.sleep.set_to_normal()
        if 36 <= timer_sec <= 40 or 8 <= timer_sec <= 10:
            if feed_alert == False:
                model.feed.set_to_alert()
                model.health -= 10
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
        pygame.draw.rect(model.screen, green, (0, 0, 240*model.health/model._maxHealth, 30))
        pygame.display.update()
    pygame.quit()