from unicurses import *
from win32 import win32api
import win32con as CONST

import display

def keyDown(key):
    return (win32api.GetAsyncKeyState(key) & (1 << 15)) >> 15

# Color definitions
WHITE = 0
BLACK = 1
RED = 2
BLUE = 3
CYAN = 4
GREEN = 5
MAGENTA = 6
YELLOW = 7

# Left side of the box where spell is drawn
SPELL_BOX_START = 25
ITEM_BOX_START = 31

def printc(x, y, ch, color = WHITE, bgcolor = BLACK):
    "Prints a character at the given location with the given color.\n\nArguments:\nx: The x location to print the character\ny: The y location to print the character\nch: The character to print\ncolor: The color to print the character, default white\n\nBounds: String must end before reaching 79 along x-axis, must be before 24 on y-axis."
    if (x > 79 - len(ch)) or (y > 24) or (x < 0) or (y < 0):
        raise Exception("String out of bounds, shorten string or move left. Bounds are <= 79 on right, <= 23 on bottom, and >= 1 on top and left")
    if ('\n' in ch) or ('\r' in ch):
        raise Exception("No newlines in strings")
    mvaddstr(y, x, ch, COLOR_PAIR(color + bgcolor * 8))
    
    

stdscr = None      # Entire screen

def start():
    global stdscr
    print("Starting init...")
    stdscr = initscr()
    noecho()
    nodelay(stdscr, True)
    
    if (has_colors() == False):
        endwin()
        print("Your terminal does not support color!")
        exit(1)
        
    start_color()

  	# Init all foreground/background pairs
	# List of all colors
    color_list = [COLOR_WHITE, COLOR_BLACK, COLOR_RED, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN, COLOR_MAGENTA, COLOR_YELLOW]
    # Loop through background colors
    for bgc in range(len(color_list)):
        # Loop through foreground colors
        for fgc in range(len(color_list)):
            init_pair(fgc + 8 * bgc, color_list[fgc], color_list[bgc])
    
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

    # Intro text stuff.
    substrs = text.split('\n') # Split their intro text on lines.
    substrs.append('') # Add spacing line after intro text.
    line = 5 # Current line to print on
    while keyDown(ord('E')) or keyDown(CONST.VK_RETURN):
        pass
    flushinp()
    if len(substrs) > 10:
        raise Exception("Menu Error: Too long of basic description. Be more concise.")
    for str in substrs:
        # Cut off strings if too long.
        str = str[:29]
        # Append proper spacing
        str = str + ' ' * (29 - len(str))
        printc(50,  line, str)
        line += 1
    # Finished intro text


    # Format their options to be better.
    # Option class: can print itself, knows how many lines it is
    class option:
        def __init__(this, str, func): # str is the given string.
            this.function = func
            this.disps = [] # disps is all strings it will display
            curr_str = ""
            curr_index = 0 # How far we are along the screen. Can go to 28.
            curr_color = display.WHITE
            curr_line = 0
            
            setting_color = False
            for chr in str:
                if setting_color:
                    setting_color = False
                    if chr != '\\': # let them use \\ to just put a regular \
                        # Add the string. curr_index - len(curr_string) to get the start of the string, not the end.
                        this.disps.append([curr_index - len(curr_str), curr_line, curr_str, curr_color])
                        curr_str = "" # Reset string
                        curr_color = this.get_color(chr) # Set color to what they chose.
                    else:
                        curr_str += chr # Add the character to the string
                        curr_index += 1
                elif chr == '\\':
                    setting_color = True
                else:
                    if chr != '\n':
                        curr_str += chr # Add the character to the string.
                        curr_index += 1
                    if (curr_index == 28) or (chr == '\n'): # Max size or they wanted a new line
                        this.disps.append([curr_index - len(curr_str), curr_line, curr_str, curr_color])
                        curr_index = 1 # Add small indent
                        curr_str = ""
                        curr_line += 1
            this.disps.append([curr_index - len(curr_str), curr_line, curr_str, curr_color])
            this.lines = curr_line + 1 # Amount of lines it takes up.
            if this.lines > 7: # 7 chosen arbitrarily. It should be enough.
                raise Exception("Menu Error: Wayyy too long of an option. Really, over 7 lines?!")
        def disp(this, start_line):
            for elem in this.disps:
                # Elements have 4 variables: x location, line, text, color
                # Elements have to be shifted 51 on X-axis and start_line on Y-axis.
                display.printc(elem[0] + 51, elem[1] + start_line, elem[2], elem[3]) 

        def get_color(this, chr): # Gets the color corresponding to the given character
              if chr == 'r':
                 return display.RED
              if chr == 'g':
                  return display.GREEN
              if chr == 'b':
                  return display.BLUE
              if chr == 'c':
                  return display.CYAN
              if chr == 'm':
                  return display.MAGENTA
              if chr == 'y':
                  return display.YELLOW
              return display.WHITE # Just return white if unknown (or w)
        

    # Turn strings in opt_list to options
    PAGE_SIZE = 26 - line # Max options in a page
    pages = [[]] # List of pages, contains list of options.
    linecount = 0 # How many lines all our options take up.
    for opt in opt_list: 
        optn = option(opt[0], opt[1]) # Create option from their string
        if linecount + optn.lines >= PAGE_SIZE: # If overflow of page
            pages.append([]) # New page
            linecount = 0 # Haven't used any of it.
        pages[-1].append(optn) # Add option
        linecount += optn.lines
        
    curr_page = 0
    choice = 0
    menu_min = line # Can't go farther up than this.

    # Display first page
    # Start by clearing area.
    for index in range(menu_min, 25):
        display.printc(50, index, ' ' * 29)
    for optn in pages[curr_page]: # Display everything
        optn.disp(line)
        line += optn.lines

    # Draw cursor
    printc(50, menu_min, '>')
    cursor_loc = menu_min
    can_W = True
    can_S = True
    while True:
        refresh()
        if (keyDown(ord('W')) or keyDown(CONST.VK_UP)) and can_W:
            if choice > 0:
                printc(50, cursor_loc, ' ')
                choice -= 1
                cursor_loc -= pages[curr_page][choice].lines
                printc(50, cursor_loc, '>')
            elif curr_page > 0: # They can go to a lesser page
                curr_page -= 1 # Go to prev page
                cursor_loc = menu_min
                for index in range(menu_min, 25): # Clear menu area
                    display.printc(50, index, ' ' * 29)
                for optn in pages[curr_page]: # Display everything
                    optn.disp(cursor_loc)
                    cursor_loc += optn.lines
                choice = len(pages[curr_page]) - 1
                cursor_loc -= pages[curr_page][-1].lines
                display.printc(50, cursor_loc, '>')

            can_W = False
        if not (keyDown(ord('W')) or keyDown(CONST.VK_UP)):
            can_W = True

        if (keyDown(ord('S')) or keyDown(CONST.VK_DOWN)) and can_S:
            if choice < len(pages[curr_page]) - 1:
                printc(50, cursor_loc, ' ')
                cursor_loc += pages[curr_page][choice].lines
                choice += 1
                printc(50, cursor_loc, '>')
            elif len(pages) - 1 > curr_page:
                curr_page += 1 # Go to prev page
                cursor_loc = menu_min
                for index in range(menu_min, 25): # Clear menu area
                    display.printc(50, index, ' ' * 29)
                for optn in pages[curr_page]: # Display everything
                    optn.disp(cursor_loc)
                    cursor_loc += optn.lines
                choice = 0
                cursor_loc = menu_min
                display.printc(50, cursor_loc, '>')

            can_S = False
        if not (keyDown(ord('S')) or keyDown(CONST.VK_DOWN)):
            can_S = True
        if (keyDown(CONST.VK_RETURN)) or (keyDown(ord('E'))):
            # Clear menu area
            for i in range(20): # Clear menu
                printc(50, i + 5, ' ' * 29)
            # Call function
            pages[curr_page][choice].function(*fn_params[choice])
            while (keyDown(ord('E')) or keyDown(CONST.VK_RETURN)):
                pass
            # Since non-uniform page length, must add all page sizes to get what they chose
            opt_chosen = 0
            for index in range(curr_page):
                opt_chosen += len(pages[index]) # Add length of page
            return opt_chosen + choice
