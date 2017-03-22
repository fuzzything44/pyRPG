# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world

from objects import General

from objects.tutorial import mage_tut

def generate():
    world.objects.clear()

    world.objects.append(General.portal.portal(0, 0, "mage_tut_1", 48, 0))

    world.objects.append(mage_tut.adv_mage_spawner.adv_mage_spawner(18, 7))
    world.objects.append(mage_tut.adv_mage_spawner.adv_mage_spawner(38, 6))
    world.objects.append(mage_tut.adv_mage_spawner.adv_mage_spawner(18, 14))
    world.objects.append(mage_tut.adv_mage_spawner.adv_mage_spawner(39, 12))


    world.map = [[ [display.WHITE, display.BLACK, '.', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.map[0][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[1][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[2][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[3][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[4][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[5][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[6][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[7][0] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[8][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[1][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[2][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[3][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[4][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[5][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[6][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[7][1] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[8][1] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[1][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[2][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[3][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[4][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[5][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[6][2] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[7][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[1][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[2][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[3][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[4][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[5][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[6][3] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[7][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[1][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[2][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[3][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[4][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[5][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[6][4] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[0][5] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[1][5] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[2][5] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[3][5] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[4][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][6] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[1][6] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[2][6] =  [display.WHITE, display.BLACK, ' ', True]
    world.map[3][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[2][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[25][7] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[26][7] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[24][8] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[25][8] =  [display.MAGENTA, display.BLACK, '%', True]
    world.map[26][8] =  [display.MAGENTA, display.BLACK, '%', True]
    world.map[27][8] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[23][9] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[24][9] =  [display.MAGENTA, display.BLACK, '%', True]
    world.map[25][9] =  [display.RED, display.BLACK, 'O', True]
    world.map[26][9] =  [display.RED, display.BLACK, 'O', True]
    world.map[27][9] =  [display.MAGENTA, display.BLACK, '%', True]
    world.map[28][9] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[23][10] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[24][10] =  [display.MAGENTA, display.BLACK, '%', True]
    world.map[25][10] =  [display.RED, display.BLACK, 'O', True]
    world.map[26][10] =  [display.RED, display.BLACK, 'O', True]
    world.map[27][10] =  [display.MAGENTA, display.BLACK, '%', True]
    world.map[28][10] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[24][11] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[25][11] =  [display.MAGENTA, display.BLACK, '%', True]
    world.map[26][11] =  [display.MAGENTA, display.BLACK, '%', True]
    world.map[27][11] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[25][12] =  [display.MAGENTA, display.BLACK, '@', True]
    world.map[26][12] =  [display.MAGENTA, display.BLACK, '@', True]
