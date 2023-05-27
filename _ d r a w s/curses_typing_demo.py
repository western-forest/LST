import curses
import random

def ui_loop(standard_screen):
    standard_screen.clear()
    standard_screen.addstr("hi curses")
    standard_screen.refresh()
    standard_screen.getkey()

curses.wrapper(ui_loop)

# print(random.randint(0,5))
# print(random.randint(0,5))
# print(random.randint(0,5))
# print(random.randint(0,5))
# print(random.randint(0,5))
# print(random.randint(0,5))
