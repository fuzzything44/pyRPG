import copy
import glob

import display
import world
from items import item
from items import start as start_eq

from objects.Player import player
from objects import world_object

from spells import heal
from spells import spell

def load_game():
    display.clear()
    # Get all save files
    saves = glob.glob("res/saves/*.plr")
    # Parse res/saves/FILE.plr to just FILE. Much better for display, don't want the res/ for pickling.
    saves = [file[10:-4] for file in saves]
    if len(saves) == 0:
        display.printc(30, 8, "No saves were found...")
        display.flushinp()
        while display.getch() == -1:
            pass
        display.end()
    # Break saves into pages.
    PAGE_SIZE = 25
    pages = [[]]
    for opt in saves:             # Add every object to the list.
        if len(pages[-1]) == PAGE_SIZE:    # If list overflow, add a new page
            pages.append([])
        # Add option to last element in pages. Also should edits it to give amount held too.
        pages[-1].append(opt)

    curr_page = 0
    choice = 0
    # Display first page
    for index in range(len(pages[curr_page])):
        display.printc(10, index, pages[curr_page][index]) # Print out the option

    display.printc(9, 0, '>') # Cursor
    display.refresh()
    can_up = True
    can_down = True
    while True: # Now loop and wait for a choice
        if (display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP)) and can_up:
            # Go up 1.
            display.printc(9, choice, ' ') # Remove old arrow
            if choice == 0: # Already at top of page. 
                if curr_page == 0:
                    curr_page = len(pages) - 1 # Go to last page
                else:
                    # Go up a page
                    curr_page -= 1
                choice = len(pages[-1]) # Go to bottom of page
                display.clear() # Clear all the old stuff.
                for index in range(len(pages[curr_page])): # Draw the new page
                    display.printc(10, index, pages[curr_page][index]) # Print out the option

            choice -= 1 # Go up 1.
            display.printc(9, choice, '>') # Redraw arrow
            display.refresh() # Refresh screen
            can_up = False
        if not (display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP)):
            can_up = True
        if (display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN)) and can_down:
            # Go down 1.
            display.printc(9, choice, ' ') # Remove old arrow
            if choice == len(pages[curr_page]) - 1: # Already at bottom of page. 
                if curr_page == len(pages) - 1:
                    curr_page = 0 # Go to first page
                else:
                    # Go down a page
                    curr_page += 1
                choice = -1 # Go to top of page
                display.clear() # Clear all the old stuff.
                for index in range(len(pages[curr_page])): # Draw the new page
                    display.printc(10, index, pages[curr_page][index]) # Print out the option

            choice += 1 # Go down 1.
            if choice == len(pages[curr_page]):
                choice -= 1 # At bottom, can't go down
            display.printc(9, choice, '>') # Redraw arrow
            display.refresh() # Refresh screen
            can_down = False
        if not (display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN)):
            can_down = True

        # TODO: Possibly let them easily skip through pages with AD and left/right arrow keys
    
        if display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_RETURN):
            file = pages[curr_page][choice]
            world.load_player(file)
            return

