import world
from objects import *
from objects.StoneDungeon import lavaborder
from objects.General import lock_portal
from objects.StoneDungeon import stone_boss

def generate():
    world.objects = []
    world.map = [[ world.WORLD_NOTHING for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, 48,10,{"newmap": "credits", "locx": 0, "locy": 10, "used" : False}))

    world.objects.append(world_object.world_object(stone_boss.update, stone_boss.collide, stone_boss.char, stone_boss.color, stone_boss.type, 25, 10, dict(stone_boss.attributes)))
    world.objects.append(world_object.world_object(lavaborder.update, lavaborder.collide, lavaborder.char, lavaborder.color, lavaborder.type, 0, 0, lavaborder.attributes))
    for x in range(0,49):
        world.map[x][0] = world.WORLD_LAVA
        world.map[x][world.WORLD_Y-1] = world.WORLD_LAVA
    for y in range(0,20):
        world.map[0][y] = world.WORLD_LAVA
        world.map[world.WORLD_X-1][y] = world.WORLD_LAVA

