import world
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects = [world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 49,10,{"newmap": "tutboss", "locx": 0, "locy": 10, "used" : False})]
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 7, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 20, 6, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 10, dict(enemy.enemy_attributes)))
    world.map[4][4] = [0, 'K', True]
    world.map[5][4] = [0, 'I', True]
    world.map[6][4] = [0, 'L', True]
    world.map[7][4] = [0, 'L', True]
    world.map[8][4] = [0, ' ', True]
    world.map[9][4] = [0, 'T', True]
    world.map[10][4] = [0, 'H', True]
    world.map[11][4] = [0, 'E', True]
    world.map[12][4] = [0, 'M', True]