# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world

from objects import obj_maker
from objects.General import lock_portal
from objects import Tutorial

def generate():
    world.objects.clear()
    world.map = [[ [display.GREEN, display.BLACK, ';', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(obj_maker.make(lock_portal, 49, 10,{"newmap": "town", "locx": 25, "locy": 10, "used" : False}))     
    world.objects.append(obj_maker.make(Tutorial.lava, 0, 0))
    world.objects.append(obj_maker.make(Tutorial.tutorial_boss, 25, 10))

    world.map[2][2] =  [display.RED, display.RED, '#', True]
    world.map[3][2] =  [display.RED, display.RED, '#', True]
    world.map[46][2] =  [display.RED, display.RED, '#', True]
    world.map[47][2] =  [display.RED, display.RED, '#', True]
    world.map[2][3] =  [display.RED, display.RED, '#', True]
    world.map[3][3] =  [display.RED, display.RED, '#', True]
    world.map[46][3] =  [display.RED, display.RED, '#', True]
    world.map[47][3] =  [display.RED, display.RED, '#', True]
    world.map[6][4] =  [display.RED, display.RED, '#', True]
    world.map[43][4] =  [display.RED, display.RED, '#', True]
    world.map[9][5] =  [display.RED, display.RED, '#', True]
    world.map[40][5] =  [display.RED, display.RED, '#', True]
    world.map[13][6] =  [display.RED, display.RED, '#', True]
    world.map[36][6] =  [display.RED, display.RED, '#', True]
    world.map[16][7] =  [display.RED, display.RED, '#', True]
    world.map[33][7] =  [display.RED, display.RED, '#', True]
    world.map[19][8] =  [display.RED, display.RED, '#', True]
    world.map[30][8] =  [display.RED, display.RED, '#', True]
    world.map[23][9] =  [display.RED, display.RED, '#', True]
    world.map[26][9] =  [display.RED, display.RED, '#', True]
    world.map[23][10] =  [display.RED, display.RED, '#', True]
    world.map[26][10] =  [display.RED, display.RED, '#', True]
    world.map[19][11] =  [display.RED, display.RED, '#', True]
    world.map[30][11] =  [display.RED, display.RED, '#', True]
    world.map[16][12] =  [display.RED, display.RED, '#', True]
    world.map[33][12] =  [display.RED, display.RED, '#', True]
    world.map[13][13] =  [display.RED, display.RED, '#', True]
    world.map[36][13] =  [display.RED, display.RED, '#', True]
    world.map[9][14] =  [display.RED, display.RED, '#', True]
    world.map[40][14] =  [display.RED, display.RED, '#', True]
    world.map[6][15] =  [display.RED, display.RED, '#', True]
    world.map[43][15] =  [display.RED, display.RED, '#', True]
    world.map[2][16] =  [display.RED, display.RED, '#', True]
    world.map[3][16] =  [display.RED, display.RED, '#', True]
    world.map[46][16] =  [display.RED, display.RED, '#', True]
    world.map[47][16] =  [display.RED, display.RED, '#', True]
    world.map[2][17] =  [display.RED, display.RED, '#', True]
    world.map[3][17] =  [display.RED, display.RED, '#', True]
    world.map[46][17] =  [display.RED, display.RED, '#', True]
    world.map[47][17] =  [display.RED, display.RED, '#', True]
