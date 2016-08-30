import display
import world
from objects import *
def pchar(this):
    if this.attributes["used"]:
        return '\0'
    return 'o'
def pcolor(this):
    return 0

def generate():
    world.objects = []
    world.map = [[ world.WORLD_NOTHING for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    port = world_object.world_object(portal.update, portal.collide, pchar, pcolor, portal.type, 33,12,{"newmap": "town", "locx": 0, "locy": 0, "used" : False})
    world.objects.append(port)
    world.map[5][4] = [display.YELLOW, display.BLACK, 'p', False]
    world.map[6][4] = [display.YELLOW, display.BLACK, 'y', False]
    world.map[7][4] = [display.RED, display.BLACK, 'R', False]
    world.map[8][4] = [display.GREEN, display.BLACK, 'P', False]
    world.map[9][4] = [display.BLUE, display.BLACK, 'G', False]
    world.map[11][4] = [display.WHITE, display.BLACK, 'W', False]
    world.map[12][4] = [display.WHITE, display.BLACK, 'a', False]
    world.map[13][4] = [display.WHITE, display.BLACK, 's', False]
    world.map[15][4] = [display.WHITE, display.BLACK, 'M', False]
    world.map[16][4] = [display.WHITE, display.BLACK, 'a', False]
    world.map[17][4] = [display.WHITE, display.BLACK, 'd', False]
    world.map[18][4] = [display.WHITE, display.BLACK, 'e', False]
    world.map[20][4] = [display.WHITE, display.BLACK, 'B', False]
    world.map[21][4] = [display.WHITE, display.BLACK, 'y', False]
    world.map[22][4] = [display.WHITE, display.BLACK, ':', False]

    world.map[11][6] = [display.WHITE, display.BLACK, 'T', False]
    world.map[12][6] = [display.WHITE, display.BLACK, 'a', False]
    world.map[13][6] = [display.WHITE, display.BLACK, 'n', False]
    world.map[14][6] = [display.WHITE, display.BLACK, 'n', False]
    world.map[15][6] = [display.WHITE, display.BLACK, 'e', False]
    world.map[16][6] = [display.WHITE, display.BLACK, 'r', False]
    world.map[18][6] = [display.WHITE, display.BLACK, 'M', False]
    world.map[19][6] = [display.WHITE, display.BLACK, '.', False]
                           
    world.map[11][7] = [display.WHITE, display.BLACK, 'M', False]
    world.map[12][7] = [display.WHITE, display.BLACK, 'a', False]
    world.map[13][7] = [display.WHITE, display.BLACK, 't', False]
    world.map[14][7] = [display.WHITE, display.BLACK, 't', False]
    world.map[15][7] = [display.WHITE, display.BLACK, 'h', False]
    world.map[16][7] = [display.WHITE, display.BLACK, 'e', False]
    world.map[17][7] = [display.WHITE, display.BLACK, 'w', False]
    world.map[19][7] = [display.WHITE, display.BLACK, 'K', False]
    world.map[20][7] = [display.WHITE, display.BLACK, '.', False]
                           
    world.map[11][8] = [display.WHITE, display.BLACK, 'A', False]
    world.map[12][8] = [display.WHITE, display.BLACK, 'l', False]
    world.map[13][8] = [display.WHITE, display.BLACK, 'e', False]
    world.map[14][8] = [display.WHITE, display.BLACK, 'x', False]
    world.map[16][8] = [display.WHITE, display.BLACK, 'P', False]
    world.map[17][8] = [display.WHITE, display.BLACK, '.', False]
                           
    world.map[11][9] = [display.WHITE, display.BLACK, 'C', False]
    world.map[12][9] = [display.WHITE, display.BLACK, 'o', False]
    world.map[13][9] = [display.WHITE, display.BLACK, 'r', False]
    world.map[14][9] = [display.WHITE, display.BLACK, 'y', False]
    world.map[16][9] = [display.WHITE, display.BLACK, 'R', False]
    world.map[17][9] = [display.WHITE, display.BLACK, '.', False]
    
    world.map[25][12] = [display.WHITE, display.BLACK, 'T', False]
    world.map[26][12] = [display.WHITE, display.BLACK, 'h', False]
    world.map[27][12] = [display.WHITE, display.BLACK, 'a', False]
    world.map[28][12] = [display.WHITE, display.BLACK, 'n', False]
    world.map[29][12] = [display.WHITE, display.BLACK, 'k', False]
    world.map[30][12] = [display.WHITE, display.BLACK, 's', False]
    world.map[32][12] = [display.WHITE, display.BLACK, 'F', False]
    
    world.map[34][12] = [display.WHITE, display.BLACK, 'r', False]
    world.map[36][12] = [display.WHITE, display.BLACK, 'P', False]
    world.map[37][12] = [display.WHITE, display.BLACK, 'l', False]
    world.map[38][12] = [display.WHITE, display.BLACK, 'a', False]
    world.map[39][12] = [display.WHITE, display.BLACK, 'y', False]
    world.map[40][12] = [display.WHITE, display.BLACK, 'i', False]
    world.map[41][12] = [display.WHITE, display.BLACK, 'n', False]
    world.map[42][12] = [display.WHITE, display.BLACK, 'g', False]
    world.map[43][12] = [display.WHITE, display.BLACK, '!', False]
    