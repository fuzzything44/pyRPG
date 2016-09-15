import display
import world

from objects.General import portal
from objects import world_object

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 25,8,{"newmap": "tut1", "locx": 0, "locy": 10, "used" : False}))

    for x in range(22,29):
        world.map[x][5] = world.WORLD_WALL
        world.map[x][10] = world.WORLD_WALL
    for y in range(5,11):
        world.map[22][y] = world.WORLD_WALL
        world.map[28][y] = world.WORLD_WALL
   
    for x in range(23,28):
        for y in range(6,10):
            world.map[x][y] = [display.WHITE, display.BLACK, ".", True]
        
    world.map[25][10] = [display.WHITE, display.BLACK, ".", True]
                         
    world.map[25][12] = [display.WHITE, display.BLACK, 'W', True]
    world.map[24][13] = [display.WHITE, display.BLACK, 'A', True]
    world.map[25][13] = [display.WHITE, display.BLACK, 'S', True]
    world.map[26][13] = [display.WHITE, display.BLACK, 'D', True]
                         
    world.map[22][14] = [display.WHITE, display.BLACK, 'T', True]
    world.map[23][14] = [display.WHITE, display.BLACK, 'O', True]
                         
    world.map[25][14] = [display.WHITE, display.BLACK, 'M', True]
    world.map[26][14] = [display.WHITE, display.BLACK, 'O', True]
    world.map[27][14] = [display.WHITE, display.BLACK, 'V', True]
    world.map[28][14] = [display.WHITE, display.BLACK, 'E', True]
                         
    world.map[19][17] = [display.WHITE, display.BLACK, 'Y', True]
    world.map[20][17] = [display.WHITE, display.BLACK, 'O', True]
    world.map[21][17] = [display.WHITE, display.BLACK, 'U', True]
    world.map[23][17] = [display.WHITE, display.BLACK, '>', True]
                         
    world.map[27][17] = [display.WHITE, display.BLACK, '<', True]
    world.map[29][17] = [display.WHITE, display.BLACK, 'Y', True]
    world.map[30][17] = [display.WHITE, display.BLACK, 'O', True]
    world.map[31][17] = [display.WHITE, display.BLACK, 'U', True]
                         
    world.map[22][16] = [display.BLUE, display.BLUE, 'O', True]
    world.map[23][16] = [display.WHITE, display.BLACK, '=', True]
    world.map[24][16] = [display.WHITE, display.BLACK, 'P', True]
    world.map[25][16] = [display.WHITE, display.BLACK, 'o', True]
    world.map[26][16] = [display.WHITE, display.BLACK, 'r', True]
    world.map[27][16] = [display.WHITE, display.BLACK, 't', True]
    world.map[28][16] = [display.WHITE, display.BLACK, 'a', True]
    world.map[29][16] = [display.WHITE, display.BLACK, 'l', True]
