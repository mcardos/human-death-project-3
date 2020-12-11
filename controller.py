import pygame 
import sys


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
        Initialize the controller class.
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

