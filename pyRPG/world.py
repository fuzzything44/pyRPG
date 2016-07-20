import pickle

import display
from objects import world_object
import objects.player as play

# World tile. Form of [Color, display char, canwalk]. None of this should move, all is part of background world.
WORLD_NOTHING   = [0, ' ', True]        # Nothing there
WORLD_WALL      = [0, '#', False]       # Wall, can't be walked through
WORLD_LAVA      = [1, '#', True]        # Lava tile. Must add a damage tile over it.
WORLD_GRASS     = [4, ';', True]        # Grass!
WORLD_CHEST     = [6, '@', False]       # Phat Loot!
WORLD_SMOG      = [0, 'z', False]       # Poison Gas, need a damage tile

WORLD_X = 50    # Max X size
WORLD_Y = 20    # Max Y size

global player, map, objects

map = 0
player = 0

objects = []    # World objects that can interacted with such as enemies, chests, etc...
to_del = []     # Objects that should be deleted.

world_name = "default"
save_name = "default"
#TODO: Don't save player here, save in another file instead!
def load(name):
    global map, objects, world_name
    try:
        with open("res/maps/" + name + ".wrld", "rb") as handle:
            map = pickle.load(handle)
            objects = pickle.load(handle)
            world_name = name
    except:
        map = [[ WORLD_NOTHING for y in range(WORLD_Y)] for x in range(WORLD_X)]
        objects = []
        world_name = "default"


def save(name):
    try:
        with open("res/maps/" + name + ".wrld", "wb") as handle:
            pickle.dump(map, handle)
            # Don't save player...
            pickle.dump(objects[1:], handle)
    except Exception as ex:
        display.printc(20, 10, "Could not save. Press ESC to continue.")
        display.refresh()
        while not display.keyDown(display.CONST.VK_ESCAPE):
            pass

def save_player():
    try:
        with open("res/saves/" + save_name + ".plr", "wb") as handle:
            pickle.dump(player, handle, pickle.HIGHEST_PROTOCOL)
            pickle.dump(world_name, handle, pickle.HIGHEST_PROTOCOL)
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
            load(pickle.load(handle))
            save_name = name
    except:
        player = world_object.world_object(play.player_update, play.collide, play.player_char, play.player_color, "player", 0, 0, play.player_attributes)
    objects = [player] + objects