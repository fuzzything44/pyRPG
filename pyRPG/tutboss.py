import world
from objects import *
from objects import MiniBoss
from objects import lock_portal
def generate():
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects = []
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, 49,10,{"newmap": "town", "locx": 0, "locy": 10, "used" : False}))
    world.objects.append(world_object.world_object(invis_dmg.update, fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 12, 15, dict(invis_dmg_attributes)))
    world.objects.append(world_object.world_object(MiniBoss.MiniBoss_update, MiniBoss.MiniBosscollide, MiniBoss.MiniBossChar, MiniBoss.MiniBossColor, MiniBoss.MiniBoss_type, 25, 10, dict(MiniBoss.MiniBoss_attributes)))

    world.map[30][15] = [1, '#', True]
    world.map[31][15] = [0, '=', True]
    world.map[32][15] = [0, 'L', True]
    world.map[33][15] = [0, 'a', True]
    world.map[34][15] = [0, 'v', True]
    world.map[35][15] = [0, 'a', True]
   
    world.map[12][15] = world.WORLD_LAVA 
    world.map[43][5] = world.WORLD_LAVA
    world.map[2][15] = world.WORLD_LAVA
    world.map[12][5] = world.WORLD_LAVA
    world.map[6][18] = world.WORLD_LAVA
    world.map[3][9] = world.WORLD_LAVA

