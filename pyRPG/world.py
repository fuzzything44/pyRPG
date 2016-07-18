import pickle

# World tile. Form of [Color, display char, canwalk]. None of this should move, all is part of background world.
WORLD_NOTHING   = [0, ' ', True]        # Nothing there
WORLD_WALL      = [0, '#', False]       # Wall, can't be walked through
WORLD_LAVA      = [1, '#', True]          # Lava tile. Must add a damage tile over it.
WORLD_GRASS     = [4, ';', True]        # Grass!
WORLD_CHEST     = [6, '@', False]      # Phat Loot!

WORLD_X = 50    # Max X size
WORLD_Y = 20    # Max Y size

map = 0
player = 0

objects = []    # World objects that can interacted with such as enemies, chests, etc...
to_del = []     # Objects that should be deleted.

def load(name):
    with open("res/" + name + ".wrld", "rb") as handle:
        global map, player, objects
        map = pickle.load(handle)
        player = pickle.load(handle)
        objects = pickle.load(handle)
    pass
        

def save(name):
    with open("res/" + name + ".wrld", "wb") as handle:
        pickle.dump(map, handle)
        pickle.dump(player, handle)
        pickle.dump(objects, handle)