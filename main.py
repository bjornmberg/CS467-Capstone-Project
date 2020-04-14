import menu

# Call to menu.display.
# Intended is to be called from a primary "game" driver
choice = menu.display()

# User option selection handling.
# Itended to be handled by various function calls from appropriate separate source files
if choice == 'startgame':
    print('You\'ve chosen to start the game')
elif choice == 'loadgame':
    print('You\'ve chosen to load an existing game')
elif choice == 'credits':
    print('You\'ve chosen to display the credits')
else:
    exit()