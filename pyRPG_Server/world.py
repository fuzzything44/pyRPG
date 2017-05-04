import pickle
import json as JSON

import display

# World tile. Form of [foreground color, background color, display char, canwalk]. None of this should move, all is part of background world.
WORLD_NOTHING = [0, 1, ' ', True]     # Nothing there

WORLD_X = 50    # Max X size
WORLD_Y = 20    # Max Y size

map = [[ WORLD_NOTHING for y in range(WORLD_Y)] for x in range(WORLD_X)]

send_data = ""

players = []

objects = []    # World objects that can interacted with such as enemies, chests, etc...
to_del = []     # Objects that should be deleted.
to_del_plr = []

move_requests = [] # Requests to move players

dungeon_state = {} # Dict of var_name to value, for tracking various values in dungeons.
dungeon_state_diff = {} # For when stuff wants to change dungeon_state.

def out_of_bounds(x, y):
    return (y < 0) or (y >= WORLD_Y) or (x < 0) or (x >= WORLD_X)

world_name = "default"

def load(name):
    global map, objects, world_name, to_del, send_data
    try:
        with open("res/maps/" + name + ".wrld", "rb") as handle:
            map = pickle.load(handle)
            objects = pickle.load(handle)
            send_data = pickle.load(handle)
            to_del = []
            world_name = name
    except Exception as ex:
        map = [[ WORLD_NOTHING for y in range(WORLD_Y)] for x in range(WORLD_X)]
        objects = []
        world_name = "default"
        print("Error loading map " + name)
        print(ex)

def save_player(plr):
    temp_pipe = plr.attributes["pipe"] # Save pipe because it can't be serialized. Maybe. At least it doesn't need to

    try:
        with open("res/saves/" + plr.attributes["name"] + ".plr", "wb") as handle:
            plr.attributes["pipe"] = None
            plr.attributes["timeout"] = 0
            plr.attributes["keys"] = bytearray(display.NUM_KEYS)
            pickle.dump(plr, handle)
            plr.attributes["send_pipe"] = temp_pipe
    except Exception as ex:
        print("Could not save player named " + plr.attributes["name"], ": ", ex)
        plr.attributes["pipe"] = temp_pipe

def load_player(name):
    if name == "default":
        print("default!")
        return None
    try:
        with open("res/saves/" + name + ".plr", "rb") as handle:
            return pickle.load(handle)
    except Exception as ex:
        print(ex)
        return None

def save(name):
    try:
        with open("res/maps/" + name + ".wrld", "wb") as handle:
            pickle.dump(map, handle)
            pickle.dump(objects, handle)
            pickle.dump(make_send_data(), handle)
    except Exception as ex:
        print( "Could not save.", ex)

def make_send_data():
    send_data = []
    for y in range(WORLD_Y):
        for x in range(WORLD_X):
            send_data.append({"fgc" : map[x][y][0], "bgc" : map[x][y][1], "chr": map[x][y][2]})
    return JSON.dumps({"type" : "map", "data" : send_data})
