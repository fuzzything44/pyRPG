import world
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    #world.objects = [world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 49,10,{"newmap": "end", "locx": 1, "locy": 10, "used" : False})]
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 49,10,{"newmap": "stonstart", "locx": 0, "locy": 10, "used" : False}))
    world.map[45][1] = world.WORLD_CHEST

    for x in range(16,25):
        world.map[x][16] = world.WORLD_WALL
        world.map[x][20] = world.WORLD_WALL
    for y in range(16,20):
        world.map[16][y] = world.WORLD_WALL
        world.map[25][y] = world.WORLD_WALL
   
    for x in range(17,24):
        for y in range(17,19):
            world.map[x][y] = [0,".", True]
        
    world.map[19][16] = [0,".", True]
    
    for x in range(42,49):
        world.map[x][0] = world.WORLD_WALL
        world.map[x][5] = world.WORLD_WALL
    for y in range(0,5):
        world.map[42][y] = world.WORLD_WALL
        world.map[48][y] = world.WORLD_WALL
   
    for x in range(43,48):
        for y in range(1,5):
            world.map[x][y] = [0,".", True]
        
    world.map[45][5] = [0,".", True]
    