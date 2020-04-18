# A test of the curses library. Adapted from:
# https://www.youtube.com/watch?v=zwMsmBsC1GM

import curses

menu = ['The Spooky Mansion Mystery', ' ', 'New Game', 'Load Game', 'Credits', 'Exit']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()

    # screen.border(0)
    box1 = stdscr.subwin(10, 30, 15, 35)
    box1.box()

    # Obtain height and width of the screen
    h, w = stdscr.getmaxyx()

    # Calculate print location
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    box1.refresh()
    stdscr.refresh()

def main(stdscr):
    # Remove blinking cursor
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_idx = 2
    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 2:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0,0, "You have selected {}".format(menu[current_row_idx]))
            stdscr.refresh()
            stdscr.getch()
            if current_row_idx == len(menu) - 1:
                break

        print_menu(stdscr, current_row_idx)
        stdscr.refresh()

curses.wrapper(main)
