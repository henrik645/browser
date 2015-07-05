import curses
import sys

def exit(code=0):
    try:
        curses.endwin()
    except curses.error: 
        pass
    sys.exit(code)
