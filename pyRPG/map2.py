import world
from objects import *

def generate():
    try:
        world.map = [[world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

        world.map[5][5] = world.WORLD_WALL  
    except Exception as ex:
        pass
