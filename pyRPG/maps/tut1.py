import copy

import world
from objects import *
from objects import lock_portal

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]    
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, 49,10,{"newmap": "tutboss", "locx": 0, "locy": 10, "used" : False}))
     
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7,  7, copy.deepcopy(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 20, 6, copy.deepcopy(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 10, copy.deepcopy(enemy.enemy_attributes)))

    world.map[4][4] = [0, 'K', False]
    world.map[5][4] = [0, 'i', False]
    world.map[6][4] = [0, 'l', False]
    world.map[7][4] = [0, 'l', False]
    world.map[8][4] = [0, ' ', False]
    world.map[9][4] = [0, 'T', False]
    world.map[10][4] = [0, 'h', False]
    world.map[11][4] = [0, 'e', False]
    world.map[12][4] = [0, 'm', False]
    world.map[13][4] = [0, ' ', False]
    world.map[14][4] = [0, 'T', False]
    world.map[15][4] = [0, 'o', False]
    world.map[16][4] = [0, ' ', False]
    world.map[17][4] = [0, 'P', False]
    world.map[18][4] = [0, 'r', False]
    world.map[19][4] = [0, 'o', False]
    world.map[20][4] = [0, 'c', False]
    world.map[21][4] = [0, 'e', False]
    world.map[22][4] = [0, 'd', False]
    world.map[23][4] = [0, 'e', False]


