import world
from objects import *
from objects import lock_portal
from objects import shoot_enemy 

def generate():
    world.objects = []
    world.map = [[ world.WORLD_STONE for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, 49,10,{"newmap": "ston1", "locx": 0, "locy": 10, "used" : False}))
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, 0,10,{"newmap": "town", "locx": 0, "locy": 10, "used" : False}))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 7, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 20, 6, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 35, 10, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 40, 7, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 30, 6, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 25, 10, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 45, 10, dict(shoot_enemy.attributes)))