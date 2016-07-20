import world
from objects import *

def generate():
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects = []