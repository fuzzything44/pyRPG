import world
from objects import *

def generate():
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD.Y)] for x in range(world.WORLD_X)]

    world.map[5][5] = world.WORLD_WALL  
