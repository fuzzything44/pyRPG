import display
import world
import socket
import select

def multiplayer(name):
    display.clear()
    display.draw_topbar()

    world.map = [[ world.WORLD_NOTHING for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(name, 'utf-8'), ('localhost', 5000))

    (data, new_addr) = sock.recvfrom(65507)

    # All coord pairs to overwrite.
    to_overwrite = []
    while True:
        if select.select([sock], [], [], 0) != ([], [], []):
            data, addr = sock.recvfrom(65507)
            while select.select([sock], [], [], 0) != ([], [], []):
                sock.recvfrom(65507)

            if data[0] == 0:
                for elem in to_overwrite:
                    display.printc(elem[0], elem[1], world.map[elem[0]][elem[1] - 5][2], world.map[elem[0]][elem[1] - 5][0])
                to_overwrite.clear()
                index = 1
                while index < len(data):
                    display.printc(data[index], 5 + data[index + 1], chr(data[index + 2]), data[index + 3])
                    to_overwrite.append((data[index], 5 + data[index + 1]))
                    index += 4

                display.refresh()

            # TODO: Actually fix this to do things
            if data[0] == 1: # Probably HP/MP display?
                pass
            if data[0] == 2: # Probably sidebar?
                pass
            if data[0] == 3: # Probably new map?
                pass
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
        to_send = bytearray(11)
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

        sock.sendto(to_send, new_addr)
