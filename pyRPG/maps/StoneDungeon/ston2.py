import copy

import display
import world

from objects.General import lock_portal
from objects.General import portal
from objects.StoneDungeon import enemy
from objects.StoneDungeon import shoot_enemy
from objects.General import invis_dmg
from objects import world_object

def generate():
    world.objects = []
    world.map = [[ world.WORLD_NOTHING for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    for x in range(world.WORLD_X):
        world.map[x][0] = [display.WHITE, display.WHITE, '#', False]
        world.map[x][world.WORLD_Y - 1] = [display.WHITE, display.WHITE, '#', False]
    for y in range(world.WORLD_Y):
        world.map[0][y] = [display.WHITE, display.WHITE, '#', False]
        world.map[world.WORLD_X - 1][y] = [display.WHITE, display.WHITE, '#', False]

    world.objects.append(portal.portal(0, 10, "stonedungeon.1", world.WORLD_X - 2, 10))
    world.objects.append(lock_portal.lock_portal(world.WORLD_X - 1, 10,"stonedungeon.boss", 2, 10))
    world.objects.append(enemy.stone_enemy(7 , 7 ))
    world.objects.append(enemy.stone_enemy(20, 6 ))
    world.objects.append(enemy.stone_enemy(7 , 10))
    world.objects.append(shoot_enemy.shoot_enemy(45, 5 ))
    world.objects.append(shoot_enemy.shoot_enemy(30, 18))
    world.objects.append(shoot_enemy.shoot_enemy(20, 15))
    world.objects.append(shoot_enemy.shoot_enemy(13, 5 ))
    world.objects.append(shoot_enemy.shoot_enemy(35, 18))
    world.objects.append(shoot_enemy.shoot_enemy(27, 15))
    world.objects.append(invis_dmg.lavatile(12, 15))
    world.objects.append(invis_dmg.lavatile(43, 5 ))
    world.objects.append(invis_dmg.lavatile(2 , 15))
    world.objects.append(invis_dmg.lavatile(12, 5 ))
    world.objects.append(invis_dmg.lavatile(6 , 18))
    world.objects.append(invis_dmg.lavatile(3 , 9 ))

    world.map[49][10] = world.WORLD_NOTHING
    world.map[0][10] = world.WORLD_NOTHING
    world.map[12][15] =[display.RED, display.RED, '#', True]
    world.map[43][5] = [display.RED, display.RED, '#', True]
    world.map[2][15] = [display.RED, display.RED, '#', True]
    world.map[12][5] = [display.RED, display.RED, '#', True]
    world.map[6][18] = [display.RED, display.RED, '#', True]
    world.map[3][9] =  [display.RED, display.RED, '#', True]
