import world
from objects import *
from objects import lock_portal

def generate():
    world.objects = []
    world.map = [[ world.WORLD_STONE for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, 49,10,{"newmap": "end", "locx": 2, "locy": 10, "used" : False}))
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, 0,10,{"newmap": "stone1", "locx": 0, "locy": 10, "used" : False}))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 7, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 20, 6, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 10, dict(enemy.enemy_attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 45, 5, dict(shoot_enemy.attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 30, 19, dict(shoot_enemy.attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 20, 15, dict(shoot_enemy.attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 13, 5, dict(shoot_enemy.attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 35, 19, dict(shoot_enemy.attributes)))
    world.objects.append(world_object.world_object(shoot_enemy.update, shoot_enemy.collide, shoot_enemy.char, shoot_enemy.color, shoot_enemy.type, 27, 15, dict(shoot_enemy.attributes)))
    world.map[12][15] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 12, 15, {}))
    world.map[43][5] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 43, 5, {}))
    world.map[2][15] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 2, 15, {}))
    world.map[12][5] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 12, 5, {}))
    world.map[6][18] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 6, 18, {}))
    world.map[3][9] = world.WORLD_LAVA
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 3, 9, {}))
