import itertools

import display
import world
import socket
import select
import pickle
import struct
import time

NEWMAP = 1
TO_INV = 2
# Double backslashes so when printing they actually print.
def make_chr(data):
    return chr(data) if chr(data) != "\\" else "\\\\"

def unpack_map(data):
    return [[ [data[(x + y * world.WORLD_X) * 3], data[(x + y * world.WORLD_X) * 3 + 1], make_chr(data[(x + y * world.WORLD_X) * 3 + 2])] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

# Returns number of bytes the utf-8 char will take. Byte is the first byte of the char
def unicode_bytes(byte):
    if byte < 0b10000000: # So a 0 in start position
        return 1
    elif byte < 0b11000000: # Not a single width, but less than a double width. Must be a continuing char.
        raise UnicodeDecodeError("Unexpected continuation character found")
    elif byte < 0b11100000: # Not continuing, not 3 width. So 2
        return 2
    elif byte < 0b11110000: # Not 4 width, not 2. So 3
        return 3
    return 4

def multiplayer():

    # Get username and password.
    display.clear()
    display.flushinp()
    inpt = display.getch()
    curs_loc = 0
    char_name = ""

    display.printc(30, 9, "Enter your name:")
    while inpt != 10: # Until ENTER pressed
        if inpt == 8: # Backspace
            if curs_loc != 0:
                curs_loc -= 1
                char_name = char_name[:-1] # Remove last character
            display.printc(curs_loc + 30, 10, ' ')
        elif (inpt != -1) and (curs_loc < 45) and (chr(inpt) in "abcdefghijklmnopqrtsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-1234567890 "): # Also don't let them get too long. 45 chosen arbitrarily because yeah.
            display.printc(curs_loc + 30, 10, chr(inpt))
            char_name += chr(inpt)
            curs_loc += 1
        display.refresh()
        inpt = display.getch()
    # Wait for release
    while display.keyDown(display.CONST.VK_RETURN):
        pass
    if char_name == len(char_name) * ' ':
        char_name = "default"

    curs_loc = 0
    password = ""

    inpt = display.getch()
    display.printc(30, 11, "Enter your Password:")
    while inpt != 10 or len(password) < 8: # Until ENTER pressed. 8 char password min.
        if inpt == 10 and len(password) < 8:
            display.printc(30, 13, "Passwords must be at least 8 characters.")
        elif inpt != -1:
            display.printc(30, 13, "                                        ")
        if inpt == 8: # Backspace
            if curs_loc != 0:
                curs_loc -= 1
                password = password[:-1] # Remove last character
            display.printc(curs_loc + 30, 12, ' ')
        elif (inpt != -1) and (curs_loc < 45) and (inpt < 127) and (inpt > 31): # Most characters allowed in password. Just has to be a printable ASCI
            display.printc(curs_loc + 30, 12, chr(inpt))
            password += chr(inpt)
            curs_loc += 1
        display.refresh()
        inpt = display.getch()
    # Wait for release
    while display.keyDown(display.CONST.VK_RETURN):
        pass



    display.clear()
    display.draw_topbar()
    display.refresh()

    world.map = [[ [0, 1, '!'] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    try:
        sock.sendto(bytes(char_name, 'utf-8'), ('localhost', 5000))
    
        (data, new_addr) = sock.recvfrom(65507)
        last_update = time.clock()

        # All coord pairs to overwrite.
        to_overwrite = []
    
        sidebar_lines = 0

        # ID of current map we're in. Useful for server.
        current_map = 0

        class states:
            WORLD = 0
            INVENTORY = 1

        class inventory: # Only one of these exists so we can just modify class stuff.
            class item:
                def __init__(this, name, desc, amount, value):
                    this.name = name
                    this.desc = desc
                    this.value = value
                    this.amount = amount

            selected_index = 0
            current_type = "weapon"

            weapons = []
            hats    = []
            shirts  = []
            pants   = []
            rings   = []
            consumables = []

            def str_to_list(string):
                return [inventory.weapons, inventory.hats, inventory.shirts, inventory.pants, inventory.rings, inventory.consumables][["weapon", "hat", "shirt", "pants", "ring", "consumable"].index(string)]           

            def clear(): # Clears entire inventory.
                inventory.weapons.clear()
                inventory.hats.clear()
                inventory.shirts.clear()
                inventory.pants.clear()
                inventory.rings.clear()
                inventory.consumables.clear()
            def add_item(data): # Adds an item based off of current data
                split_data = [bytearray(g) for k,g in itertools.groupby(data, lambda x: x == 0) if not k] # Data is packed as type, name, desc, amount, value. First 3 are null terminated strings
                type = split_data[0].decode('utf-8')
                name = split_data[1].decode('utf-8')
                desc = split_data[2].decode('utf-8')
                amount = struct.unpack("!I", data[len(data) - 8: len(data) - 4])[0] # Unpack last bytes.
                value = struct.unpack("!I", data[len(data) - 4: len(data)])[0]
                inventory.str_to_list(type).append(inventory.item(name, desc, amount, value))

        state = states.WORLD
        while True:
            # Let players force quit with Ctrl+Q
            if display.keyDown(display.CONST.VK_CONTROL) and display.keyDown(ord('Q')) or (time.clock() - last_update > 1.0):
                while display.keyDown(ord('Q')):
                    pass
                sock.close()
                return
    
            if select.select([sock], [], [], 0) != ([], [], []):
                data, addr = sock.recvfrom(65507)
                while select.select([sock], [], [], 0) != ([], [], []):
                    sock.recvfrom(65507)
                last_update = time.clock()

                if state == states.WORLD:
                    index = 1 # Current data index
                    if data[0] == NEWMAP:
                        current_map = data[index]
                        index += 1
                        map_size = struct.unpack("!I", data[index:index + 4])[0] # 4 bytes for size of map
                        index += 4
                        world.map = unpack_map(data[index: index + map_size]) 
                        index += map_size
                        world.dispworld()
                        display.refresh()
                    elif data[0] == TO_INV:
                        display.printc(0, 5, ((" " * 80) + "\n") * 25) # Should clear main screen.
                        # Now print out inventory.
                        display.printc(0, 5, "Inventory: \\fyWeapons(1)\\fw Hats(2) Shirts(3) Pants(4) Rings(5) Consumables(6)")
                        display.printc(0, 6, "Name/Description                                  Value          Amount")
                        display.printc(0, 7, '-' * 80)
                        inventory.clear() # Clear old inv data.
                        index = 1 # Current data index.
                        while index < len(data):                        
                            num_bytes = struct.unpack("!I", data[index: index + 4])[0] # Number of bytes in item
                            index += 4 # increment index
                            inventory.add_item(data[index: index + num_bytes]) # Add the item.
                            index += num_bytes

                        # Set last tracking vals
                        inventory.current_type = "weapon"
                        inventory.selected_index = 0
                        # Now print out inventory
                        display.printc(0, 8, ">") # Draw cursor.
  
                        loc = 8 # y location to print item at.
                        for itm in inventory.weapons: # Default to weapons
                            display.printc(1, loc, itm.name)
                            display.printc(50, loc, str(itm.value))
                            display.printc(65, loc, str(itm.amount))
                            display.printc(2, loc + 1, itm.desc)
                            loc += 2
                            if loc > 23: # Can't print more. So we get 12 items per sheet.
                                break
                        display.refresh()

                        state = states.INVENTORY
                        continue # Finish loop
                    # Here we do our updating
                    # So we need to redraw objects, HP/MP, gold, sidebar, and possibly equipment/spellbox/itembox
                    # Remove all previous objects
                    for elem in to_overwrite:
                        display.printc(elem[0], elem[1], world.map[elem[0]][elem[1] - 5][2], world.map[elem[0]][elem[1] - 5][0])
                    to_overwrite.clear()
    
                    num_objs = data[index]
                    index += 1
                    # Redraw all new objects
                    
                    while num_objs > 0:
                        x_loc = data[index]
                        y_loc = data[index + 1]
                        index += 2
                        char = data[index: index + unicode_bytes(data[index])].decode('utf-8') # Total char length for unicode char
                        index += unicode_bytes(data[index]) # Increment counter
                        color = data[index]
                        index += 1
                        display.printc(x_loc, 5 + y_loc, char, color, world.map[x_loc][y_loc][1])
                        to_overwrite.append((x_loc, 5 + y_loc))
                        num_objs -= 1
    
                    # Draw HP and MP
                    HP = struct.unpack("!I", data[index:index + 4])[0]
                    maxHP = struct.unpack("!I", data[index + 4 : index + 8])[0]
                    display.printc(8, 0, ' ' * 17)
                    display.printc(8, 0, str(HP) + "/" + str(maxHP))
                    index += 8

                    MP = struct.unpack("!I", data[index:index + 4])[0]
                    maxMP = struct.unpack("!I", data[index + 4 : index+8])[0]
                    display.printc(8, 1, ' ' * 17)
                    display.printc(8, 1, str(MP) + "/" + str(maxMP))
                    index += 8

                    # Draw level, EXP, gold:
                    level   = struct.unpack("!I", data[index: index + 4])[0]
                    exp     = struct.unpack("!I", data[index + 4: index + 8])[0]
                    gold    = struct.unpack("!I", data[index + 8: index + 12])[0]

                    display.printc(12, 3, str(level))
                    display.printc(5, 4, ' ' * 20)
                    display.printc(5, 4, str(int(exp)) + " to level")
                    display.printc(10, 2, ' ' * 15)
                    display.printc(10, 2, str(gold))
                    index += 12

                    # Print spell box, item box
                    spell_len = struct.unpack("!I", data[index: index + 4])[0]
                    index += 4
                    display.printc(display.SPELL_BOX_START + 1, 1, data[index: index + spell_len].decode('utf-8'))
                    index += spell_len

                    item_len = struct.unpack("!I", data[index: index + 4])[0]
                    index += 4
                    display.printc(display.ITEM_BOX_START + 1, 1, data[index: index + item_len].decode('utf-8'))
                    index += item_len

                    # Prints equipment
                    y_print = 0
                    
                    for equip in [display.WEAPON_X, display.HAT_X, display.SHIRT_X, display.PANTS_X, display.RING_X]:
                        equip_len = struct.unpack("!I", data[index : index + 4])[0]
                        index += 4
                        display.printc(equip, y_print, ' ' * 37)
                        display.printc(equip, y_print, data[index : index + equip_len].decode('utf-8'))
                        index += equip_len
                        y_print += 1

                    # Now, we see if we have sidebar stuff to print.
                    # So overwrite previous sidebar
                    for ind in range(sidebar_lines):
                        display.printc(50, ind + 5, ' ' * 30)

                    sidebar_length = struct.unpack("!I", data[index: index + 4])[0]
                    index += 4
                    display.printc(50, 5, data[index : index + sidebar_length].decode('utf-8'))
                    sidebar_lines = display.getyx(display.stdscr)[0] - 4 # We know how far down we printed by where the cursor is.
                    display.refresh()
            elif state == states.INVENTORY:
                # We can ignore data sent. So all we do is check kbd input and update based on that
                last_a = False
                if last_a and not display.keyDown(ord('A')):
                    display.printc(0, 0, 'B')
                if display.keyDown(ord('A')):
                    display.printc(0, 0, 'A')
                    last_a = True
                display.refresh()
    
            # Sends what keys are down.
            # Byte  Key
            # 0     W  
            # 1     A
            # 2     S
            # 3     D
            # 4     I
            # 5     J
            # 6     K
            # 7     L
            # 8     SHIFT 
            # 9     SPACE
            # 10    ENTER
            # 11    Q/UP
            # 12    E/DOWN
            # 13    U
            # 14    O
            # 15    ESC
            # 16    Special: Current map ID. Not actually a key. 

            to_send = bytearray(20)
            if state == states.WORLD: # Only send kbd input if we're in the world.
                to_send[0] = states.WORLD # Sending world input
                to_send[1] = display.keyDown(ord('W'))
                to_send[2] = display.keyDown(ord('A'))
                to_send[3] = display.keyDown(ord('S'))
                to_send[4] = display.keyDown(ord('D'))
                to_send[5] = display.keyDown(ord('I'))
                to_send[6] = display.keyDown(ord('J'))
                to_send[7] = display.keyDown(ord('K'))
                to_send[8] = display.keyDown(ord('L'))
                to_send[9] = display.keyDown(display.CONST.VK_LSHIFT)
                to_send[10] = display.keyDown(ord(' '))
                to_send[11]= display.keyDown(display.CONST.VK_RETURN)
                to_send[12]= display.keyDown(ord('Q')) or display.keyDown(display.CONST.VK_UP)
                to_send[13]= display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_DOWN)
                to_send[14]= display.keyDown(ord('E'))
                to_send[15]= display.keyDown(ord('U'))
                to_send[16]= display.keyDown(ord('O'))
                to_send[17]= display.keyDown(ord('V'))
                to_send[18]= display.keyDown(display.CONST.VK_ESCAPE)
                to_send[19] = current_map
            elif to_send == states.INVENTORY:
                to_send[0] = states.INVENTORY
            sock.sendto(to_send, new_addr)

    except ConnectionResetError as ex:
        sock.close()
        return
    except Exception as ex:
        return