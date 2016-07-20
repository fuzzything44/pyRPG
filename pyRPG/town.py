import world
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

    world.map[45][1] = world.WORLD_CHEST

    
    for x in range(42,49):
        world.map[x][0] = world.WORLD_WALL
        world.map[x][5] = world.WORLD_WALL
    for y in range(0,5):
        world.map[42][y] = world.WORLD_WALL
        world.map[48][y] = world.WORLD_WALL
   
    for x in range(43,48):
        for y in range(1,5):
            world.map[x][y] = [0,".", True]
        
    world.map[45][5] = [0,".", True]
    