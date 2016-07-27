import world
from items import item
from items import goodDagger, t2wand, goodSword
from objects import *

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    #world.objects = [world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 49,10,{"newmap": "end", "locx": 1, "locy": 10, "used" : False})]
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 49,10,{"newmap": "stonstart", "locx": 0, "locy": 10, "used" : False}))

   #house 1
    for x in range(10,20):
        world.map[x][0] = world.WORLD_WALL
        world.map[x][5] = world.WORLD_WALL
    for y in range(0,6):
        world.map[10][y] = world.WORLD_WALL
        world.map[20][y] = world.WORLD_WALL
   
    for x in range(11,20):
        for y in range(1,5):
            world.map[x][y] = [0,".", True]

#house 2
    for x in range(16,25):
        world.map[x][16] = world.WORLD_WALL
        world.map[x][19] = world.WORLD_WALL
    for y in range(16,20):
        world.map[16][y] = world.WORLD_WALL
        world.map[25][y] = world.WORLD_WALL
   
    for x in range(17,25):
        for y in range(17,19):
            world.map[x][y] = [0,".", True]

    
#house 3
    for x in range(42,49):
        world.map[x][0] = world.WORLD_WALL
        world.map[x][5] = world.WORLD_WALL
    for y in range(0,5):
        world.map[42][y] = world.WORLD_WALL
        world.map[48][y] = world.WORLD_WALL
   
    for x in range(43,48):
        for y in range(1,5):
            world.map[x][y] = [0,".", True]
#house 4
    for x in range(40,49):
        world.map[x][14] = world.WORLD_WALL
        world.map[x][19] = world.WORLD_WALL
    for y in range(14,20):
        world.map[40][y] = world.WORLD_WALL
        world.map[49][y] = world.WORLD_WALL
   
    for x in range(41,49):
        for y in range(15,19):
            world.map[x][y] = [0,".", True]

    world.map[45][5] = [0,".", True]
    world.map[20][16] = [0,".", True]
    world.map[15][5] = [0,".", True]
    world.map[44][14] = [0,".", True]

    world.map[45][1] = world.WORLD_CHEST
    world.objects.append(world_object.world_object(chest.chest_update, chest.chest_collide, chest.chest_char, chest.chest_col, chest.chest_type, 45, 2, {"canopen" : False, "contents" : \
        [item.item(goodDagger.name, goodDagger.type, goodDagger.on_equip, goodDagger.on_unequip, 1, goodDagger.attributes), item.item(goodSword.name, goodSword.type, goodSword.on_equip, goodSword.on_unequip, 1, goodSword.attributes), item.item(t2wand.name, t2wand.type, t2wand.on_equip, t2wand.on_unequip, 1, t2wand.attributes)]}))    