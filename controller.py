import pygame
import model
import view
import sys

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (27, 133, 27)

class HealthfyController:
    """
    Controller class of the game that translates input from the user into arguements
    that can be used to play the game.

    Attributes:
        model = an instance of the model class that references the features of the game model
    """

    def __init__(self):
        """
        Instantiate the controller class.
        """
        self.model = model.HealthfyModel()

    def get_input(self):
        """
        Gets the input from the player and translates it into one of the 5 commands.

        Returns:
            A string with the current status of the humanoid and an updated healthbar.
        """
        player_input = input(
            "Press a button to command the humanoid! (or enter h for help, q to quit): ")
        stripped_input = player_input.strip()
        if stripped_input == "q":
            self._quit_game()
        elif stripped_input == "h":
            self._help()
    
    def _quit_game(self):
        """
        Print a message and quit the game by exiting the program.
        """
        model.Button(250, 300, 'You quit.', pygame.QUIT, self.model.screen)
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