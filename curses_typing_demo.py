import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("hi curses")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

