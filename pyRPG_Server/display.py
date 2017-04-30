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

# Key defs
KEY_MOV_UP      = 0
KEY_MOV_LEFT    = 1
KEY_MOV_DOWN    = 2
KEY_MOV_RIGHT   = 3

KEY_ATK_UP      = 4
KEY_ATK_LEFT    = 5
KEY_ATK_DOWN    = 6
KEY_ATK_RIGHT   = 7

KEY_ITEM        = 8
KEY_SPELL       = 9
KEY_ENTER       = 10

KEY_UP = 11
KEY_DOWN = 12

KEY_INTERACT    = 13

KEY_LASTSPELL   = 14
KEY_NEXTSPELL   = 15

KEY_INVENTORY   = 16
KEY_ESC  = 17

# How many keys there are.
NUM_KEYS = 18

def chr_to_color(chr): # Gets the color corresponding to the given character
      if chr == 'r':
         return RED
      if chr == 'g':
          return GREEN
      if chr == 'b':
          return BLUE
      if chr == 'c':
          return CYAN
      if chr == 'm':
          return MAGENTA
      if chr == 'y':
          return YELLOW
      return WHITE # Just return white if unknown (or w)

def add_newlines(st, maxlen = 29):
  "Adds new lines in the middle of a string to make it fit in a specific size" 
  arr = st.split(' ')
  ret = ''
  length = 0
  for elem in arr:
    if len(elem) + 1 > maxlen:
      raise Exception("Too long of word" + elem)
      
    if len(elem) + 1 + length > maxlen:
      ret += "\n "
      length = 0
      
    if length != 0:
      length += 1
      ret += " "
      
    length += len(elem)
    ret += elem
    
  return ret
  

class menu:
    def update(this):
        """Updates the menu, returns None if no option selected, otherwise returns option."""
        if this._end_val != -1:
            return this._end_val

        # If enter key was down
        if this._ending:
            # If released, finish menu
            if not this._player.attributes["keys"][KEY_ENTER]:
                this._end_val = this._opt
                return this._opt
            # Still pressed. Ignore all other input
            return

        # Player has ESC menu up and this isn't it.
        if this._player.attributes["esc_menu"] is not None and not this.is_esc_menu:
            return

        # Update
    
        # Move cursor up
        if this._can_up:
            if this._player.attributes["keys"][KEY_UP]:
                # Go up in the menu.
                if this._page_opt == 0: # Top of page
                    if this._page != 0: # Go to prev page
                        this._page -= 1
                        linecount = 0
                        for elem in this._pages[this._page]:
                            linecount += elem.count('\n') + 1
                        # Reset page loc stuff
                        this._page_opt = len(this._pages[this._page]) - 1
                        this._opt -= 1
                else:
                    this._page_opt -= 1 # Track previous option
                    this._opt -= 1      # Select previous option.
                this._can_up = False
        elif not this._player.attributes["keys"][KEY_UP]:
            this._can_up = True
    
        # Move cursor down
        if this._can_down:
            if this._player.attributes["keys"][KEY_DOWN]:
                # Go down in the menu.
                if this._page_opt == len(this._pages[this._page]) - 1: # Top of page
                    if this._page != len(this._pages) - 1: # Go to next page
                        this._page += 1
                        linecount = 0
                        for elem in this._pages[this._page]:
                            linecount += elem.count('\n') + 1
                        # Reset  page loc stuff
                        this._page_opt = 0
                        this._opt += 1
    
                else:
                    this._page_opt += 1 # Track next option
                    this._opt += 1      # Select previous option.
                this._can_down = False
        elif not this._player.attributes["keys"][KEY_DOWN]:
            this._can_down = True
    
        if this._player.attributes["keys"][KEY_ENTER]:
            this._ending = True
    
    def __init__(this, text, player, *opt_list):
        """Starts a menu.
    
    Arguments:
    text: A string containing the introduction text to the menu
    *opt_list: A list of strings as options to display.
    
    Begins by displaying the text and initializing for future updatethis.() calls.
    """
        this._pages     = [[]]  # All pages of options.
        this._page      = 0     # What page we're on
        this._opt       = 0     # What option we're on.
        this._page_opt  = 0     # Where we are on the page.
        this._can_up    = True  # They can go up
        this._can_down  = True  # They can go down
        this._end_val   = -1    # Not finished yet
        this._text      = text
        this._player    = player
        this._ending    = False # End when enter key is pressed
        this.is_esc_menu= False # So when moving through esc menus normal ones don't also update.
        if text.count('\n') > 10: # Count lines of text
            raise BaseException("Menu Error: Too long of basic description. Be more concise.")
    
        # Turn strings in opt_list to options
        PAGE_SIZE = 19 - text.count('\n') # Max lines in a page
        pages = [[]] # List of pages, contains list of options.
        linecount = 0 # How many lines all our options take up so far.
    
        for opt in opt_list: 
            if linecount + opt.count('\n') + 1 >= PAGE_SIZE: # If overflow of page
                pages.append([]) # New page
                linecount = 0 # Haven't used any of it.
            pages[-1].append(opt) # Add option
            linecount += opt.count('\n') + 1
    
    
        this._pages   = pages

    def disp(this):
        disp_str = this._text
        opt = 0
        for text in this._pages[this._page]:
            if opt == this._page_opt:
                disp_str += '\n>' + text
            else:
                disp_str += '\n ' + text
            opt += 1

        return disp_str