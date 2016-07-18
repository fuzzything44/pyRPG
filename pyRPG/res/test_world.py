from objects import world_object
from objects import player
from objects import invis_dmg
from objects import chest

WORLD_NOTHING   = [0, ' ', True]        # Nothing there
WORLD_WALL      = [0, '#', False]       # Wall, can't be walked through
WORLD_LAVA      = [1, '#', True]          # Lava tile. Must add a damage tile over it.
WORLD_GRASS     = [4, ';', True]        # Grass!
WORLD_CHEST     = [6, '@', False]      # Phat Loot!

player = world_object.world_object(player.player_update, player.collide, player.player_char, player.player_color, player.player_type, 10, 10, player.player_attributes)

WORLD_X = 50
WORLD_Y = 20

def get_map():
    map = [[WORLD_GRASS for y in range(WORLD_Y)] for x in range(WORLD_X)]     # Represents world map
    map[5][5] = WORLD_WALL
    map[10][15] = WORLD_LAVA
    map[7][7] = WORLD_NOTHING
    map[15][10] = WORLD_CHEST
    map[0][0] = WORLD_WALL
    map[WORLD_X - 1][WORLD_Y - 1] = WORLD_WALL
    return map

def get_objects():
    obj = []
    obj.append(world_object.world_object(invis_dmg.invis_dmg_update, invis_dmg.invis_fire_dmg_collide, invis_dmg.invis_dmg_char, invis_dmg.invis_dmg_color, invis_dmg.invis_dmg_type, 10, 15, {"type" : "damage", "name" : "lava"}))
    obj.append(world_object.world_object(chest.chest_update, chest.chest_collide, chest.chest_char, chest.chest_col, chest.chest_type, 16, 10, chest.chest_attributes))
    return obj

def get_player():
    return player
