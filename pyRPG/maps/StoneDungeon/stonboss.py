import display
import world
from objects import *
from objects.StoneDungeon import lavaborder
from objects.General import lock_portal
from objects.StoneDungeon import stone_boss

def generate():
    world.objects = []
    world.map = [[ world.WORLD_NOTHING for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(lock_portal.lock_portal(48, 10, "town", 0, 10))

    world.objects.append(stone_boss.stone_boss(25, 10))
    world.objects.append(lavaborder.lavaborder())
    for x in range(0,49):
        world.map[x][0] = [display.RED, display.RED, '#', True]
        world.map[x][world.WORLD_Y-1] = [display.RED, display.RED, '#', True]
    for y in range(0,20):
        world.map[0][y] = [display.RED, display.RED, '#', True]
        world.map[world.WORLD_X-1][y] = [display.RED, display.RED, '#', True]

