from unicurses import *
import locale

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
#Equip locations
WEAPON_X = 39 + len("Weapon:")
WEAPON_Y = 0
HAT_X = 39 + len("Hat:")
HAT_Y = 1
SHIRT_X = 39 + len("Shirt:")
SHIRT_Y = 2
PANTS_X = 39 + len("Pants:")
PANTS_Y = 3
RING_X = 39 + len("Ring:")
RING_Y = 4

def chr_to_color(chr): # Gets the color corresponding to the given character
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

def printc(x, y, str, start_color = WHITE, start_bgcolor = BLACK):
    """Prints a string at the given location with the given color.

Arguments:
  x: The x location to print the string
  y: The y location to print the string
  ch: The string to print
  start_color: The color to print the string, default white
  start_bgcolor: The background color for the string, default black.

Special characters:
  To go on to a new line (and reset x location to given x), use a newline character(\\n).
  To set the foreground color, use \\fX, where X is the color to set it to.
  To set the background color, use \\bX, where X is the color to set it to.
"""

    color   = start_color
    bgcolor = start_bgcolor

    escaped       = False
    setting_color = False
    setting_bg    = False

    move(y, x) # Move to start printing.
    for chr in str:
        if getyx(stdscr)[1] < x:      # We wrapped to a new line.
            return                    # Just ignore the rest of the string
        if escaped: # Set color.
            if chr == '\\': # Print just the backslash.
                addstr(chr, COLOR_PAIR(color + bgcolor * 8))
            elif chr == 'b': # Set background color
                setting_bg = True
            elif chr == 'f': # Set foreground color
                setting_color = True
            else: # Unknown
                raise "Unknown escaped character '" + chr + "'."
            escaped = False
        elif setting_color:
            color = chr_to_color(chr)
            setting_color = False
        elif setting_bg:
            bgcolor = chr_to_color(chr)
            setting_bg = False
        else:
            if chr == '\n': # Reset to left position, next col.
                y += 1
                move(y, x)
            elif chr == '\\': # Escape character.
                escaped = True
            else: # Regular character.
                addstr(chr, COLOR_PAIR(color + bgcolor * 8))

    

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

current_menu = None

class menu:
    def update(this):
        """Updates the menu, returns None if no option selected, otherwise returns option."""
        if this._end_val != -1:
            return this._end_val

        display.printc(50, this._cursor, ' ')
        # Update
    
        # Move cursor up
        if this._can_up:
            if keyDown(CONST.VK_UP):
                # Go up in the menu.
                if this._page_opt == 0: # Top of page
                    if this._page != 0: # Go to prev page
                        this._page -= 1
                        # Redraw page
                        for i in range(this._opt_start, 50):
                            display.printc(50, i, ' ' * 29)
                        linecount = 0
                        for elem in this._pages[this._page]:
                            display.printc(51, linecount + this._opt_start, elem)
                            linecount += elem.count('\n') + 1
                        # Reset cursor, page loc stuff
                        this._page_opt = len(this._pages[this._page]) - 1
                        this._cursor = linecount + this._opt_start - 1 - this._pages[this._page][this._page_opt].count('\n')
                        this._opt -= 1
                else:
                    this._page_opt -= 1 # Track previous option
                    # Move cursor up proper amount of lines
                    this._cursor -= this._pages[this._page][this._page_opt].count('\n') + 1
                    this._opt -= 1      # Select previous option.
                this._can_up = False
        elif not keyDown(CONST.VK_UP):
            this._can_up = True
    
        # Move cursor down
        if this._can_down:
            if keyDown(CONST.VK_DOWN):
                # Go down in the menu.
                if this._page_opt == len(this._pages[this._page]) - 1: # Top of page
                    if this._page != len(this._pages) - 1: # Go to next page
                        this._page += 1
                        # Redraw page
                        for i in range(this._opt_start, 50):
                            display.printc(50, i, ' ' * 29)
                        linecount = 0
                        for elem in this._pages[this._page]:
                            display.printc(51, linecount + this._opt_start, elem)
                            linecount += elem.count('\n') + 1
                        # Reset cursor, page loc stuff
                        this._cursor = this._opt_start
                        this._page_opt = 0
                        this._opt += 1
    
                else:
                    # Move cursor up proper amount of lines
                    this._cursor += this._pages[this._page][this._page_opt].count('\n') + 1
                    this._page_opt += 1 # Track next option
                    this._opt += 1      # Select previous option.
                this._can_down = False
        elif not keyDown(CONST.VK_DOWN):
            this._can_down = True
    
        if keyDown(CONST.VK_RETURN):
            while keyDown(CONST.VK_RETURN):
                pass
            this._end_val = this._opt
            this.clear()
            return this._opt
        # Redraw cursor
        display.printc(50, this._cursor, '>')
    
    def redraw(this):
        # Redraws menu
        # Clear right pane
        this.clear()
        printc(50, 5, this._text) # Redraw description

        # Redraw current options.
        linecount = 0
        for elem in this._pages[this._page]:
            display.printc(51, linecount + this._opt_start, elem)
            linecount += elem.count('\n') + 1

    def __init__(this, text, *opt_list):
        """Starts a menu.
    
    Arguments:
    text: A string containing the introduction text to the menu
    *opt_list: A list of strings as options to display.
    
    Begins by displaying the text and initializing for future updatethis.() calls.
    """
        this._cursor    = 0     # Where cursor is currently
        this._pages     = [[]]  # All pages of options.
        this._opt_start = 0     # Top place cursor/options can go.
        this._page      = 0     # What page we're on
        this._opt       = 0     # What option we're on.
        this._page_opt  = 0     # Where we are on the page.
        this._can_up    = True  # They can go up
        this._can_down  = True  # They can go down
        this._end_val   = -1    # Not finished yet
        this._text      = text
        if text.count('\n') > 10: # Count lines of text
            raise BaseException("Menu Error: Too long of basic description. Be more concise.")
    
        this.clear()        # Clear so that menu is drawn nicely
        printc(50, 5, text)
        
        this._opt_start = 7 + text.count('\n') # What line we're printing on for options. 5 (start) + 1 (description) + extra description lines
            # + 1 (blank space after description)
    
        # Turn strings in opt_list to options
        PAGE_SIZE = 26 - this._opt_start # Max lines in a page
        pages = [[]] # List of pages, contains list of options.
        linecount = 0 # How many lines all our options take up so far.
    
        for opt in opt_list: 
            if linecount + opt.count('\n') + 1 >= PAGE_SIZE: # If overflow of page
                pages.append([]) # New page
                linecount = 0 # Haven't used any of it.
            pages[-1].append(opt) # Add option
            if len(pages) == 1: # Only print first page
                display.printc(51, linecount + this._opt_start, opt)
            linecount += opt.count('\n') + 1
    
    
        this._pages   = pages
        this._cursor  = this._opt_start

    def clear(this):
        for i in range(5, 25):
            display.printc(50, i, ' ' * 30)
    