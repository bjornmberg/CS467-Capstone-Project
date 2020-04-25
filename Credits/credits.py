import os
import shutil

# Initialize some variables for use in displaying the credits screen
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

def display():
    selection = -1
    while selection != 'e':
        os.system('clear')
        print ('█' * cols)
        print('\n' * centerTopBottom)
        # Print a top border to the box
        print(('▒' * halfWidth).center(centerLeftRight))
        # Side borders with no center text
        print(('▒' + (' ' * halfWidthLessBorder) + '▒').center(centerLeftRight))
        # Set up buffers for borders and the string to print
        buffer, header = borderCalculator('The Spooky Mansion Mystery')
        # Print line of text with borders
        print(('▒' + (' ' * buffer) + header + (' ' * buffer) + '▒').center(centerLeftRight))
        buffer, subheading = borderCalculator('a cs467 capstone project - spring 2020')
        print(('▒' + (' ' * buffer) + subheading + (' ' * buffer) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * halfWidthLessBorder) + '▒').center(centerLeftRight))
        buffer, sectionHead = borderCalculator('developed by:')
        print(('▒' + (' ' * buffer) + sectionHead + (' ' * buffer) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * halfWidthLessBorder) + '▒').center(centerLeftRight))
        buffer, firstName = borderCalculator('Steven Blasiol')
        print(('▒' + (' ' * buffer) + firstName + (' ' * buffer) + '▒').center(centerLeftRight))
        buffer, secondName = borderCalculator('Kevin Ohrlund')
        print(('▒' + (' ' * buffer) + secondName + (' ' * buffer) + '▒').center(centerLeftRight))
        buffer, thirdName = borderCalculator('Bjorn Berg')
        print(('▒' + (' ' * buffer) + thirdName + (' ' * buffer) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * halfWidthLessBorder) + '▒').center(centerLeftRight))
        print(('▒' * halfWidth).center(centerLeftRight))
        print('\n' * (lastLine - 2))
        selection = input('press \'e\' to return to main menu  ')
