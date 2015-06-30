import os
import curses
import sys

import page

def print_header(screen, columns):
    screen.addstr('NORMAN EXPLORER  v1.0' + '\n')
    screen.addstr('-' * columns + '\n')
    screen.addstr('-' * columns)
        
def exit(code=0):
    curses.endwin()
    sys.exit(code)
    
stdscr = curses.initscr()
rows, columns = stdscr.getmaxyx()

stdscr.clear()
stdscr.move(0, 0)
print_header(stdscr, columns)

calls = {} #Used for storing special URLs which redirect to another page

while True:    
    stdscr.move(2, 0)
    stdscr.clrtoeol()
    stdscr.refresh()
    url = stdscr.getstr(2, 0)
    url = url.decode("utf-8") #converts from 'bytes' to 'str'
    if (url == 'q'):
        exit()
    if (url in calls):
        url = calls[url]
    stdscr.clear()
    stdscr.move(0, 0)
    print_header(stdscr, columns)
    website = page.Page(url)
    website.load_page()
    stdscr.move(4, 0)
    website.display_page(stdscr)
    calls = website.get_special_calls()
    stdscr.refresh()