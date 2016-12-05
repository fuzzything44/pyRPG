import display
import world
import socket
import select
import pickle
import struct


def multiplayer(name):
    display.clear()
    display.draw_topbar()

    world.map = [[ world.WORLD_NOTHING for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(bytes(name, 'utf-8'), ('localhost', 5000))
    
        (data, new_addr) = sock.recvfrom(65507)
    
        # All coord pairs to overwrite.
        to_overwrite = []
    
        sidebar_lines = 0

        # ID of current map we're in. Useful for server.
        current_map = 0
        while True:
            # Let players force quit with Ctrl+Q
            if display.keyDown(display.CONST.VK_CONTROL) and display.keyDown(ord('Q')):
                sock.close()
                return
    
            if select.select([sock], [], [], 0) != ([], [], []):
                data, addr = sock.recvfrom(65507)
                while select.select([sock], [], [], 0) != ([], [], []):
                    sock.recvfrom(65507)
    
                if data[0] == 0:
                    # Here we do our updating
                    # So we need to redraw objects, HP/MP, gold, sidebar, and possibly equipment/spellbox/itembox
                    # Remove all previous objects
                    for elem in to_overwrite:
                        display.printc(elem[0], elem[1], world.map[elem[0]][elem[1] - 5][2], world.map[elem[0]][elem[1] - 5][0])
                    to_overwrite.clear()
    
                    # Redraw all new objects
                    index = 2
                    while index < 4*data[1]:
                        display.printc(data[index], 5 + data[index + 1], chr(data[index + 2]), data[index + 3])
                        to_overwrite.append((data[index], 5 + data[index + 1]))
                        index += 4
    
                    # Draw HP and MP
                    HP = struct.unpack("!I", data[index:index + 4])[0]
                    maxHP = struct.unpack("!I", data[index + 4 : index+8])[0]
                    display.printc(8, 0, str(HP) + "/" + str(maxHP) + "  ")
                    index += 8

                    MP = struct.unpack("!I", data[index:index + 4])[0]
                    maxMP = struct.unpack("!I", data[index + 4 : index+8])[0]
                    display.printc(8, 1, str(MP) + "/" + str(maxMP) + "  ")
                    index += 8

                    # Now, we see if we have sidebar stuff to print.
                    # So overwrite previous sidebar
                    for index in range(sidebar_lines):
                        display.printc(50, index + 5, ' ' * 30)

                    sidebar_length = struct.unpack("!I", data[index: index + 4])[0]
                    index += 4
                    display.printc(50, 5, data[index : index + sidebar_length].decode('utf-8'))
                    sidebar_lines = display.getyx(display.stdscr)[0] - 5 # We know how far down we printed by where the cursor is.

                    display.refresh()
    
                else: # New map
                    current_map = data[1]
                    world.map = pickle.loads(data[2:])
                    world.dispworld()
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
            # 13    Special: Current map ID. Not actually a key. 
            to_send = bytearray(14)
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
            to_send[13]= current_map
    
            sock.sendto(to_send, new_addr)

    except:
        sock.close()
        return