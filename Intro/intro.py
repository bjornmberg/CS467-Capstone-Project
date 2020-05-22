import os
import shutil
# I get an import error here in pylint in VS Code. However, the import is working fine. Tested colors as well and functions.
from Wrapper import wrapper

# Initialize some variables for use in displaying the credits screen
cols, rows = shutil.get_terminal_size()
lastLine = rows//2
centerLeftRight = cols//1
centerTopBottom = (lastLine) // 3 

halfWidth = cols // 2

def display():
    """Formats and displays the Game introduction

    :return: VOID
    """

    intro_string = 'It is a crisp fall day. You\'re walking along a dirt trail about a half hour out from your new hometown in Pembroke Falls, Maine. Your feet crunch on fallen leaves. The sun is starting to go down and you really should get back, you think to yourself. You haven\'t explored this trail before and you would not want to get lost.\n\n\nYou think you hear a stick cracking, but it was not due to you.\n\n\n What was that?            ...            Maybe there is someone else here?\n\n\nYou look around but see nothing. Or you think you saw nothing. There was a blur by a tree behind you, but that must just be a bird... right?\n\nYou hear a sound like a woosh. You  see a flash of light as you are struck from behind. You fall forward and all goes black.\n\n'

    selection = -1
    while selection != ' ':
        os.system('clear')
        print ('█' * cols)
        print('\n' * centerTopBottom)
        # Print a top border to the box
        print((' ' * 20) + ('▒' * 85) + '\n')
        print('\n')
        processed = wrapper.wrap_processor(intro_string)
        for i in processed:
            print(i)
        print('\n')
        print((' ' * 20) + ('▒' * 85) + '\n')

        print('\n' * (lastLine - 14))
        selection = input('press \'enter\' to continue... ')
        selection = ' ' + selection
    # Having reached this point, selection matches. Clear screen to begin game.
    os.system('clear')
