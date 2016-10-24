import pickle

import display
from objects import Player as play

# World tile. Form of [foreground color, background color, display char, canwalk]. None of this should move, all is part of background world.
WORLD_NOTHING = [display.BLACK, display.BLACK, ' ', True]     # Nothing there

WORLD_X = 50    # Max X size
WORLD_Y = 20    # Max Y size

map = [[]]
player = None

objects = []    # World objects that can interacted with such as enemies, chests, etc...
to_del = []     # Objects that should be deleted.

def out_of_bounds(x, y):
    return (y < 0) or (y >= WORLD_Y) or (x < 0) or (x >= WORLD_X)

def dispworld():
    for x in range(WORLD_X):
        for y in range(WORLD_Y):
            display.printc(x, y + 5, map[x][y][2], map[x][y][0]) # Print normal char with black bgc


world_name = "default"
save_name = "default"
def load(name):
    global map, objects, world_name, to_del
    try:
        with open("res/maps/" + name + ".wrld", "rb") as handle:
            map = pickle.load(handle)
            objects = pickle.load(handle)
            to_del = []
            world_name = name
    except:
        map = [[ WORLD_NOTHING for y in range(WORLD_Y)] for x in range(WORLD_X)]
        objects = []
        world_name = "default"


def save(name):
    try:
        with open("res/maps/" + name + ".wrld", "wb") as handle:
            pickle.dump(map, handle)
            pickle.dump(objects, handle)
    except Exception as ex:
        display.printc(20, 10, "Could not save. Press ESC to continue.")
        display.refresh()
        while not display.keyDown(display.CONST.VK_ESCAPE):
            pass

def save_player():
    try:
        with open("res/saves/" + save_name + ".plr", "wb") as handle:
            pickle.dump(player, handle)
            pickle.dump(world_name, handle)
            display.flash()
    except Exception as ex:
        display.printc(20, 10, "Could not save. Press ESC to continue.")
        display.refresh()
        while not display.keyDown(display.CONST.VK_ESCAPE):
            pass

def load_player(name):
    global player, save_name, objects
    try:
        with open("res/saves/" + name + ".plr", "rb") as handle:
            player = pickle.load(handle)
            # Next saved item should be the world they were in, so load that world
            in_world = pickle.load(handle)
            load(in_world)
            save_name = name
    except:
        player = play.player.player(0, 0)
    objects = [player] + objects