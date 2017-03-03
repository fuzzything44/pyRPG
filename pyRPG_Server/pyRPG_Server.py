import multiprocessing as mp
#import Process, Queue
import select
import socket
import time
import sys
import importlib

import map as spawn_map
from objects import Player
import world

# Returns IP to bind to.
def ip():
    return 'localhost'
# Returns port to bind to.
def port():
    return 5000

# Starts map with given name.
def start_map(name):
    return 0

# Accepts connections, manages IPC, manages input
def connector(queue):
    # Make server socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serversocket.bind((ip(), port()))

    # maps is a dict from map_name to [get_queue, send_queue]
    maps = {}
    while True: # Main loop, connections are received, data is processed.
        # Check if we have readable data.

        # List of all players that need to be put in new maps. List of (mapname, player)
        move_requests = []

        can_read, can_write, errors = select.select([serversocket], [], [], 0)
        if can_read != []: # We have some data to process...
            (data, addr) = serversocket.recvfrom(65507) # Receive the data.
            plr_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # Socket player connects to.
            plr = world.load_player(data.decode('utf-8'))
            if plr is None:
                plr = Player.player.player(25, 7, plr_sock, addr, data.decode('utf-8'))  # New player object for request.
                print("[SV] New player connected")
                world.save_player(plr)
            else:
                plr.attributes["socket"] = plr_sock
                plr.attributes["address"] = addr
                print("[SV] Returning player connected")
            plr.X = plr.attributes["respawnX"]
            plr.Y = plr.attributes["respawnY"]
            move_requests.append((plr.attributes["respawnMap"], plr))

        if not queue.empty(): # Some owner input
            command = queue.get().split(' -')
            if command[0] == "end":
                serversocket.close() # End server
                for map, data in maps.items(): # End maps.
                    data[1].put(("end",))
                return
            elif command[0] == "mod":
                print("Modules loaded:" )
                for mod in sys.modules.keys():
                    if len(command) == 1 or command[1] in mod:
                        print(" ", mod)
            elif command[0] == "rel":
                try:
                    importlib.reload(sys.modules[command[1]])
                    print("Module reloaded")
                except Exception as ex:
                    print("Couldn't refresh module: ", ex)
            elif command[0] == "maps":
                print("Current maps:")
                for map in maps:
                    print(" ", map)

            elif command[0] == "stop":
                try:
                    maps[command[1]][1].put(("end",))
                    del maps[command[1]]
                except Exception as ex:
                    print("Couldn't end map: ", ex)
            elif command[0] == "help":
                print("Available commands:")
                print("  end : Ends the server.")
                print("  mod [-X]: Prints all modules loaded [with X in their name]")
                print("  rel -X: Reloads module X")
                print("  maps : Shows all current maps")
                print("  stop -X : Stops map X")
            else:
                print("Unknown command \"", command, '"')

        # Go through map queue input.
        
        to_close = [] # List of maps to close.
        for mapname, data in maps.items():
            while not data[0].empty():
                cmd = data[0].get() # Get command from map.
                if cmd[0] == "end": # Close map command
                    to_close.append(mapname) # Remove map, should have returned anyways.
                elif cmd[0] == "mov": # Move player command
                    move_requests.append(cmd[1]) # Add move request.

        for mapname in to_close: # Remove closed maps.
            maps[mapname][1].put(("end",)) # Send acknowledge of close
            del maps[mapname]
            print("[SV] " + mapname + " deleted")

        # Handle move requests. Should be in form of (map, object)
        for req in move_requests:
            print("[SV] Handling move request...")
            if req[0] in maps:          # Map currently exists
                maps[req[0]][1].put(("add", req[1]))
            else:                       # Map doesn't exist, add map
                name = req[0]
                get = mp.Queue()
                send = mp.Queue()
                proc = mp.Process(target=spawn_map.run_map, args=(name, send, get)) # Create map process
                send.put(("add", req[1]))
                proc.start()
                maps[name] = [get, send]    # Add map to list

        mp.active_children() # End any zombie processes. Just in case.


# Gives user input to the queue.
def inputter():
    input_queue = mp.Queue()
    proc = mp.Process(target=connector, args=(input_queue,))
    proc.start()
    while True:
        inpt = input()
        input_queue.put(inpt)
        if inpt == "end":
            return

if __name__ == "__main__":
    inputter()