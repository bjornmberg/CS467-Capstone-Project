import credits
import loadGame
import menu
import newGame
import sys

# Call to menu.display
# Intended is to be called from a primary "game" driver
choice = menu.display()

# User option selection handling.
# Intended to be handled by various function calls from appropriate separate source files
if choice == 'startgame':
    newGame.begin()
elif choice == 'loadgame':
    loadGame.begin()
elif choice == 'credits':
    credits.display()
    choice = menu.display()
else:
    exit()
