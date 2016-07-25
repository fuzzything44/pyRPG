from unicurses import *
from win32 import win32api
import win32con as CONST

def keyDown(key):
    return win32api.GetAsyncKeyState(key) & (1 << 15)

# Color definitions
WHITE = 0
RED = 1
BLUE = 2
CYAN = 3
GREEN = 4
MAGENTA = 5
YELLOW = 6

# Left side of the box where spell is drawn
SPELL_BOX_START = 25
def printc(x, y, ch, color = WHITE):
    "Prints a character at the given location with the given color.\n\nArguments:\nx: The x location to print the character\ny: The y location to print the character\nch: The character to print\ncolor: The color to print the character, default white\n\nBounds: String must end before reaching 79 along x-axis, must be before 24 on y-axis."
    if (x > 79 - len(ch)) or (y > 24) or (x < 0) or (y < 0):
        raise Exception("String out of bounds, shorten string or move left. Bounds are <= 79 on right, <= 23 on bottom, and >= 1 on top and left")
    if ('\n' in ch) or ('\r' in ch):
        raise Exception("No newlines in strings")
    mvaddstr(y, x, ch, COLOR_PAIR(color))
    
    

stdscr = 0      # Entire screen

def start():
    print("Starting init...")
    stdscr = initscr()
    noecho()
    nodelay(stdscr, True)
    
    if (has_colors() == False):
        endwin()
        print("Your terminal does not support color!")
        exit(1)
    
    start_color()
    init_pair(0, COLOR_WHITE, COLOR_BLACK)
    init_pair(1, COLOR_RED, COLOR_BLACK)
    init_pair(2, COLOR_BLUE, COLOR_BLACK)
    init_pair(3, COLOR_CYAN, COLOR_BLACK)
    init_pair(4, COLOR_GREEN, COLOR_BLACK)
    init_pair(5, COLOR_MAGENTA, COLOR_BLACK)
    init_pair(6, COLOR_YELLOW, COLOR_BLACK)
    
    curs_set(0)
    
    
def end():
    nodelay(stdscr, False)
    endwin()
    exit(0)


def menu(text, fn_params = [],  *opt_list):
    """Base menu template.

Arguments:
text: A string containing the introduction text to the menu
fn_params: A list of lists. fn_params[n] will be the list of arguments to be passed to opt_list[n]'s function if it has one.
*opt_list: A set of  [string, func] . The string is the displayed option, the func is function called if chosen.

Returns an int corresponding to the option chosen. Min of 0, max of (Num_options - 1)
"""
    substrs = text.split('\n')
    substrs.append('')
    line = 5
    while keyDown(ord('E')):
        getch()
    flushinp()
    for str in substrs:
        # Cut off strings if too long.
        str = str[:29]
        # Append proper spacing
        str = str + ' ' * (29 - len(str))
        printc(50,  line, str)
        line += 1
        if line > 24: # Overflowed screen
            key = getch()
            while key == -1: # Wait for keypress
                key = getch()
            for i in range(20): # Clear menu
                printc(50, i + 5, ' ' * 29)
            line = 5 # Reset line
    # Before displaying options, check if all can fit.
    if len(opt_list) > (24 - line): # overflowed screen
        key = getch()
        while key == -1: # Wait for keypress
            key = getch()
        for i in range(20): # Clear menu
            printc(50, i + 5, ' ' * 29)
        line = 5 # Reset line
    if len(opt_list) > 20: # Too long for one menu
        raise Exception("Menu Error: Too many options. Try to lower the amount.")
    
    # Finally can make menu
    menu_min = line # Can't go farther up than this.
    for opt in opt_list:
        # The [:28] is to slice the string as to not overflow the menu
        printc(51, line, opt[0][:28])
        line += 1
    menu_max = line # Can't get to this or above
    # Draw cursor
    printc(50, menu_min, '>')
    cursor_loc = menu_min
    can_W = True
    can_S = True
    while True:
        refresh()
        if keyDown(ord('W')) and can_W:
            if cursor_loc > menu_min:
                printc(50, cursor_loc, ' ')
                cursor_loc -= 1
                printc(50, cursor_loc, '>')
            can_W = False
        if not keyDown(ord('W')):
            can_W = True

        if keyDown(ord('S')) and can_S:
            printc(50, cursor_loc, ' ')
            cursor_loc += 1
            if cursor_loc == menu_max:  # Can't get to max...
                cursor_loc -= 1
            printc(50, cursor_loc, '>')
            can_S = False
        if not keyDown(ord('S')):
            can_S = True
        if (keyDown(CONST.VK_RETURN)) or (keyDown(ord('E'))):
            # Clear menu area
            for i in range(20): # Clear menu
                printc(50, i + 5, ' ' * 29)
            # Call function
            opt_list[cursor_loc - menu_min][1](*fn_params[cursor_loc - menu_min])
            while keyDown(ord('E')) or keyDown(CONST.VK_RETURN):
                pass
            return cursor_loc - menu_min
            


        
    
