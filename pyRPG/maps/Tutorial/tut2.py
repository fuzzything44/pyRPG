# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world
from objects.General import lock_portal
from objects import Tutorial
from objects import obj_maker

def generate():
    world.objects.clear()
    world.map = [[ [display.GREEN, display.BLACK, ';', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(obj_maker.make(lock_portal, 49, 10,{"newmap": "tutorial.2-killed", "locx": 45, "locy": 10, "used" : False}))     
    enemy1 = obj_maker.make(Tutorial.level_up_enemy, 10, 13)
    enemy2 = obj_maker.make(Tutorial.level_up_enemy, 25, 10)
    enemy3 = obj_maker.make(Tutorial.level_up_enemy, 40, 10)
    world.objects.append(obj_maker.make(Tutorial.lava, 0, 0))
    enemy1.attributes["pattern_loc"] = 3
    enemy2.attributes["pattern_loc"] = 5
    enemy3.attributes["pattern_loc"] = 1

    world.objects.append(enemy1)
    world.objects.append(enemy2)
    world.objects.append(enemy3)

    world.map[19][1] =  [display.RED, display.RED, '#', True]
    world.map[20][1] =  [display.RED, display.RED, '#', True]
    world.map[21][1] =  [display.RED, display.RED, '#', True]
    world.map[20][2] =  [display.RED, display.RED, '#', True]
    world.map[21][2] =  [display.RED, display.RED, '#', True]
    world.map[2][6] = [0, 1, 'B', True]
    world.map[3][6] = [0, 1, 'e', True]
    world.map[4][6] = [0, 1, 'w', True]
    world.map[5][6] = [0, 1, 'a', True]
    world.map[6][6] = [0, 1, 'r', True]
    world.map[7][6] = [0, 1, 'e', True]
    world.map[8][6] = [0, 1, ' ', True]
    world.map[9][6] = [0, 1, 'o', True]
    world.map[10][6] = [0, 1, 'f', True]
    world.map[11][6] = [0, 1, ' ', True]
    world.map[12][6] = [0, 1, 'l', True]
    world.map[13][6] = [0, 1, 'a', True]
    world.map[14][6] = [0, 1, 'v', True]
    world.map[15][6] = [0, 1, 'a', True]
    world.map[16][6] = [0, 1, '!', True]
    world.map[2][7] = [0, 1, 'I', True]
    world.map[3][7] = [0, 1, 't', True]
    world.map[4][7] = [0, 1, ' ', True]
    world.map[5][7] = [0, 1, 'w', True]
    world.map[6][7] = [0, 1, 'i', True]
    world.map[7][7] = [0, 1, 'l', True]
    world.map[8][7] = [0, 1, 'l', True]
    world.map[9][7] = [0, 1, ' ', True]
    world.map[10][7] = [0, 1, 'k', True]
    world.map[11][7] = [0, 1, 'i', True]
    world.map[12][7] = [0, 1, 'l', True]
    world.map[13][7] = [0, 1, 'l', True]
    world.map[14][7] = [0, 1, ' ', True]
    world.map[15][7] = [0, 1, 'y', True]
    world.map[16][7] = [0, 1, 'o', True]
    world.map[17][7] = [0, 1, 'u', True]
    world.map[18][7] = [0, 1, '.', True]
    world.map[2][8] =  [display.RED, display.RED, '#', True]
    world.map[3][8] = [0, 1, ' ', True]
    world.map[4][8] = [0, 1, 'i', True]
    world.map[5][8] = [0, 1, 's', True]
    world.map[6][8] = [0, 1, ' ', True]
    world.map[7][8] = [0, 1, 'l', True]
    world.map[8][8] = [0, 1, 'a', True]
    world.map[9][8] = [0, 1, 'v', True]
    world.map[10][8] = [0, 1, 'a', True]
    world.map[11][8] = [0, 1, '.', True]
    world.map[49][10] = [0, 1, 'O', True]
    world.map[5][13] =  [display.RED, display.RED, '#', True]
    world.map[6][13] =  [display.RED, display.RED, '#', True]
    world.map[7][13] =  [display.RED, display.RED, '#', True]
    world.map[30][13] =  [display.RED, display.RED, '#', True]
    world.map[31][13] =  [display.RED, display.RED, '#', True]
    world.map[32][13] =  [display.RED, display.RED, '#', True]
    world.map[6][14] =  [display.RED, display.RED, '#', True]
    world.map[7][14] =  [display.RED, display.RED, '#', True]
    world.map[8][14] =  [display.RED, display.RED, '#', True]
    world.map[31][14] =  [display.RED, display.RED, '#', True]
    world.map[32][14] =  [display.RED, display.RED, '#', True]
    world.map[7][15] =  [display.RED, display.RED, '#', True]
    world.map[8][15] =  [display.RED, display.RED, '#', True]
    world.map[9][15] =  [display.RED, display.RED, '#', True]
    world.map[10][15] =  [display.RED, display.RED, '#', True]
    world.map[11][15] =  [display.RED, display.RED, '#', True]
    world.map[5][16] =  [display.RED, display.RED, '#', True]
    world.map[6][16] =  [display.RED, display.RED, '#', True]
    world.map[7][16] =  [display.RED, display.RED, '#', True]
    world.map[8][16] =  [display.RED, display.RED, '#', True]
    world.map[9][16] =  [display.RED, display.RED, '#', True]
