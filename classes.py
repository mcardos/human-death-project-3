import pygame,sys
from pygame.locals import *


# pygame.init()
# size = (576, 1024)
# screen = pygame.display.set_mode(size) # Create a screen
# pygame.display.set_caption('HEALTHFY') # creates name of the game on top
# clock = pygame.time.Clock()

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

    def process_input(self):
        """
        """

    def feeding_status(self):
        pass

    def sleeping_status(self, parameter_list):
        """
        Add or decrease the health bar if user inputs integer 2.
        """
        pass
    
    def working_status(self):
        pass

    def socializing_status(self):
        pass

    def bathroom_status(self):
        pass
    
    def user_score(self, parameter_list):
        """
        docstring
        """
        pass



class HealthfyView(HealthfyModel):
    """
    Displays the current game (the current status of the humanoid, face, and health bar)
    and the inputs/buttons to the player.

    Attributes:
        _healthbar: A float bar representing the health of the humanoid
        _current_status: A number representing the current activity of the humanoid
        buttons: A list of 5 numbers that represent each activity
    """

    def __init__(self, HealthfyModel):
        """
        Initialize the view class.
        """
        super().__init__()
    
    def buttons(self, parameter_list):
        """
        Display the 5 buttons to the user.
        """
        pass

    def current_status(self):
        """
        Display the activity currently being performed by the humanoid. 
        """
        print(f"Humanoid is currently {model.process_input}\n Try to keep them alive.")
    
    def display_bar(self, parameter_list):
        """
        Convert current health of the humanoid to a percentage and corresponding dashes to display. 

        Returns: 
            A float representing the current health of the humanoid in percentage, 
            and a bar with dashes the size of the percentage (i.e. 1 dash for 10%).
        """
        dashConvert = int(self._maxHealth/self._healthDashes)    # Get the number to divide by to convert health to dashes
        currentDashes = int(self.health/dashConvert)             # Convert health to dash count
        remainingHealth = self._healthDashes - currentDashes     # Get the health remaining to fill as space

        healthDisplay = '-' * currentDashes                             # Convert to dashes as a string:   "--------"
        remainingDisplay = ' ' * remainingHealth                        # Convert to spaces as a string: "            "
        percent = str(int((self.health/self._maxHealth)*100)) + "%"     # Get the percent as a whole number:

        print("|" + healthDisplay + remainingDisplay + "|")  # Print out text based health bar 
        print("         " + percent)                         # Print the percent
    
    
    def display_score(self, parameter_list):
        """
        Display the top score and the current score to the player.
        """
        pass




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

    def __init__(self):
        """
        docstring
        """
        pass

    def get_input(self):
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
# TODO: Add an else statement that corresponds with the commands.
    
    def _quit_game(self):
        """
        Print a message and quit the game by exiting the program.
        """
        print('You quit, call 2BR02B or something.')
        sys.exit()

    def _help(self):
        """
        Print a short summary of the game to help the player.
        """
        print("Click one of the buttoms or the keys 1 to 5 to command")
        print("the humanoid to do something. Win by not letting them die.")
    
    def _invalid_input(self):
        """
        Print an error message stating that the input to the controller was
        invalid in some way and for the user to input another command.
        """
        print("Invalid input. Please try again. Enter h for help or q to quit.")



def main():
    model = HealthfyModel()

if __name__ == '__main__':
    HealthfyController().get_input
    # pygame.init()
    # size = (576, 1024)
    # screen = pygame.display.set_mode(size) # Create a screen
    # pygame.display.set_caption('HEALTHFY') # creates name of the game on top
    # clock = pygame.time.Clock()

    # running = True
    # while True:
    #     pass