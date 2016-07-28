import display
import world
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 25,8,{"newmap": "tut1", "locx": 0, "locy": 10, "used" : False}))

    for x in range(22,29):
        world.map[x][5] = world.WORLD_WALL
        world.map[x][10] = world.WORLD_WALL
    for y in range(5,11):
        world.map[22][y] = world.WORLD_WALL
        world.map[28][y] = world.WORLD_WALL
   
    for x in range(23,28):
        for y in range(6,10):
            world.map[x][y] = [0,".", True]
        
    world.map[25][10] = [0,".", True]
    
    world.map[25][12] = [0, 'W', True]
    world.map[24][13] = [0, 'A', True]
    world.map[25][13] = [0, 'S', True]
    world.map[26][13] = [0, 'D', True]

    world.map[22][14] = [0, 'T', True]
    world.map[23][14] = [0, 'O', True]
                   
    world.map[25][14] = [0, 'M', True]
    world.map[26][14] = [0, 'O', True]
    world.map[27][14] = [0, 'V', True]
    world.map[28][14] = [0, 'E', True]

    world.map[19][17] = [0, 'Y', True]
    world.map[20][17] = [0, 'O', True]
    world.map[21][17] = [0, 'U', True]
    world.map[23][17] = [0, '>', True]

    world.map[27][17] = [0, '<', True]
    world.map[29][17] = [0, 'Y', True]
    world.map[30][17] = [0, 'O', True]
    world.map[31][17] = [0, 'U', True]

    world.map[22][16] = [display.BLUE, 'O', True]
    world.map[23][16] = [0, '=', True]
    world.map[24][16] = [0, 'P', True]
    world.map[25][16] = [0, 'o', True]
    world.map[26][16] = [0, 'r', True]
    world.map[27][16] = [0, 't', True]
    world.map[28][16] = [0, 'a', True]
    world.map[29][16] = [0, 'l', True]
