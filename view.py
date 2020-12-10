import pygame
import model

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)
TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 1000)

class HealthfyView:
    """
    Displays the current state of the game
    (the current status of the humanoid, face, and health bar)
    and the inputs/buttons to the player.

    Attributes:
        _healthbar: A float bar representing the health of the humanoid
        _current_status: A number representing the current activity of the humanoid
        buttons: A list of 5 numbers that represent each activity
    """

    def __init__(self, model):
        """
        Initialize the view class with reference to the model and create
        instances of the  background and humanoid images.
        """
        self.model = model
        self.screen = model.screen
        pygame.display.set_caption('Healthfy')
        self.background = pygame.image.load("Images/background.jpg")
        self.humanoid = pygame.image.load("Images/humanoid.jpg")


    def text_objects(self, text, font):
        """
        
        """
        text_surface = font.render(text, True, white)
        return text_surface, text_surface.get_rect()

    def draw(self):
        """ Draw the current game state to the screen """
       
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.humanoid, (250, 350))
        font = pygame.font.SysFont(None, 100)
        text = font.render(str(self.model.get_timer_sec()), True, (0, 128, 0))
        text_rect = text.get_rect(center = self.screen.get_rect().center)
        self.screen.blit(text, text_rect)
      
    def current_status(self):
        """
        Display the activity currently being performed by the humanoid. 
        """
        print(f"Humanoid is currently {model.action}\n Try to keep them alive.")
    
    
    def display_score(self):
        """
        Display the top score and the current score to the player.
        """
        score = font.render(f"Score: {model.user_score}")