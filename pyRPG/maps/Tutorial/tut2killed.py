# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops
import display
import world

from objects import obj_maker
from objects.General import portal
from objects import Tutorial

def generate():
    world.objects.clear()
    world.map = [[ [display.GREEN, display.BLACK, ';', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(obj_maker.make(portal, world.WORLD_X - 1, 10, {"newmap": "tutboss", "locx": 0, "locy": 10, "used" : False}))
    world.objects.append(obj_maker.make(Tutorial.lava, 0, 0))

    world.map[5][0] = [0, 1, '^', True]
    world.map[26][0] = [0, 1, '^', True]
    world.map[34][0] = [0, 1, '^', True]
    world.map[2][1] = [0, 1, 'L', True]
    world.map[3][1] = [0, 1, 'e', True]
    world.map[4][1] = [0, 1, 'v', True]
    world.map[5][1] = [0, 1, 'e', True]
    world.map[6][1] = [0, 1, 'l', True]
    world.map[7][1] = [0, 1, ' ', True]
    world.map[8][1] = [0, 1, 'a', True]
    world.map[9][1] = [0, 1, 'n', True]
    world.map[10][1] = [0, 1, 'd', True]
    world.map[11][1] = [0, 1, ' ', True]
    world.map[12][1] = [0, 1, 'E', True]
    world.map[13][1] = [0, 1, 'X', True]
    world.map[14][1] = [0, 1, 'P', True]
    world.map[22][1] = [0, 1, 'C', True]
    world.map[23][1] = [0, 1, 'u', True]
    world.map[24][1] = [0, 1, 'r', True]
    world.map[25][1] = [0, 1, 'r', True]
    world.map[26][1] = [0, 1, 'e', True]
    world.map[27][1] = [0, 1, 'n', True]
    world.map[28][1] = [0, 1, 't', True]
    world.map[32][1] = [0, 1, 'C', True]
    world.map[33][1] = [0, 1, 'u', True]
    world.map[34][1] = [0, 1, 'r', True]
    world.map[35][1] = [0, 1, 'r', True]
    world.map[36][1] = [0, 1, 'e', True]
    world.map[37][1] = [0, 1, 'n', True]
    world.map[38][1] = [0, 1, 't', True]
    world.map[23][2] = [0, 1, 'S', True]
    world.map[24][2] = [0, 1, 'p', True]
    world.map[25][2] = [0, 1, 'e', True]
    world.map[26][2] = [0, 1, 'l', True]
    world.map[27][2] = [0, 1, 'l', True]
    world.map[33][2] = [0, 1, 'I', True]
    world.map[34][2] = [0, 1, 't', True]
    world.map[35][2] = [0, 1, 'e', True]
    world.map[36][2] = [0, 1, 'm', True]
    world.map[31][4] = [0, 1, 'C', True]
    world.map[32][4] = [0, 1, 'o', True]
    world.map[33][4] = [0, 1, 'n', True]
    world.map[34][4] = [0, 1, 'g', True]
    world.map[35][4] = [0, 1, 'r', True]
    world.map[36][4] = [0, 1, 'a', True]
    world.map[37][4] = [0, 1, 't', True]
    world.map[38][4] = [0, 1, 'u', True]
    world.map[39][4] = [0, 1, 'l', True]
    world.map[40][4] = [0, 1, 'a', True]
    world.map[41][4] = [0, 1, 't', True]
    world.map[42][4] = [0, 1, 'i', True]
    world.map[43][4] = [0, 1, 'o', True]
    world.map[44][4] = [0, 1, 'n', True]
    world.map[45][4] = [0, 1, 's', True]
    world.map[46][4] = [0, 1, '!', True]
    world.map[25][5] = [0, 1, 'Y', True]
    world.map[26][5] = [0, 1, 'o', True]
    world.map[27][5] = [0, 1, 'u', True]
    world.map[28][5] = [0, 1, ' ', True]
    world.map[29][5] = [0, 1, 'l', True]
    world.map[30][5] = [0, 1, 'e', True]
    world.map[31][5] = [0, 1, 'v', True]
    world.map[32][5] = [0, 1, 'e', True]
    world.map[33][5] = [0, 1, 'l', True]
    world.map[34][5] = [0, 1, 'l', True]
    world.map[35][5] = [0, 1, 'e', True]
    world.map[36][5] = [0, 1, 'd', True]
    world.map[37][5] = [0, 1, ' ', True]
    world.map[38][5] = [0, 1, 'u', True]
    world.map[39][5] = [0, 1, 'p', True]
    world.map[40][5] = [0, 1, ' ', True]
    world.map[41][5] = [0, 1, 'a', True]
    world.map[42][5] = [0, 1, 'n', True]
    world.map[43][5] = [0, 1, 'd', True]
    world.map[44][5] = [0, 1, ' ', True]
    world.map[45][5] = [0, 1, 'g', True]
    world.map[46][5] = [0, 1, 'o', True]
    world.map[47][5] = [0, 1, 't', True]
    world.map[26][6] = [0, 1, 'a', True]
    world.map[27][6] = [0, 1, ' ', True]
    world.map[28][6] = [0, 1, 'n', True]
    world.map[29][6] = [0, 1, 'e', True]
    world.map[30][6] = [0, 1, 'w', True]
    world.map[31][6] = [0, 1, ' ', True]
    world.map[32][6] = [0, 1, 's', True]
    world.map[33][6] = [0, 1, 'p', True]
    world.map[34][6] = [0, 1, 'e', True]
    world.map[35][6] = [0, 1, 'l', True]
    world.map[36][6] = [0, 1, 'l', True]
    world.map[37][6] = [0, 1, '!', True]
    world.map[38][6] = [0, 1, ' ', True]
    world.map[39][6] = [0, 1, 'P', True]
    world.map[40][6] = [0, 1, 'r', True]
    world.map[41][6] = [0, 1, 'e', True]
    world.map[42][6] = [0, 1, 's', True]
    world.map[43][6] = [0, 1, 's', True]
    world.map[44][6] = [0, 1, ' ', True]
    world.map[45][6] = [0, 1, 'E', True]
    world.map[46][6] = [0, 1, 'S', True]
    world.map[47][6] = [0, 1, 'C', True]
    world.map[2][7] = [0, 1, 'B', True]
    world.map[3][7] = [0, 1, 'e', True]
    world.map[4][7] = [0, 1, 'w', True]
    world.map[5][7] = [0, 1, 'a', True]
    world.map[6][7] = [0, 1, 'r', True]
    world.map[7][7] = [0, 1, 'e', True]
    world.map[8][7] = [0, 1, ' ', True]
    world.map[9][7] = [0, 1, 'o', True]
    world.map[10][7] = [0, 1, 'f', True]
    world.map[11][7] = [0, 1, ' ', True]
    world.map[12][7] = [0, 1, 'l', True]
    world.map[13][7] = [0, 1, 'a', True]
    world.map[14][7] = [0, 1, 'v', True]
    world.map[15][7] = [0, 1, 'a', True]
    world.map[16][7] = [0, 1, '!', True]
    world.map[31][7] = [0, 1, 't', True]
    world.map[32][7] = [0, 1, 'o', True]
    world.map[33][7] = [0, 1, ' ', True]
    world.map[34][7] = [0, 1, 'o', True]
    world.map[35][7] = [0, 1, 'p', True]
    world.map[36][7] = [0, 1, 'e', True]
    world.map[37][7] = [0, 1, 'n', True]
    world.map[38][7] = [0, 1, ' ', True]
    world.map[39][7] = [0, 1, 't', True]
    world.map[40][7] = [0, 1, 'h', True]
    world.map[41][7] = [0, 1, 'e', True]
    world.map[42][7] = [0, 1, ' ', True]
    world.map[43][7] = [0, 1, 'm', True]
    world.map[44][7] = [0, 1, 'e', True]
    world.map[45][7] = [0, 1, 'n', True]
    world.map[46][7] = [0, 1, 'u', True]
    world.map[47][7] = [0, 1, '.', True]
    world.map[2][8] = [0, 1, 'I', True]
    world.map[3][8] = [0, 1, 't', True]
    world.map[4][8] = [0, 1, ' ', True]
    world.map[5][8] = [0, 1, 'w', True]
    world.map[6][8] = [0, 1, 'i', True]
    world.map[7][8] = [0, 1, 'l', True]
    world.map[8][8] = [0, 1, 'l', True]
    world.map[9][8] = [0, 1, ' ', True]
    world.map[10][8] = [0, 1, 'k', True]
    world.map[11][8] = [0, 1, 'i', True]
    world.map[12][8] = [0, 1, 'l', True]
    world.map[13][8] = [0, 1, 'l', True]
    world.map[14][8] = [0, 1, ' ', True]
    world.map[15][8] = [0, 1, 'y', True]
    world.map[16][8] = [0, 1, 'o', True]
    world.map[17][8] = [0, 1, 'u', True]
    world.map[18][8] = [0, 1, '.', True]
    world.map[29][8] = [0, 1, 'I', True]
    world.map[30][8] = [0, 1, 'n', True]
    world.map[31][8] = [0, 1, ' ', True]
    world.map[32][8] = [0, 1, 't', True]
    world.map[33][8] = [0, 1, 'h', True]
    world.map[34][8] = [0, 1, 'e', True]
    world.map[35][8] = [0, 1, ' ', True]
    world.map[36][8] = [0, 1, 'm', True]
    world.map[37][8] = [0, 1, 'e', True]
    world.map[38][8] = [0, 1, 'n', True]
    world.map[39][8] = [0, 1, 'u', True]
    world.map[40][8] = [0, 1, ',', True]
    world.map[41][8] = [0, 1, ' ', True]
    world.map[42][8] = [0, 1, 'c', True]
    world.map[43][8] = [0, 1, 'h', True]
    world.map[44][8] = [0, 1, 'o', True]
    world.map[45][8] = [0, 1, 'o', True]
    world.map[46][8] = [0, 1, 's', True]
    world.map[47][8] = [0, 1, 'e', True]
    world.map[2][9] =  [display.RED, display.RED, '#', True]
    world.map[3][9] = [0, 1, ' ', True]
    world.map[4][9] = [0, 1, 'i', True]
    world.map[5][9] = [0, 1, 's', True]
    world.map[6][9] = [0, 1, ' ', True]
    world.map[7][9] = [0, 1, 'l', True]
    world.map[8][9] = [0, 1, 'a', True]
    world.map[9][9] = [0, 1, 'v', True]
    world.map[10][9] = [0, 1, 'a', True]
    world.map[11][9] = [0, 1, '.', True]
    world.map[28][9] = [0, 1, '"', True]
    world.map[29][9] = [0, 1, 'S', True]
    world.map[30][9] = [0, 1, 'p', True]
    world.map[31][9] = [0, 1, 'e', True]
    world.map[32][9] = [0, 1, 'l', True]
    world.map[33][9] = [0, 1, 'l', True]
    world.map[34][9] = [0, 1, 's', True]
    world.map[35][9] = [0, 1, '"', True]
    world.map[36][9] = [0, 1, ' ', True]
    world.map[37][9] = [0, 1, 'a', True]
    world.map[38][9] = [0, 1, 'n', True]
    world.map[39][9] = [0, 1, 'd', True]
    world.map[40][9] = [0, 1, ' ', True]
    world.map[41][9] = [0, 1, 's', True]
    world.map[42][9] = [0, 1, 'e', True]
    world.map[43][9] = [0, 1, 't', True]
    world.map[44][9] = [0, 1, ' ', True]
    world.map[45][9] = [0, 1, 'i', True]
    world.map[46][9] = [0, 1, 't', True]
    world.map[47][9] = [0, 1, '!', True]
    world.map[49][10] = [0, 1, 'O', True]
    world.map[34][12] = [0, 1, 'P', True]
    world.map[35][12] = [0, 1, 'r', True]
    world.map[36][12] = [0, 1, 'e', True]
    world.map[37][12] = [0, 1, 's', True]
    world.map[38][12] = [0, 1, 's', True]
    world.map[39][12] = [0, 1, ' ', True]
    world.map[40][12] = [0, 1, 's', True]
    world.map[41][12] = [0, 1, 'p', True]
    world.map[42][12] = [0, 1, 'a', True]
    world.map[43][12] = [0, 1, 'c', True]
    world.map[44][12] = [0, 1, 'e', True]
    world.map[45][12] = [0, 1, ' ', True]
    world.map[46][12] = [0, 1, 't', True]
    world.map[47][12] = [0, 1, 'o', True]
    world.map[5][13] =  [display.RED, display.RED, '#', True]
    world.map[6][13] =  [display.RED, display.RED, '#', True]
    world.map[7][13] =  [display.RED, display.RED, '#', True]
    world.map[30][13] =  [display.RED, display.RED, '#', True]
    world.map[31][13] =  [display.RED, display.RED, '#', True]
    world.map[32][13] =  [display.RED, display.RED, '#', True]
    world.map[33][13] = [0, 1, 'c', True]
    world.map[34][13] = [0, 1, 'a', True]
    world.map[35][13] = [0, 1, 's', True]
    world.map[36][13] = [0, 1, 't', True]
    world.map[37][13] = [0, 1, ' ', True]
    world.map[38][13] = [0, 1, 'y', True]
    world.map[39][13] = [0, 1, 'o', True]
    world.map[40][13] = [0, 1, 'u', True]
    world.map[41][13] = [0, 1, 'r', True]
    world.map[42][13] = [0, 1, ' ', True]
    world.map[43][13] = [0, 1, 's', True]
    world.map[44][13] = [0, 1, 'p', True]
    world.map[45][13] = [0, 1, 'e', True]
    world.map[46][13] = [0, 1, 'l', True]
    world.map[47][13] = [0, 1, 'l', True]
    world.map[6][14] =  [display.RED, display.RED, '#', True]
    world.map[7][14] =  [display.RED, display.RED, '#', True]
    world.map[8][14] =  [display.RED, display.RED, '#', True]
    world.map[31][14] =  [display.RED, display.RED, '#', True]
    world.map[32][14] =  [display.RED, display.RED, '#', True]
    world.map[33][14] = [0, 1, 'b', True]
    world.map[34][14] = [0, 1, 'u', True]
    world.map[35][14] = [0, 1, 't', True]
    world.map[36][14] = [0, 1, ' ', True]
    world.map[37][14] = [0, 1, 'k', True]
    world.map[38][14] = [0, 1, 'e', True]
    world.map[39][14] = [0, 1, 'e', True]
    world.map[40][14] = [0, 1, 'p', True]
    world.map[41][14] = [0, 1, ' ', True]
    world.map[42][14] = [0, 1, 'a', True]
    world.map[43][14] = [0, 1, 'n', True]
    world.map[44][14] = [0, 1, ' ', True]
    world.map[45][14] = [0, 1, 'e', True]
    world.map[46][14] = [0, 1, 'y', True]
    world.map[47][14] = [0, 1, 'e', True]
    world.map[7][15] =  [display.RED, display.RED, '#', True]
    world.map[8][15] =  [display.RED, display.RED, '#', True]
    world.map[9][15] =  [display.RED, display.RED, '#', True]
    world.map[10][15] =  [display.RED, display.RED, '#', True]
    world.map[11][15] =  [display.RED, display.RED, '#', True]
    world.map[35][15] = [0, 1, 'o', True]
    world.map[36][15] = [0, 1, 'n', True]
    world.map[37][15] = [0, 1, ' ', True]
    world.map[38][15] = [0, 1, 'y', True]
    world.map[39][15] = [0, 1, 'o', True]
    world.map[40][15] = [0, 1, 'u', True]
    world.map[41][15] = [0, 1, 'r', True]
    world.map[42][15] = [0, 1, ' ', True]
    world.map[43][15] = [0, 1, 'm', True]
    world.map[44][15] = [0, 1, 'a', True]
    world.map[45][15] = [0, 1, 'n', True]
    world.map[46][15] = [0, 1, 'a', True]
    world.map[47][15] = [0, 1, '!', True]
    world.map[5][16] =  [display.RED, display.RED, '#', True]
    world.map[6][16] =  [display.RED, display.RED, '#', True]
    world.map[7][16] =  [display.RED, display.RED, '#', True]
    world.map[8][16] =  [display.RED, display.RED, '#', True]
    world.map[9][16] =  [display.RED, display.RED, '#', True]