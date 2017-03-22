# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world

from objects import General

from objects.tutorial import mage_tut

def generate():
    world.objects.clear()

    world.objects.append(General.portal.portal(0, 9, "mage_start", 48, 9))

    world.objects.append(mage_tut.mage_spawner.mage_spawner(20, 10))
    world.objects.append(mage_tut.mage_spawner.mage_spawner(17, 3))
    world.objects.append(mage_tut.mage_spawner.mage_spawner(30, 8))
    world.objects.append(mage_tut.mage_spawner.mage_spawner(7, 15))
    world.objects.append(mage_tut.mage_spawner.mage_spawner(40, 18))

    world.objects.append(General.portal.portal(49, 0, "mage_tut_2", 1, 0))

    world.map = [[ [display.WHITE, display.BLACK, '.', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.map[41][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[43][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[44][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[45][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[46][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[47][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[48][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[49][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[41][1] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[43][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[44][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[45][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[46][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[47][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[48][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[49][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[42][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[44][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[45][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[46][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[47][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[48][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[49][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[42][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[44][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[45][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[46][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[47][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[48][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[49][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[43][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[44][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[45][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[46][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[47][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[48][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[49][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[44][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][5] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[47][5] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[48][5] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[49][5] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[46][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][6] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[48][6] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[49][6] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[47][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][7] =  [display.WHITE, display.BLACK, '#', False]
