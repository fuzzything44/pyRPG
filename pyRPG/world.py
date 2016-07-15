# World tile. Form of [Color, display char, canwalk]. None of this should move, all is part of background world.
WORLD_NOTHING   = [0, ' ', True]        # Nothing there
WORLD_WALL      = [0, '#', False]       # Wall, can't be walked through
WORLD_LAVA      = [1, '#', True]          # Lava tile. Must add a damage tile over it.
WORLD_GRASS     = [4, ';', True]        # Grass!
WORLD_CHEST     = [6, '@', False]      # Phat Loot!

WORLD_X = 50    # Max X size
WORLD_Y = 20    # Max Y size
map = [[WORLD_GRASS for y in range(WORLD_Y)] for x in range(WORLD_X)]     # Represents world map
player = 0

map[5][5] = WORLD_WALL
map[10][15] = WORLD_LAVA
map[7][7] = WORLD_NOTHING
map[15][10] = WORLD_CHEST
map[0][0] = WORLD_WALL
map[WORLD_X - 1][WORLD_Y - 1] = WORLD_WALL
objects = []    # World objects that can interacted with such as enemies, chests, etc...
to_del = []     # Objects that should be deleted.
