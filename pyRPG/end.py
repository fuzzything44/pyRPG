import world
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_STONE for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]