# Healthfy
### Game Overview
This game is all about keeping a humanoid alive. This humanoid is represented by an icon and its life by a health bar. The player needs to keep this humanoid alive by correctly commanding the feeding, working, socializing, sleeping, and bathroom usage of this humanoid at the right time. The player loses if the humanoid health bar reaches below 40 or if the game is timed out. In order to win, the player needs to keep the humanoid alive for 48 seconds.

The classes and functions are contained in 3 separate files titled `model.py`, `view.py`, and `controller.py`. In these files, there are 3 classes in accordance to the Model-View-Controller architectural model. These classes maintain the information, visualizes it, and processes the player's inputs. Lastly there is one file, `main_game.py`, that runs the game.

### Installation
The package that we used to design this game was pygame. Pygame requires Python; if you don't already have it, you can download it from python.org and then follow the steps below to run the game:  

* Install [anaconda](https://docs.anaconda.com/anaconda/install/linux/).
* To install pygame run the following command on the terminal: ```python3 -m pip install -U pygame --user```
* Clone the repo: https://github.com/mcardos/project-3-healthfy.git
* ```cd``` into the cloned repo on your terminal node and run the ```main_game.py``` to start playing the game.

### Contribution
Feel free to send pull requests or email us with any feedback.