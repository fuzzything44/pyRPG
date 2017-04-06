import display
import world

from items import t1_mage
from objects import General
from objects import tutorial

from objects.Player import player, player_flags

def give_money(player):
    player.attributes["money"] += 50
    player_flags.set_flag(player, player_flags.TUT_MONEY_GIVEN, 1)

def generate():
    world.objects.clear()

    world.objects.append(General.portal.portal(6, 5, "mage_tut_boss", 25, 10))

    # Save station and merchant as starting towns need. Merchant has t1 mage stuff.
    world.objects.append(General.save_station.save_station(4, 16))
    world.objects.append(General.merchant.merchant(47, 6, [t1_mage.t1_mage_hat(), t1_mage.t1_mage_pants(), t1_mage.t1_mage_ring(), t1_mage.t1_mage_shirt(), t1_mage.t1_mage_weapon()]))

    # Portals. One right (tut area), one above (exit) and a couple to get to town second floor
    world.objects.append(General.portal.portal(1, 5, "mage_start_upper", 2, 5))
    world.objects.append(General.portal.portal(49, 9, "mage_tut_1", 1, 9))
    world.objects.append(General.level_portal.level_portal(24, 0, "test_dungeon_start", 24, 18, 5))
    world.objects.append(General.level_portal.level_portal(41, 15, "mage_start_upper", 41, 14, 10))
    world.objects.append(General.portal.portal(1, 1, "mage_start_upper", 1, 2))

    # Add tutorial guy who gives you equip money.
    dialogue_tree = General.npc.dialogue_tree()
    dialogue_tree.add_node("start", General.npc.node("Welcome to Mysticalia,\n the mage town!", ("Bye", "exit")))
    dialogue_tree.add_exit("exit", 0)
    dialogue_tree.add_exit("money", 1, give_money)
    world.objects.append(tutorial.quest_giver.quest_giver(33, 14, dialogue_tree, "upper"))

    world.map = [[ [display.WHITE, display.BLACK, '.', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.map[0][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[2][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[10][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[11][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[12][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[13][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[17][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[18][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[19][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[20][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[21][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[22][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[23][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[25][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[26][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[27][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[28][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[29][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[30][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[36][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[37][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[44][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][0] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][1] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][1] =  [display.GREEN, display.BLACK, '*', True]
    world.map[2][1] =  [display.GREEN, display.BLACK, '*', True]
    world.map[3][1] =  [display.GREEN, display.BLACK, '*', True]
    world.map[4][1] =  [display.GREEN, display.BLACK, '*', True]
    world.map[5][1] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][1] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][2] =  [display.GREEN, display.BLACK, '*', True]
    world.map[2][2] =  [display.GREEN, display.BLACK, '*', True]
    world.map[3][2] =  [display.GREEN, display.BLACK, '*', True]
    world.map[4][2] =  [display.GREEN, display.BLACK, '*', True]
    world.map[49][2] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][3] =  [display.GREEN, display.BLACK, '*', True]
    world.map[2][3] =  [display.GREEN, display.BLACK, '*', True]
    world.map[3][3] =  [display.GREEN, display.BLACK, '*', True]
    world.map[4][3] =  [display.GREEN, display.BLACK, '*', True]
    world.map[5][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][3] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[2][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[10][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[11][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[12][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[13][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[17][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[18][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[19][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[20][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[21][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[22][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[23][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[24][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[25][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[26][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[27][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[28][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[29][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[30][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[36][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[37][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[44][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][4] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][5] =  [display.GREEN, display.BLACK, '*', True]
    world.map[2][5] =  [display.GREEN, display.BLACK, '*', True]
    world.map[3][5] =  [display.GREEN, display.BLACK, '*', True]
    world.map[4][5] =  [display.GREEN, display.BLACK, '*', True]
    world.map[5][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][5] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[48][5] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[49][5] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[2][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][6] =  [display.GREEN, display.BLACK, '*', True]
    world.map[4][6] =  [display.GREEN, display.BLACK, '*', True]
    world.map[5][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][6] =  [display.YELLOW, display.BLACK, '!', False]
    world.map[49][6] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][7] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][8] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][9] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][10] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][11] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][11] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][11] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][11] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[36][12] = [0, 1, '-', True]
    world.map[37][12] = [0, 1, '-', True]
    world.map[38][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][12] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][13] =  [display.GREEN, display.BLACK, '*', True]
    world.map[7][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][13] =  [display.GREEN, display.BLACK, '*', True]
    world.map[35][13] =  [display.GREEN, display.BLACK, '*', True]
    world.map[36][13] =  [display.GREEN, display.BLACK, '*', True]
    world.map[37][13] =  [display.GREEN, display.BLACK, '*', True]
    world.map[38][13] =  [display.GREEN, display.BLACK, '*', True]
    world.map[39][13] =  [display.GREEN, display.BLACK, '*', True]
    world.map[40][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][13] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[5][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[6][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[7][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[8][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[9][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[33][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[34][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[35][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[36][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[37][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[38][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[39][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[40][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[41][14] =  [display.GREEN, display.BLACK, '*', True]
    world.map[42][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][14] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[5][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[6][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[7][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[8][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[9][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[33][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[34][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[35][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[36][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[37][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[38][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[39][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[40][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[41][15] =  [display.GREEN, display.BLACK, '*', True]
    world.map[42][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][15] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[5][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[6][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[7][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[8][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[9][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[35][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[36][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[37][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[38][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[39][16] =  [display.GREEN, display.BLACK, '*', True]
    world.map[40][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][16] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[36][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[37][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][17] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][18] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][18] =  [display.WHITE, display.BLACK, '#', False]
    world.map[0][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[1][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[2][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[3][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[4][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[5][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[6][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[7][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[8][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[9][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[10][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[11][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[12][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[13][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[14][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[15][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[16][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[17][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[18][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[19][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[20][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[21][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[22][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[23][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[24][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[25][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[26][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[27][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[28][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[29][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[30][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[31][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[32][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[33][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[34][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[35][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[36][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[37][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[38][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[39][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[40][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[41][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[42][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[43][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[44][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[45][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[46][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[47][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[48][19] =  [display.WHITE, display.BLACK, '#', False]
    world.map[49][19] =  [display.WHITE, display.BLACK, '#', False]