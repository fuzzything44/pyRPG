import world
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_STONE for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 1,9,{"newmap": "town", "locx": 0, "locy": 10, "used" : False}))
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 48,10,{"newmap": "credits", "locx": 0, "locy": 10, "used" : False}))
    
    for x in range(0,49):
        world.map[x][0] = world.WORLD_LAVA
        world.map[x][world.WORLD_Y-1] = world.WORLD_LAVA
        world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, x, WORLD_Y-1, {}))
        world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, x, 0, {}))
    for y in range(0,20):
        world.map[0][y] = world.WORLD_LAVA
        world.map[world.WORLD_X-1][y] = world.WORLD_LAVA
        world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, WORLD_X-1, y, {}))
        world.objects.append(world_object.world_object(invis_dmg.update, invis_dmg.fire_collide, invis_dmg.char, invis_dmg.color, invis_dmg.type, 0, y, {}))