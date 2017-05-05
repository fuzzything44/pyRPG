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
        (self.svr_pipe, self.plr_pipe) = mp.Pipe() # Player socket is connected to.
        self.plr_name = None
        self.timeout = None
        return super().__init__(application, request, **kwargs)

    def open(self):
        self.set_nodelay(True)
        self.timeout = tornado.ioloop.IOLoop.instance().add_timeout(0, self.update_client)

    def on_message(self, message):
        if self.plr_name is None: # No player set, so must be username
            plr = world.load_player(message)
            if plr is None:
                print("[SV] New player connected", message)
                plr = Player.player.player(25, 10, self.plr_pipe, message)
                world.save_player(plr)
            else:
                print("[SV] Returning player connected", message)
                plr.attributes["pipe"] = self.plr_pipe
            plr.X = plr.attributes["respawnX"]
            plr.Y = plr.attributes["respawnY"]
            global map_queue
            map_queue.put(("add", (plr.attributes["respawnMap"], plr)))
            self.plr_name = message
            # Now that we have the player
        else: # Player set, so some actual data. TODO: do stuff with the data.
            print("Got some sick data brah", message)
            self.svr_pipe.send(message)

    def update_client(self):
        # Get info from pipe, send it.
        while self.svr_pipe.poll():
            self.write_message(self.svr_pipe.recv())
        # Reset timeout
        self.timeout = tornado.ioloop.IOLoop.instance().add_timeout(tornado.ioloop.IOLoop.instance().time() + 1, self.update_client)

    def on_close(self):
        print('Connection closed', self.plr_name)
        tornado.ioloop.IOLoop.instance().remove_timeout(self.timeout)

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
                print("Move request", cmd[1])
                move_requests.append(cmd[1])
            elif cmd[0] == "del":
                if cmd[1] in maps:
                    maps[cmd[1]].send(("end,"))
                    del maps[cmd[1]]
                    print("[SV] " + cmd[1] + " deleted")
                else:
                    print("[SV] " + cmd[1] + " failed to delete: could not find map.")

        for mapname, pipe in maps.items():
            while pipe.poll():
                cmd = pipe.recv()   # Get command from map.
                if cmd[0] == "end": # Close map command
                    to_close.append(mapname) # Remove map, should have returned anyways.
                elif cmd[0] == "mov": # Move player command
                    move_requests.append(cmd[1]) # Add move request.

        for mapname in to_close: # Remove closed maps.
            maps[mapname].send(("end",)) # Send acknowledge of close
            del maps[mapname]
            print("[SV] " + mapname + " deleted")

        # Handle move requests. Should be in form of (map, object)
        for req in move_requests:
            print("[SV] Handling move request...")
            if req[0] in maps:          # Map currently exists
                print("Map exists")
                maps[req[0]].send(("add", req[1]))
            else:                       # Map doesn't exist, add map
                print("Adding map")
                name = req[0]
                (svr_pipe, map_pipe) = mp.Pipe()
                proc = mp.Process(target=spawn_map.run_map, args=(name, map_pipe)) # Create map process
                import pickle
                svr_pipe.send(("add", req[1]))
                proc.start()
                maps[name] = svr_pipe    # Add map to list

        mp.active_children() # End any zombie processes. Just in case.


if __name__ == "__main__":
    # Start the websocket server
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port())
    myIP = socket.gethostbyname(socket.gethostname())

    mapmanager  = mp.Process(target=map_manager, name="pyRPG map manager", args=(map_queue,))
    mapmanager.start()

    print('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
