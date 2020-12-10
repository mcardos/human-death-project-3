# Healthfy
This game is all about keeping a humanoid alive. This humanoid is simply an icon with a health bar. The player needs to keep this humanoid alive by correctly commanding the feeding, working, socializing, sleeping, and bathroom usage of this humanoid at the right time. The player loses if the humanoid health bar reaches below 40 or if the game is timed out. In order to win the player needs to keep the humanoid alive for 48 seconds.

The classes and functions are contained in 3 separate files appropriately titled `model.py`, `view.py`, and `view.py`. In these files, there are 3 classes in accordance to the Model-View-Controller architectural model. These classes maintains the information, visualizes it, and processes the player's inputs. Lastly there is one file, `main_game.py`, that runs the game.

There are a few libraries used in the making of this game:
1. pygame (to install `pip install pygame`)
2. sys