import shutil
import os

os.system('python3 resizeUtility.py')

# Initialize some variables for use in menu display
cols, rows = shutil.get_terminal_size()
lastLine = rows//2
centerLeftRight = cols//1
centerTopBottom = (lastLine) // 3 
halfWidth = cols // 2
halfWidthLessBorder = halfWidth - 2

# Function calculates the border buffer on each side for lines with text
def borderCalculator(strToCalc):
    # If not even value, division will result in botched borders. Add a space to end of string as workaround
    if len(strToCalc) % 2 != 0:
        strToCalc = strToCalc + ' '
    return (halfWidthLessBorder - len(strToCalc)) // 2, strToCalc

# display function
def display():
    # Set up and enter primary menu loop
    selection = -1
    while selection != 'newgame' and selection != 'loadgame' and selection != 'credits' and selection != 'exit':
        os.system('clear')

        print('\n' * centerTopBottom)
        # Print a top border to the box
        print(('▒' * halfWidth).center(centerLeftRight))
        # Side borders with no center text
        print(('▒' + (' ' * halfWidthLessBorder) + '▒').center(centerLeftRight))
        buffer, header = borderCalculator('The Spooky Mansion Mystery')
        # Print line of text with borders
        print(('▒' + (' ' * buffer) + header + (' ' * buffer) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * halfWidthLessBorder) + '▒').center(centerLeftRight))
        buffer, subheading = borderCalculator('Do you dare enter the mansion?')
        print(('▒' + (' ' * buffer) + subheading + (' ' * buffer) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * halfWidthLessBorder) + '▒').center(centerLeftRight))
        buffer, instruction = borderCalculator('Please Make a Selection:')
        print(('▒' + (' ' * buffer) + instruction + (' ' * buffer) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * halfWidthLessBorder) + '▒').center(centerLeftRight))
        buffer, new = borderCalculator('\'newgame\' - to start a new game')
        print(('▒' + (' ' * buffer) + new + (' ' * buffer) + '▒').center(centerLeftRight))
        buffer, load = borderCalculator('\'loadgame\' - to load a saved game')
        print(('▒' + (' ' * buffer) + load + (' ' * buffer) + '▒').center(centerLeftRight))
        buffer, creds = borderCalculator('\'credits\' - to view the game credits')
        print(('▒' + (' ' * buffer) + creds + (' ' * buffer) + '▒').center(centerLeftRight))
        buffer, depart = borderCalculator('\'exit\' - to exit the game')
        print(('▒' + (' ' * buffer) + depart + (' ' * buffer) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * halfWidthLessBorder) + '▒').center(centerLeftRight))
        print(('▒' * halfWidth).center(centerLeftRight))
        print('\n' * (lastLine - 3))
        selection = input('Enter selection:')

    # Having exited the loop, return the user's selection
    return selection