def new_game():
    # Get their save name
    display.clear()
    display.flushinp()
    inpt = display.getch()
    curs_loc = 0
    file_name = ""

    display.printc(30, 9, "Enter your name:")
    while inpt != 10: # Until ENTER pressed
        if inpt == 8: # Backspace
            if curs_loc != 0:
                curs_loc -= 1
                file_name = file_name[:-1] # Remove last character
            display.printc(curs_loc + 30, 10, ' ')
        elif (inpt != -1) and (curs_loc < 45) and (chr(inpt) in "abcdefghijklmnopqrtsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-1234567890 "): # Also don't let them get too long. 45 chosen arbitrarily because yeah.
            display.printc(curs_loc + 30, 10, chr(inpt))
            file_name += chr(inpt)
            curs_loc += 1
        display.refresh()
        inpt = display.getch()
    # Wait for release
    while display.keyDown(display.CONST.VK_RETURN):
        pass
    if file_name == len(file_name) * ' ':
        file_name = "default"
    world.save_name = file_name
    # Class select!
    # What color each class should be
    color_list = [display.RED, display.BLUE, display.YELLOW]
    # What the middle text is for each class
    text_list = ["+  Warrior   +", "+    Mage    +", "+   Thief    +"]
    # The box of '+'s top and bottom
    box = '+' * 14

    # Number of rows each box takes up. 3 for the box + 2 for the space below
    box_size = 5
    # Where the boxes start display on y-axis
    box_start = 4
    # Left side of boxes
    box_left = 32
    # Clear screen and set up menu.
    display.clear()
    for i in range(len(text_list)):
        display.printc(box_left, box_start + i * box_size, box)
        display.printc(box_left, box_start + i * box_size + 1, text_list[i])
        display.printc(box_left, box_start + i * box_size + 2, box)

    # Draw first box in color
    display.printc(box_left, box_start, box, color_list[0])
    display.printc(box_left, box_start + 1, text_list[0], color_list[0])
    display.printc(box_left, box_start + 2, box, color_list[0])

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
            # Basic player. Choice will modify it's attributes.
            world.player = world_object.world_object(player.player_update, player.collide, player.player_char, player.player_color, "player", 0, 0, player.player_attributes)
            
            hat =    item.item(start_eq.hat_name   , start_eq.hat_type   , start_eq.hat_on_equip   , start_eq.hat_on_unequip   , 1, copy.deepcopy(start_eq.hat_attributes   ))
            shirt =  item.item(start_eq.shirt_name , start_eq.shirt_type , start_eq.shirt_on_equip , start_eq.shirt_on_unequip , 1, copy.deepcopy(start_eq.shirt_attributes ))
            pants =  item.item(start_eq.pants_name , start_eq.pants_type , start_eq.pants_on_equip , start_eq.pants_on_unequip , 1, copy.deepcopy(start_eq.pants_attributes ))
            weapon = item.item(start_eq.weapon_name, start_eq.weapon_type, start_eq.weapon_on_equip, start_eq.weapon_on_unequip, 1, copy.deepcopy(start_eq.weapon_attributes))
            ring =   item.item(start_eq.ring_name  , start_eq.ring_type  , start_eq.ring_on_equip  , start_eq.ring_on_unequip  , 1, copy.deepcopy(start_eq.ring_attributes  ))
            sp = spell.spell(heal.manaCost, heal.heal, heal.name, heal.icon, heal.color)
            pclass = ""
            if not choice: # Choice was 0, so warrior
                pclass = "warrior"
            if choice == 1: # Choice was Mage
                pclass = "mage"
            if choice == 2: # Choice was Thief
                pclass = "thief"

            world.player.attributes["class"] = pclass
            world.player.attributes["items"] = [hat, shirt, pants, ring, weapon, sp] # Give them their equips
            world.player.attributes["hat"] = hat
            hat.equip(hat, world.player)
            world.player.attributes["shirt"] = shirt
            shirt.equip(shirt, world.player)
            world.player.attributes["pants"] = pants
            pants.equip(pants, world.player)
            world.player.attributes["ring"] = ring
            ring.equip(ring, world.player)
            world.player.attributes["weapon"] = weapon
            weapon.equip(weapon, world.player)
            world.player.attributes["spell"] = sp
            
            # Set starting coords
            world.player.X = world.WORLD_X // 2
            world.player.Y = world.WORLD_Y - 3
            # Load starting world
            world.load("start")
            world.objects = [world.player] + world.objects
            return

