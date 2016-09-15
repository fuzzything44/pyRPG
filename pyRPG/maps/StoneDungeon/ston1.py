import copy

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
        world.map[x][0] = world.WORLD_WALL
        world.map[x][world.WORLD_Y - 1] = world.WORLD_WALL
    for y in range(world.WORLD_Y):
        world.map[0][y] = world.WORLD_WALL
        world.map[world.WORLD_X - 1][y] = world.WORLD_WALL
        
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 0,10, {"newmap": "stonestart", "locx": world.WORLD_X - 2, "locy": 10, "used" : False}))
    world.map[49][10] = world.WORLD_NOTHING
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, world.WORLD_X - 1, 10, {"newmap": "stone2", "locx": 2, "locy": 10, "used" : False}))
    world.map[0][10] = world.WORLD_NOTHING
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 7, copy.deepcopy(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 20, 6, copy.deepcopy(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 10, copy.deepcopy(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 45, 5, copy.deepcopy(shoot_enemy.attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 30, 18, copy.deepcopy(shoot_enemy.attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 20, 15, copy.deepcopy(shoot_enemy.attributes)))
    world.map[12][15] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 12, 15, copy.deepcopy(invis_dmg.attributes)))
    world.map[43][5] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 43, 5, copy.deepcopy(invis_dmg.attributes)))
    world.map[2][15] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 2, 15, copy.deepcopy(invis_dmg.attributes)))
    world.map[12][5] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 12, 5, copy.deepcopy(invis_dmg.attributes)))
    world.map[6][18] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 6, 18, copy.deepcopy(invis_dmg.attributes)))
    world.map[3][9] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 3, 9, copy.deepcopy(invis_dmg.attributes)))
