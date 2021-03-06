import pygame

pygame.font.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)
TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 1000)
font = pygame.font.SysFont("freesans", 25)


class HealthfyView:
    """
    A view class that displays to the user the current status of
    the game: the screen, background, humanoid and state of buttons.

    Attributes:
        _model = an instance of the model class that references the
        features of the game model.
        screen = an instance of the model class referring to the
        screen display.
        background = an image instance representing the background
        of the game display.
        humanoid = an image instance represrenting the humanoid to be
        displayed on the screen.
    """

    def __init__(self, model):
        """
        Instantiate the view class with reference to the game model.
        """
        self.model = model
        self.screen = model.screen
        pygame.display.set_caption('Healthfy')
        self.background = pygame.image.load("Images/background.jpg")
        self.humanoid = pygame.image.load("Images/humanoid.jpg")

    def draw(self, backdrop):
        """
        Draw the current game state to the screen.
        Arguement:
            backdrop: A surface upon which another surface is displayed.
        """
        self.screen.fill((255, 255, 255))
        self.screen.blit(backdrop, (0, 0))
        self.screen.blit(self.humanoid, (250, 350))
        font = pygame.font.SysFont(None, 100)
        text = font.render(str(self.model.get_timer_sec()), True, (0, 128, 0))
        text_rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, text_rect)

    def current_status(self):
        """
        Display the activity currently being performed by the humanoid.
        """
        self.screen.blit(f"Humanoid is currently {self.model.action()}\
            \n Try to keep them alive.")

    def display_score(self):
        """
        Display the top score and the current score to the player.
        """
        score = font.render(
            f"Score: {self.model.convert_user_score()}", True, black)
        self.screen.blit(score, (250, 0))

    def display_message(self):
        """
        Display the current state of the humanod and what it needs
        """
        message = font.render(self.model.message, True, black)
        self.screen.blit(message, (0, 120))
