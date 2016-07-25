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
    world.map[5][4] = [6, 'p', False]
    world.map[6][4] = [6, 'y', False]
    world.map[7][4] = [1, 'R', False]
    world.map[8][4] = [5, 'P', False]
    world.map[9][4] = [4, 'G', False]
    world.map[10][4] = [0, ' ', False]
    world.map[11][4] = [0, 'W', False]
    world.map[12][4] = [0, 'a', False]
    world.map[13][4] = [0, 's', False]
    world.map[14][4] = [0, ' ', False]
    world.map[15][4] = [0, 'M', False]
    world.map[16][4] = [0, 'a', False]
    world.map[17][4] = [0, 'd', False]
    world.map[18][4] = [0, 'e', False]
    world.map[19][4] = [0, ' ', False]
    world.map[20][4] = [0, 'B', False]
    world.map[21][4] = [0, 'y', False]
    world.map[22][4] = [0, ':', False]
    world.map[23][4] = [0, ' ', False]

    world.map[11][6] = [0, 'T', False]
    world.map[12][6] = [0, 'a', False]
    world.map[13][6] = [0, 'n', False]
    world.map[14][6] = [0, 'n', False]
    world.map[15][6] = [0, 'e', False]
    world.map[16][6] = [0, 'r', False]
    world.map[17][6] = [0, ' ', False]
    world.map[18][6] = [0, 'M', False]
    world.map[19][6] = [0, '.', False]

    world.map[11][7] = [0, 'M', False]
    world.map[12][7] = [0, 'a', False]
    world.map[13][7] = [0, 't', False]
    world.map[14][7] = [0, 't', False]
    world.map[15][7] = [0, 'h', False]
    world.map[16][7] = [0, 'e', False]
    world.map[17][7] = [0, 'w', False]
    world.map[18][7] = [0, ' ', False]
    world.map[19][7] = [0, 'K', False]
    world.map[20][7] = [0, '.', False]

    world.map[11][8] = [0, 'A', False]
    world.map[12][8] = [0, 'l', False]
    world.map[13][8] = [0, 'e', False]
    world.map[14][8] = [0, 'x', False]
    world.map[15][8] = [0, ' ', False]
    world.map[16][8] = [0, 'P', False]
    world.map[17][8] = [0, '.', False]

    world.map[11][9] = [0, 'C', False]
    world.map[12][9] = [0, 'o', False]
    world.map[13][9] = [0, 'r', False]
    world.map[14][9] = [0, 'y', False]
    world.map[15][9] = [0, ' ', False]
    world.map[16][9] = [0, 'R', False]
    world.map[17][9] = [0, '.', False]
    
    world.map[25][12] = [0, 'T', False]
    world.map[26][12] = [0, 'h', False]
    world.map[27][12] = [0, 'a', False]
    world.map[28][12] = [0, 'n', False]
    world.map[29][12] = [0, 'k', False]
    world.map[30][12] = [0, 's', False]
    world.map[31][12] = [0, ' ', False]
    world.map[32][12] = [0, 'F', False]
    
    world.map[34][12] = [0, 'r', False]
    world.map[35][12] = [0, ' ', False]
    world.map[36][12] = [0, 'P', False]
    world.map[37][12] = [0, 'l', False]
    world.map[38][12] = [0, 'a', False]
    world.map[39][12] = [0, 'y', False]
    world.map[40][12] = [0, 'i', False]
    world.map[41][12] = [0, 'n', False]
    world.map[42][12] = [0, 'g', False]
    world.map[43][12] = [0, '!', False]

    #Tanner McCormack
    #Matthew Kelley
    #Alex Pruitt
    #Cory Reck
    