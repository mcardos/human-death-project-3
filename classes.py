class HealthfyModel:
    '''
    Keep track of the state of the game, including 1. how many times it was fed
    2. how many times it rested, 3. how many times it worked, 
    4. how many times it socialized, 5. how many times it used the bathrooms
    Attributes:
                _healthbar: A float bar represeting the health of the humanoid
                feeding_status: A bool represeting if the humanoid is hungry or not(False)
                sleeping_status: A bool represeting if the humanoid is sleepy or not(False)
                working_status: A bool represeting if the humanoid needs to work or not(False)
                _current_status: A number representing the current activity of the humanoid
                socializing_status: A bool represeting if the humanoid needs to socialize or not(False)
                bathroom_status: A bool represeting if the humanoid is in need of the bathroom or not(False)
    '''
    def __init__(self):
        pass
        # self._healthbar = pass
        # self._current_status = pass
    
    def feeding_status(self):
        pass

    def sleeping_status(self, parameter_list):
        """
        Add or decrease the healthbar if user inputs integer 2.
        """
        pass
    
    def working_status(self):
        pass

    def socializing_status(self):
        pass

    def bathroom_status(self):
        pass
                
class HealthfyView:
    'Displays the current game inputs/buttoms, the current status of the humanoid and its face, as well'
    'as its health bar'
    'Attributes:
                '_healthbar: A float bar represeting the health of the humanoid'
                '_current_status: A number representing the current activity of the humanoid'
                'buttoms: A list of 5 numbers that represent each activity'

    def __init__(self, HealthfyModel):
        """
        docstring
        """
        pass
    
    def buttoms(self, parameter_list):
        """
        Display the 5 buttoms to the user.
        """
        pass

    def current_status(self):
        pass

    def display_bar(self, parameter_list):
        """
        Display the icon of the humanoid and its current healthbar.
        """
        pass
    
    def display_score(self, parameter_list):
        """
        docstring
        """
        pass

class HealthfyController:
    'Process the inputs from the user'
    'Attributes:
                'quit_game: Command to exit the game'
                'process_input: Process the user input of an integer from 1 to 5'
                'user_score: Adds or decreases the user score based on the inputs'

    def __init__(self, parameter_list):
        """
        docstring
        """
        pass

    def process_input(self, parameter_list):
        """
        docstring
        """
        pass
    
    def quit_game(self, parameter_list):
        """
        docstring
        """
        pass

    def user_score(self, parameter_list):
        """
        docstring
        """
        pass

def main():
    ''' 
    Run the game 