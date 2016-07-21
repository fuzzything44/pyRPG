import world
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_STONE for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 49,10,{"newmap": "ston1", "locx": 0, "locy": 10, "used" : False}))
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 0,9,{"newmap": "town", "locx": 0, "locy": 10, "used" : False}))
