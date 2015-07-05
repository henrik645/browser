import os
import curses
import sys

import page
import config

from exit import exit

def print_header(screen, columns, config):
    screen.addstr(config.get_parameter('title') + '  ' + config.get_parameter('version') + '\n')
    screen.addstr(config.get_parameter('horizontal_line') * columns + '\n')
    screen.addstr(config.get_parameter('horizontal_line') * columns)

config_file = config.get_config()

stdscr = curses.initscr()
rows, columns = stdscr.getmaxyx()

stdscr.clear()
stdscr.move(0, 0)
print_header(stdscr, columns, config_file)

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
    print_header(stdscr, columns, config_file)
    website = page.Page(url)
    website.load_page(config_file)
    stdscr.move(4, 0)
    website.display_page(stdscr)
    calls = website.get_special_calls()
    stdscr.refresh()
