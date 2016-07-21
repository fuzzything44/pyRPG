import world
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 25,8,{"newmap": "tut1", "locx": 0, "locy": 10, "used" : False}))
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 0,9,{"newmap": "town", "locx": 0, "locy": 10, "used" : False}))

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
    
    world.map[5][3] = [0, 'W', True]
    world.map[4][4] = [0, 'A', True]
    world.map[5][4] = [0, 'S', True]
    world.map[6][4] = [0, 'D', True]
    world.map[4][6] = [0, 'M', True]
    world.map[5][6] = [0, 'O', True]
    world.map[6][6] = [0, 'V', True]

    world.map[world.WORLD_X - 6][3] = [0, 'I', True]
    world.map[world.WORLD_X - 7][4] = [0, 'J', True]
    world.map[world.WORLD_X - 6][4] = [0, 'K', True]
    world.map[world.WORLD_X - 5][4] = [0, 'L', True]
    world.map[world.WORLD_X - 7][6] = [0, 'A', True]
    world.map[world.WORLD_X - 6][6] = [0, 'T', True]
    world.map[world.WORLD_X - 5][6] = [0, 'K', True]
