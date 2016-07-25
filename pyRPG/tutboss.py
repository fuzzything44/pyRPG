import world
from objects import *
from objects import MiniBoss
from objects import lock_portal
def generate():
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects = []
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, 49,10,{"newmap": "town", "locx": 0, "locy": 10, "used" : False}))
    world.objects.append(world_object.world_object(MiniBoss.MiniBoss_update, MiniBoss.MiniBosscollide, MiniBoss.MiniBossChar, MiniBoss.MiniBossColor, MiniBoss.MiniBoss_type, 25, 10, dict(MiniBoss.MiniBoss_attributes)))

    world.map[30][0] = [6, '@', True]
    world.map[31][0] = [0, '=', True]
    world.map[32][0] = [0, 'C', True]
    world.map[33][0] = [0, 'h', True]
    world.map[34][0] = [0, 'e', True]
    world.map[35][0] = [0, 's', True]
    world.map[36][0] = [0, 't', True]

    world.map[30][1] = [1, '#', True]
    world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 30, 1, {}))
    world.map[31][1] = [0, '=', True]
    world.map[32][1] = [0, 'L', True]
    world.map[33][1] = [0, 'a', True]
    world.map[34][1] = [0, 'v', True]
    world.map[35][1] = [0, 'a', True]

    world.map[30][4] = [0, 'U', True]
    world.map[31][4] = [0, 's', True]
    world.map[32][4] = [0, 'e', True]
    world.map[33][4] = [0, ' ', True]
    world.map[34][4] = [0, 'S', True]
    world.map[35][4] = [0, 'p', True]
    world.map[36][4] = [0, 'a', True]
    world.map[37][4] = [0, 'c', True]
    world.map[38][4] = [0, 'e', True]
    world.map[39][4] = [0, ' ', True]
    world.map[40][4] = [0, 'T', True]
    world.map[41][4] = [0, 'o', True]
    world.map[42][4] = [0, ' ', True]
    world.map[43][4] = [0, 'H', True]
    world.map[44][4] = [0, 'e', True]
    world.map[45][4] = [0, 'a', True]
    world.map[46][4] = [0, 'l', True]



    world.map[42][15] = world.WORLD_LAVA
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
