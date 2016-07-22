import world
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    
    world.objects = [world_object.world_object(lockedportal.update, lockedportal.collide, lockedportal.char, lockedportal.color, lockedportal.type, 49,10,{"newmap": "tutboss", "locx": 0, "locy": 10, "used" : False})]
     
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 7, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 20, 6, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 10, dict(enemy.enemy_attributes)))

    world.map[4][4] = [0, 'K', False]
    world.map[5][4] = [0, 'I', False]
    world.map[6][4] = [0, 'L', False]
    world.map[7][4] = [0, 'L', False]
    world.map[8][4] = [0, ' ', False]
    world.map[9][4] = [0, 'T', False]
    world.map[10][4] = [0, 'H', False]
    world.map[11][4] = [0, 'E', False]
    world.map[12][4] = [0, 'M', False]