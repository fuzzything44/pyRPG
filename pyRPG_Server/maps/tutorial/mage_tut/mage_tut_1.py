# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world

from objects import General

from objects.tutorial import mage_tut

def generate():
    world.objects.clear()

    world.objects.append(General.portal.portal(0, 9, "mage_start", 48, 9))

    world.objects.append(mage_tut.mage_spawner.mage_spawner(10, 5))
    world.objects.append(mage_tut.mage_spawner.mage_spawner(17, 3))
    world.objects.append(mage_tut.mage_spawner.mage_spawner(30, 8))
    world.objects.append(mage_tut.mage_spawner.mage_spawner(7, 15))
    world.objects.append(mage_tut.mage_spawner.mage_spawner(40, 18))

    world.map = [[ [display.WHITE, display.BLACK, '.', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.map[41][0] = [0, 1, '#', True]
    world.map[41][1] = [0, 1, '#', True]
    world.map[42][2] = [0, 1, '#', True]
    world.map[42][3] = [0, 1, '#', True]
    world.map[44][5] = [0, 1, '#', True]
    world.map[45][5] = [0, 1, '#', True]
    world.map[46][6] = [0, 1, '#', True]
    world.map[47][7] = [0, 1, '#', True]
    world.map[48][7] = [0, 1, '#', True]
    world.map[49][7] = [0, 1, '#', True]
