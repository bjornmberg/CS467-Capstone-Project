import os

def display():
    selection = -1

    while selection != ' ':
        os.system('clear')




        selection = input('press \'enter\' to return to the game... ')
        selection = ' ' + selection

    # Having reached this point, selection matches. Clear screen to get ready to return to the game
    os.system('clear')
