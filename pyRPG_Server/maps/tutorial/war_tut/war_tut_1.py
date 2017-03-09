# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world

from objects import General
from objects.tutorial import war_tut

def generate():
    world.objects.clear()

    world.objects.append(General.portal.portal(0, 10, "warrior_start", 48, 10))
    world.objects.append(war_tut.water.water())
    world.objects.append(war_tut.war_spawner.war_spawner(30, 7))
    world.objects.append(war_tut.war_spawner.war_spawner(20, 3))
    world.objects.append(war_tut.war_spawner.war_spawner(10, 5))
    world.objects.append(war_tut.war_spawner.war_spawner(45, 13))
    world.objects.append(war_tut.war_spawner.war_spawner(40, 17))

    world.objects.append(war_tut.war_enemy.war_enemy(40, 17))
    world.objects.append(war_tut.war_enemy.war_enemy(40, 17))




    world.map = [[ [display.GREEN, display.BLACK, ';', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.map[16][0] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[17][0] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[18][0] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[17][1] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[18][1] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[19][1] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[20][1] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[18][2] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[19][2] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[20][2] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[21][2] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][2] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[19][3] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[20][3] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[21][3] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][3] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[21][4] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][4] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][4] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][4] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][5] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][5] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][5] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][6] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][6] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][6] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[25][6] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][7] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][7] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][8] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][8] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][8] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[25][8] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[21][9] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][9] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][9] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][9] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][10] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][10] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[25][10] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[25][11] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[26][11] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[27][11] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][12] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][12] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[25][12] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[26][12] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][13] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][13] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][13] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[19][14] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[20][14] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[21][14] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][14] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[21][15] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][15] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][15] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][15] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[22][16] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][16] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][16] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[25][16] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][17] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[25][17] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[26][17] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[27][17] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][18] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[25][18] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[26][18] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[23][19] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[24][19] =  [display.BLUE, display.BLUE, 'W', True]
    world.map[25][19] =  [display.BLUE, display.BLUE, 'W', True]
