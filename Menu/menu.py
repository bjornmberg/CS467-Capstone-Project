# Adapted from:
# https://www.youtube.com/watch?v=zwMsmBsC1GM

import curses

menu = ['New Game', 'Load Game', 'Credits ', 'Exit    ']

def print_menu(stdscr, selected_row_index):
    stdscr.clear()

    # screen.border(0)
    box1 = stdscr.subwin(16, 38, 16, 43)
    box1.border(20)
    box1.border(curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD)

    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BLINK)
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(19,50, "The Spooky Mansion Mystery")
    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BLINK)
    stdscr.attroff(curses.A_BOLD)

    # Obtain height and width of the screen
    h, w = stdscr.getmaxyx()

    # Calculate print location
    for index, row in enumerate(menu):
        # x = w // 2 - len(row) // 2
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + index
        if index == selected_row_index:
            if index == selected_row_index and selected_row_index == 0:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    box1.refresh()
    stdscr.refresh()

def main(stdscr):
    curses.use_default_colors()
    # Remove blinking cursor
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, -1)


    current_row_index = 0
    print_menu(stdscr, current_row_index)

    while 1:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_index > 0:
            current_row_index -= 1
        elif key == curses.KEY_DOWN and current_row_index < len(menu) - 1:
            current_row_index += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row_index == 0:
                curses.curs_set(1)
                curses.echo()
                curses.nocbreak()
                stdscr.keypad(False)
                curses.endwin()
                return 'newgame'
            elif current_row_index == 1:
                curses.curs_set(1)
                curses.echo()
                curses.nocbreak()
                stdscr.keypad(False)
                curses.endwin()
                return 'loadgame'
            elif current_row_index == 2:
                curses.curs_set(1)
                curses.echo()
                curses.nocbreak()
                stdscr.keypad(False)
                curses.endwin()
                return 'credits'
            else:
                curses.curs_set(1)
                curses.echo()
                curses.nocbreak()
                stdscr.keypad(False)
                curses.endwin()
                return 'exit'
            #stdscr.refresh()
            # stdscr.getch()
            # if current_row_index == len(menu) - 1:
            #     break

        print_menu(stdscr, current_row_index)
        stdscr.refresh()

def display():
    selection = curses.wrapper(main)
    return selection