def help_menu():
    display.clear()
    display.printc(0, 0,  "pyRPG is a real-time terminal based RPG")
    display.printc(0, 4,  "In a menu, use either the UP ARROW key or the W key to move your cursor up")
    display.printc(0, 5,  "Use either the DOWN ARROW key or the S key to move your cursor down")
    display.printc(0, 6,  "Use either the ENTER key or the E key to select the current option")
    display.printc(0, 9,  "In game controls:")
    display.printc(0, 10, "Use WASD to move and IJKL to attack directionally")
    display.printc(0, 11, "Press SPACE to cast your current spell, set in the Spell menu")
    display.printc(0, 12, "Press LEFT SHIFT to use your item, set in the Consumable menu of your inventory")
    display.printc(0, 13, "Press ESC to open the main menu to save, access inventory, set spell, or exit")
    display.printc(0, 15, "Press ENTER to go to page two or press ESC to exit to the main menu")
    display.refresh()
    while (not display.keyDown(display.CONST.VK_ESCAPE)) and (not display.keyDown(display.CONST.VK_RETURN)):
        pass # Wait for press of ESC or ENTER
    if display.keyDown(display.CONST.VK_ESCAPE):
        while display.keyDown(display.CONST.VK_ESCAPE):
            pass # Wait for release
        return
    while display.keyDown(display.CONST.VK_RETURN):
        pass # Wait for release
    # Now give page 2 of the menu.
    display.clear()
    display.printc(0, 0, "Colors and symbols guide:")
    display.printc(0, 2, "Colors:")

    display.printc(0, 3, "Red", display.RED)
    display.printc(4, 3, "is either a locked portal ( ) or an obstacle. Often,     objects hurt.")
    display.printc(31, 3, "O", display.RED)
    display.printc(57, 3, "red", display.RED)

    display.printc(0, 4, "White objects tend to be neutral. Walls (#) and floors (.) tend to be white.")
    
    display.printc(0, 5, "Blue", display.BLUE)
    display.printc(5, 5, "objects are often portals ( ). Also, player attacks ( ) are blue.")
    display.printc(32, 5, "O", display.BLUE)
    display.printc(58, 5, "!", display.BLUE)

    display.printc(0, 6, "Cyan", display.CYAN)
    display.printc(5, 6, "objects are enemies. All enemies are      and all      things are enemies.")
    display.printc(42, 6, "cyan", display.CYAN)
    display.printc(55, 6, "cyan", display.CYAN)

    display.printc(0, 7, "Green", display.GREEN)
    display.printc(6, 7, "tends not to be used. Grass ( ) is       but it is not otherwise used.")
    display.printc(35, 7, ';', display.GREEN)
    display.printc(41, 7, "green", display.GREEN)

    display.printc(0, 8, "Magenta", display.MAGENTA)
    display.printc(8, 8, "tends not to be used. Enemy attacks ( ) are        .")
    display.printc(45, 8, "!", display.MAGENTA)
    display.printc(52, 8, "magenta", display.MAGENTA)

    display.printc(0, 9, "Yellow", display.YELLOW)
    display.printc(7, 9, "is loot! Money ( ) and chests ( ) are       .        things are good.")
    display.printc(23, 9, "$", display.YELLOW)
    display.printc(38, 9, "@", display.YELLOW)
    display.printc(45, 9, "yellow", display.YELLOW)
    display.printc(53, 9, "Yellow", display.YELLOW)

    display.printc(0, 11, "Common Symbols:")
    display.printc(0, 13, "# is a wall. Walls block movement of the player, attacks, and enemies.")
    display.printc(0, 14, ". is a common ground tile. It does nothing special.")
    display.printc(0, 15, "#", display.RED)
    display.printc(2, 15, "is lava. Stepping on it hurts!")
    display.printc(0, 16, ';', display.GREEN)
    display.printc(2, 16, "is a common ground tile. It does nothing special.")

    display.printc(0, 20, "These are common trends and there are objects that break these trends.")
    display.printc(0, 21, "However, they hold true for most objects that you will encounter.")
    display.printc(0, 22, "Also, the rule about cyan objects ALWAYS holds.")
    display.printc(21, 22, "cyan", display.CYAN)

    display.refresh()
    while not display.keyDown(display.CONST.VK_RETURN):
        pass
    while display.keyDown(display.CONST.VK_RETURN):
        pass
    return

def start():
    """Gives the main menu option to load a file, create a new file, or exit"""
    display.printc(28, 10, "Welcome to pyRPG!")
    display.printc(30, 11, ">Load a file")
    display.printc(31, 12, "New game")
    display.printc(31, 13, "Exit game")
    display.printc(28, 15, "Press H for help")
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
                world.player.attributes["HP"] = world.player.attributes["maxHP"]
                world.player.attributes["MP"] = world.player.attributes["maxMP"]
                world.save_player()
                display.clear()
                return
            if opt == 2:
                display.end() # They chose exit

        # They need help!
        if display.keyDown(ord('H')):
            help_menu()
            display.clear()
            display.printc(28, 10, "Welcome to pyRPG!")
            display.printc(31, 11, "Load a file")
            display.printc(31, 12, "New game")
            display.printc(31, 13, "Exit game")
            display.printc(28, 15, "Press H for help")
            display.printc(30, opt + 11, '>')
            display.refresh()



