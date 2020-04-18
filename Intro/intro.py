import os
import shutil

# Initialize some variables for use in displaying the credits screen
cols, rows = shutil.get_terminal_size()
lastLine = rows//2
centerLeftRight = cols//1
centerTopBottom = (lastLine) // 3 

halfWidth = cols // 2

def display():
    selection = -1
    while selection != ' ':
        os.system('clear')
        print ('█' * cols)
        print('\n' * centerTopBottom)
        # Print a top border to the box
        longestString = 'and you really should get back, you think to yourself. You haven\'t'
        print(('▒' * len(longestString)).center(centerLeftRight))
        print('\n')
        print('It is a crisp fall day. You\'re walking along a dirt trail about'.center(centerLeftRight))
        print('a half hour out from your new hometown in Pembroke Falls, Maine.'.center(centerLeftRight))
        print('Your feet crunch on fallen leaves. The sun is starting to go down'.center(centerLeftRight))
        print(longestString.center(centerLeftRight))
        print('explored this trail before and you would not want to get lost.\n'.center(centerLeftRight))
        print('You think you hear a stick cracking, but it was not due to you.\n\n'.center(centerLeftRight))
        print('What was that? Maybe there is someone else here?\n'.center(centerLeftRight))
        print('You look around but see nothing. Or you think you saw nothing.'.center(centerLeftRight))
        print('There was a blur by a tree behind you, but must be a bird...\n\n'.center(centerLeftRight))
        print('You hear a sound like a woosh. You  see a flash of light as'.center(centerLeftRight))
        print('you are struck from behind. You fall forward and all goes black.\n\n'.center(centerLeftRight))
        print(('▒' * len(longestString)).center(centerLeftRight))

        print('\n' * (lastLine - 13))
        selection = input('press \'enter\' to continue... ')
        selection = ' ' + selection
    # Having reached this point, selection matches. Clear screen to begin game.
    os.system('clear')
