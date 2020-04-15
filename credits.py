import os
import shutil
import time

# Initialize some variables for use in displaying the credits screen
cols, rows = shutil.get_terminal_size()
lastLine = rows//2
centerLeftRight = cols//1
centerTopBottom = (lastLine) // 3 



def display():
    selection = -1
    while selection != 'e':
        os.system('clear')

        print ('█' * cols)
        print('\n' * centerTopBottom)
        # 60 is, unfortunately, a "magic number". Then take that width and subtract str length and 2 addl for borders subsequent
        print(('▒' * 60).center(centerLeftRight))
        print(('▒' + (' ' * (60 - 2)) + '▒').center(centerLeftRight))
        # Here 60 - 26 for str len - 2 for borders / 2 = 16 spaces on each side
        print(('▒' + (' ' * 16) + 'The Spooky Mansion Mystery' + (' ' * 16) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * 10) + 'a cs467 capstone project - spring 2020' + (' ' * 10) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * (60 - 2)) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * 22) + 'developed by: ' + (' ' * 22) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * (60 - 2)) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * 22) + 'Steven Blasiol' + (' ' * 22) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * 22) + 'Kevin Ohrlund ' + (' ' * 22) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * 24) + 'Bjorn Berg' + (' ' * 24) + '▒').center(centerLeftRight))
        print(('▒' + (' ' * (60 - 2)) + '▒').center(centerLeftRight))
        print(('▒' * 60).center(centerLeftRight))
        print('\n' * (lastLine - 2))
        selection = input('press \'e\' to return to main menu  ')
    