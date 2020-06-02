import shutil

from Game import Game

def main():

    cols, rows = shutil.get_terminal_size()
    if cols != 125 or rows != 50:
        print('This game requires an un-maximized window, and will then set itself to 125 cols * 50 rows')
        print('Required screen resolution: >=1000pixels x >=1000pixels (e.g. 1920x1080)')
        exit()
    game = Game()
    game.start()

if __name__ == '__main__':
    main()
