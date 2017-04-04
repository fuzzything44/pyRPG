# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world

from objects.tutorial import mage_tut
from objects import General

def generate():
    world.objects.clear()
    world.objects.append(mage_tut.mage_boss_spawner.mage_boss_spawner(40, 9))

    world.objects.append(General.lock_portal.lock_portal(5, 9 , "mage_tut_2", 25, 9 ))
    world.objects.append(General.lock_portal.lock_portal(5, 10, "mage_tut_2", 25, 10))
    world.objects.append(General.lock_portal.lock_portal(6, 9 , "mage_tut_2", 26, 9 ))
    world.objects.append(General.lock_portal.lock_portal(6, 10, "mage_tut_2", 26, 10))


    world.map = [[ [display.WHITE, display.BLACK, '.', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.map[39][8] =  [display.RED, display.BLACK, '\\', True]
    world.map[41][8] =  [display.RED, display.BLACK, '/', True]
    world.map[40][9] = [0, 1, '#', True]
    world.map[39][10] =  [display.RED, display.BLACK, '/', True]
    world.map[41][10] =  [display.RED, display.BLACK, '\\', True]
