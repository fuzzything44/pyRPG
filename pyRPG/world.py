import pickle
from objects import world_object
import objects.player as play

# World tile. Form of [Color, display char, canwalk]. None of this should move, all is part of background world.
WORLD_NOTHING   = [0, ' ', True]        # Nothing there
WORLD_WALL      = [0, '#', False]       # Wall, can't be walked through
WORLD_LAVA      = [1, '#', True]          # Lava tile. Must add a damage tile over it.
WORLD_GRASS     = [4, ';', True]        # Grass!
WORLD_CHEST     = [6, '@', False]      # Phat Loot!

WORLD_X = 50    # Max X size
WORLD_Y = 20    # Max Y size

global player, map, objects

map = 0
player = 0

objects = []    # World objects that can interacted with such as enemies, chests, etc...
to_del = []     # Objects that should be deleted.


#TODO: Don't save player here, save in another file instead!
def load(name):
    global map, player, objects
    try:
        with open("res/maps" + name + ".wrld", "rb") as handle:
            map = pickle.load(handle)
            objects = pickle.load(handle)
    except:
        map = [[ WORLD_NOTHING for y in range(WORLD_Y)] for x in range(WORLD_X)]


def save(name):
    with open("res/maps" + name + ".wrld", "wb") as handle:
        pickle.dump(map, handle)
        # Don't save player...
        pickle.dump(objects[1:], handle)

def save_player(name):
    with open("res/saves" + name + ".plr", "wb") as handle:
        pickle.dump(player, handle)

def load_player(name):
    global player
    try:
        with open("res/saves" + name + ".plr", "rb") as handle:
            player = pickle.load(handle)
    except:
        player = world_object.world_object(play.player_update, play.collide, play.player_char, play.player_color, "player", 0, 0, play.player_attributes)
    global objects
    objects = [player] + objects