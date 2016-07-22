import glob

import display
import world
from items import item

# Warrior equipment
from items import clothhat
from items import clothPants
from items import clothShirt
from items import okaySword
from items import UselessRingg
# Mage equipment
from items import wizardsHat
from items import magePants
from items import magerobe
from items import t1wand
# Thief equipment
from items import dagger
from items import fastHat
from items import fastShirt
from items import fastPants

from objects import player
from objects import world_object

from spells import heal
from spells import spell

def load_game():
    # Get all save files
    saves = glob.glob("res/saves/*.plr")
    # Parse res/saves/FILE.plr to just FILE. Much better for display, don't want the res/ for pickling.
    saves = [file[10:-4] for file in saves]
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
    display.clear()
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
        elif inpt != -1:
            display.printc(curs_loc + 30, 10, chr(inpt))
            file_name += chr(inpt)
            curs_loc += 1
        display.refresh()
        inpt = display.getch()
    # Wait for release
    while display.keyDown(display.CONST.VK_RETURN):
        pass
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
            hat = shirt = pants = weapon = None
            ring = item.item(UselessRingg.name, UselessRingg.type, UselessRingg.on_equip, UselessRingg.on_unequip, 1, UselessRingg.attributes)
            sp = spell.spell(heal.manaCost, heal.heal, heal.name, heal.icon, heal.color)
            pclass = ""
            if not choice: # Choice was 0, so warrior
                # Create player as warrior character
                # Their equipment
                hat = item.item(clothhat.name, clothhat.type, clothhat.on_equip, clothhat.on_unequip, 1, clothhat.attributes)
                shirt = item.item(clothShirt.name, clothShirt.type, clothShirt.on_equip, clothShirt.on_unequip, 1, clothShirt.attributes)
                pants = item.item(clothPants.name, clothPants.type, clothPants.on_equip, clothPants.on_unequip, 1, clothPants.attributes)
                weapon = item.item(okaySword.name, okaySword.type, okaySword.on_equip, okaySword.on_unequip, 1, okaySword.attributes)
                pclass = "warrior"
            if choice == 1: # Choice was Mage
                # Create player as mage.
                hat = item.item(wizardsHat.name, wizardsHat.type, wizardsHat.on_equip, wizardsHat.on_unequip, 1, wizardsHat.attributes)
                shirt = item.item(magerobe.name, magerobe.type, magerobe.on_equip, magerobe.on_unequip, 1, magerobe.attributes)
                pants = item.item(magePants.name, magePants.type, magePants.on_equip, magePants.on_unequip, 1, magePants.attributes)
                weapon = item.item(t1wand.name, t1wand.type, t1wand.on_equip, t1wand.on_unequip, 1, t1wand.attributes)
                pclass = "mage"
            if choice == 2: # Choice was Thief
                hat = item.item(fastHat.name, fastHat.type, fastHat.on_equip, fastHat.on_unequip, 1, fastHat.attributes)
                shirt = item.item(fastShirt.name, fastShirt.type, fastShirt.on_equip, fastShirt.on_unequip, 1, fastShirt.attributes)
                pants = item.item(fastPants.name, fastPants.type, fastPants.on_equip, fastPants.on_unequip, 1, fastPants.attributes)
                weapon = item.item(dagger.name, dagger.type, dagger.on_equip, dagger.on_unequip, 1, dagger.attributes)
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
                
            # Load starting world
            world.load("start")
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
                world.save_player()
                display.clear()
                return
            if opt == 2:
                display.end() # They chose exit

