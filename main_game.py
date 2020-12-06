import pygame 


class Model:
    def __init__(self):
        self.running = True 




class View:
    def __init__(self):
        self.pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.title = pygame.display.set_caption('Healthfy')
        # Add colors.
        self._black = (0, 0, 0)
        self._white = (255, 255, 255)
        self._red = (255, 0, 0)
        self._green = (27, 133, 27)




class Controller:
    def __init__(self):
        