import world
from objects import *

def generate():

    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

    world.map[5][5] = world.WORLD_WALL  

    for x in range(22,29):
        world.map[x][5] = world.WORLD_WALL
    for y in range(5,11):
        world.map[22][y] = world.WORLD_WALL

