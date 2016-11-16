from multiprocessing import Process, Queue
import select
import socket
import time

#TODO: Doing this wrong, should create a new socket for player to write to and put that in player object. This simplifies things.

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

    # Seconds to timeout.
    TIMEOUT = 5

    # Connections is a dict from address to [current_map_name, last_message]
    connections = {}

    # maps is a dict from map_name to [get_queue, send_queue, process]
    maps = {}
    while True: # Main loop, connections are received, data is processed.
        try:
            # List of all players that need to be put in new maps. List of (mapname, player)
            move_requests = []
            # Check if we have readable data.
            can_read, can_write, errors = select.select([serversocket], [], [], 0)
            if can_read != []: # We have some data to process...
                (data, addr) = serversocket.recvfrom(65507) # Receive the data.

                if addr not in connections: # New player connected
                    print("New player connected")
                    # Data should be the username.
                    data = data.decode('utf-8')
                    if data.isalnum: # Check for valid username.
                        # Connect player.
                        move_requests.append(("start", None)) # TODO: Actually load/create player if needed.
                        connections[addr] = ["start", time.clock()]
                else: # Existing player. Data should be kbd state.
                    plr_info = connections[addr]
                    plr_map = maps[plr_info[0]]         # The map they are in.
                    plr_map[1].put("upd", addr, data)   # Send update
                    plr_info[1] = time.clock()          # Update timeout
                    # TODO: Send data to right map... also make sure player is in correct map.
            if not queue.empty(): # Some owner input
                command = queue.get()
                if command == "end":
                    serversocket.close() # End server
                    for map, data in maps.items(): # End maps.
                        data[1].put(("end",))
                    return
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
                        move_requests.append((cmd[1], cmd[2])) # Add move request.
            for mapname in to_close: # Remove closed maps.
                del maps[mapname]
            
            # Handle move requests.
            for req in move_requests:
                pass # Handle request.

            # Check for timeouts.
            timeouts = []
            for conn, extra in connections.items():
                if time.clock() - extra[1] > TIMEOUT: # They timed out
                    timeouts.append[conn]
            for conn_lost in timeouts:
                # Kick player from map, kick from connection list.
                map = maps[connections[conn_lost][0]]
                map[1].put(("rmv", conn_lost))
                del connections[conn_lost]
        except ConnectionResetError:
            pass # Ignore error, it doesn't do anything.


# Gives user input to the queue.
def inputter():
    input_queue = Queue()
    proc = Process(target=connector, args=(input_queue,))
    proc.start()
    while True:
        inpt = input()
        input_queue.put(inpt)
        if inpt == "end":
            return

if __name__ == "__main__":
    inputter()