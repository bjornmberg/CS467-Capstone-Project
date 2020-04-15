import shutil
import os

# Initialize some variables for use in menu display
cols, rows = shutil.get_terminal_size()
lastLine = rows//2
centerLeftRight = cols//1
centerTopBottom = (lastLine) // 3 

# display function
def display():
    selection = -1
    while selection != 'startgame' and selection != 'loadgame' and selection != 'credits' and selection != 'exit':
        os.system('clear')

        print('\n' * centerTopBottom)
        print('The Spook Mansion Mystery'.center(centerLeftRight, ' '))
        print('\n')
        print('Do you dare enter the Mansion?'.center(centerLeftRight, ' '))
        print('\n')
        print('Please Make a Selection:'.center(centerLeftRight, ' '))
        print('\n')
        print('\'startgame\' - to start a new game'.center(centerLeftRight, ' ')) 
        print('\'loadgame\' - to load a saved game'.center(centerLeftRight, ' '))
        print('\'credits\' - to view the game credits'.center(centerLeftRight, ' '))
        print('\'exit\' - to exit the game'.center(centerLeftRight, ' '))
        print('\n' * lastLine)
        selection = input('Enter selection:')

    # Having exited the loop, return the user's selection
    return selection
