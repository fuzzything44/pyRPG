import display
import world
import socket
import select
import pickle
import struct
import time

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

def multiplayer(name):
    display.clear()
    display.draw_topbar()
    display.refresh()

    world.map = [[ world.WORLD_NOTHING for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    try:
        sock.sendto(bytes(name, 'utf-8'), ('localhost', 5000))
    
        (data, new_addr) = sock.recvfrom(65507)
        last_update = time.clock()

        # All coord pairs to overwrite.
        to_overwrite = []
    
        sidebar_lines = 0

        # ID of current map we're in. Useful for server.
        current_map = 0
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

                index = 1 # Current data index
                if data[0] == 1:
                    current_map = data[index]
                    index += 1
                    map_size = struct.unpack("!I", data[index:index + 4])[0] # 4 bytes for size of map
                    index += 4
                    world.map = pickle.loads(data[index:index + map_size])
                    index += map_size
                    world.dispworld()
                    display.refresh()

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

            to_send = bytearray(17)
            to_send[0] = display.keyDown(ord('W'))
            to_send[1] = display.keyDown(ord('A'))
            to_send[2] = display.keyDown(ord('S'))
            to_send[3] = display.keyDown(ord('D'))
            to_send[4] = display.keyDown(ord('I'))
            to_send[5] = display.keyDown(ord('J'))
            to_send[6] = display.keyDown(ord('K'))
            to_send[7] = display.keyDown(ord('L'))
            to_send[8] = display.keyDown(display.CONST.VK_LSHIFT)
            to_send[9] = display.keyDown(ord(' '))
            to_send[10]= display.keyDown(display.CONST.VK_RETURN)
            to_send[11]= display.keyDown(ord('Q')) or display.keyDown(display.CONST.VK_UP)
            to_send[12]= display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_DOWN)
            to_send[13]= display.keyDown(ord('U'))
            to_send[14]= display.keyDown(ord('O'))
            to_send[15]= display.keyDown(display.CONST.VK_ESCAPE)
            to_send[16]= current_map
    
            sock.sendto(to_send, new_addr)

    except ConnectionResetError as ex:
        sock.close()
        return
    except Exception as ex:
        pause