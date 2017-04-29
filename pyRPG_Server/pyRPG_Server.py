import multiprocessing as mp
import select
import time
import sys
import importlib

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket

import map as spawn_map
from objects import Player
import world


# Returns port to bind to.
def port():
    return 5000

# Handles socket connections.
class sockethandler(tornado.websocket.WebSocketHandler):
    def __init__(self, application, request, **kwargs):
        (self.send_pipe, self.receive_pipe) = mp.Pipe() # Player socket is connected to.
        self.plr_name = None
        return super().__init__(application, request, **kwargs)

    def open(self):
        pass
        
    def on_message(self, message):
        if self.plr_name is None: # No player set, so must be username
            plr = world.load_player(message)
            if plr is None:
                plr = Player.player.player(50, 10, self.receive_pipe, self.send_pipe, message)
                world.save_player(plr)
            else:
                plr.attributes["send_pipe"] = self.receive_pipe
                plr.attributes["recv_pipe"] = self.send_pipe
            plr.X = plr.attributes["respawnX"]
            plr.Y = plr.attributes["respawnY"]
            global map_queue
            map_queue.put(("add", (plr.attributes["respawnMap"], plr)))
            self.plr_name = message
            # Now that we have the player
        else: # Player set, so some actual data. TODO: do stuff with the data.
            pass

    def on_close(self):
        print('connection closed')


    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', sockethandler),
])

map_queue = mp.Queue()

def map_manager(request_queue):
    maps = {}
    print("[SV] Map manager started")
    while True:
        move_requests = []
        to_close = [] # List of maps to close.

        # Check if there are requests
        if not request_queue.empty():
            cmd = request_queue.get()
            if cmd[0] == "add": # Add player command
                move_requests.append(cmd[1])
            elif cmd[0] == "del":
                if cmd[1] in maps:
                    maps[cmd[1]][1].put(("end,"))
                    del maps[cmd[1]]
                    print("[SV] " + cmd[1] + " deleted")
                else:
                    print("[SV] " + cmd[1] + " failed to delete: could not find map.")

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

# Accepts connections, manages IPC, manages input
def connector(queue):
        #    (data, addr) = serversocket.recvfrom(65507) # Receive the data.
        #    plr_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # Socket player connects to.
        #    plr = world.load_player(data.decode('utf-8'))
        #    if plr is None:
        #        plr = Player.player.player(25, 7, plr_sock, addr, data.decode('utf-8'))  # New player object for request.
        #        print("[SV] New player connected")
        #        world.save_player(plr)
        #    else:
        #        plr.attributes["socket"] = plr_sock
        #        plr.attributes["address"] = addr
        #        print("[SV] Returning player connected")
        #    plr.X = plr.attributes["respawnX"]
        #    plr.Y = plr.attributes["respawnY"]
        #    move_requests.append((plr.attributes["respawnMap"], plr))

        # Go through map queue input.
        pass


if __name__ == "__main__":
    # Start the websocket server
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port())
    myIP = socket.gethostbyname(socket.gethostname())

    mapmanager  = mp.Process(target=map_manager, name="pyRPG map manager", args=(map_queue,))
    mapmanager.start()

    print('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()