import display
import world

def load_game():
    pass

   
def new_game():
    # What color each class should be
    color_list = [display.RED, display.BLUE, display.YELLOW]
    # What the middle text is for each class
    text_list = ["+  Warrior   +", "+    Mage    +", "+   Thief    +"]
    # The box of '+'s top and bottom
    box = '+' * 14

    # Number of rows each box takes up. 3 for the box + 2 for the space below
    box_size = 5
    # Where the boxes start display on y-axis
    box_start = 5
    # Left side of boxes
    box_left = 32
    # Clear screen and set up menu.
    display.clear()
    display.printc(box_left, box_start, box, color_list[0])
    display.printc(box_left, box_start + 1, text_list[0], color_list[0])
    display.printc(box_left, box_start + 2, box, color_list[0])


    display.printc(box_left, box_start + box_size, box)
    display.printc(box_left, box_start + box_size + 1, text_list[1])
    display.printc(box_left, box_start + box_size + 2, box)

    display.printc(box_left, box_start + 2 * box_size, box)
    display.printc(box_left, box_start + 2 * box_size + 1, text_list[2])
    display.printc(box_left, box_start + 2 * box_size + 2, box)
    
    
    choice = 0;

    display.refresh()
    while True:
        # Check for choice down/up
        if display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP):
            # Redraw current box in white
            display.printc(box_left, box_start + choice * box_size, box)
            display.printc(box_left, box_start + choice * box_size + 1, text_list[choice])
            display.printc(box_left, box_start + choice * box_size + 2, box)
            # If decrementing choice would bring it below zero, set it to one past last
            if choice == 0:
                choice = len(text_list)
            # And decrement it.
            choice -= 1

            # Redraw new box in correct color.
            display.printc(box_left, box_start + choice * box_size, box, color_list[choice])
            display.printc(box_left, box_start + choice * box_size + 1, text_list[choice], color_list[choice])
            display.printc(box_left, box_start + choice * box_size + 2, box, color_list[choice])
            # Refresh display
            display.refresh()
            # Wait for release
            while display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP):
                pass
        if display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN):
            # Redraw current box in white
            display.printc(box_left, box_start + choice * box_size, box)
            display.printc(box_left, box_start + choice * box_size + 1, text_list[choice])
            display.printc(box_left, box_start + choice * box_size + 2, box)
            # Go down
            choice += 1
            # Wrap options
            if choice == len(text_list):
                choice = 0
            # Redraw new box in correct color.
            display.printc(box_left, box_start + choice * box_size, box, color_list[choice])
            display.printc(box_left, box_start + choice * box_size + 1, text_list[choice], color_list[choice])
            display.printc(box_left, box_start + choice * box_size + 2, box, color_list[choice])
            # Refresh display
            display.refresh()
            # Wait for release
            while display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN):
                pass

        # Check if they chose an option
        if display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_RETURN):
            return

def start():
    """Gives the main menu option to load a file, create a new file, or exit"""
    display.printc(28, 10, "Welcome to pyRPG!")
    display.printc(30, 11, ">Load a file")
    display.printc(31, 12, "New game")
    display.printc(31, 13, "Exit game")
    display.refresh()
    opt = 0
    while True:

        # Move cursor up if w or up key pressed
        if display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP):
            # Clear old cursor
            display.printc(30, opt + 11, ' ')
            opt -= 1
            if opt < 0:
                opt = 2
            # Redraw for good menu
            display.printc(30, opt + 11, '>')
            display.refresh()      
            # Wait for release
            while display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP):
                pass

        # Move cursor down if s or down key pressed
        if display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN):
            # Clear old cursor
            display.printc(30, opt + 11, ' ')
            opt += 1
            if opt > 2:
                opt = 0
            # Redraw for good menu
            display.printc(30, opt + 11, '>')
            display.refresh()      
            # Wait for release
            while display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN):
                pass

        # If they have e or enter pressed, they chose an option.
        if display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_RETURN):
            # Wait for key release
            while display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_RETURN):
                pass

            if opt == 0:
                load_game()
                display.clear()
                return
            if opt == 1:
                new_game()
                display.clear()
                return
            if opt == 2:
                display.end() # They chose exit

