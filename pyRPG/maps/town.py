import display
import world

from items import item
from items import t1_warrior
from items import t1_mage
from items import t1_thief
from items import enemy_info

from objects.General import bg_changer
from objects.Loot import chest
from objects.General import portal
from objects import General
from objects import world_object

def generate():
    world.objects = []
    world.map = [[ [display.GREEN, display.BLACK, ';', True] for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects.append(portal.portal(49, 10, "stonedungeon.start", 2, 10))
    world.objects.append(General.level_portal.level_portal(25, 0, "lavadungeon.start", 2, 10, 5))
    world.objects.append(General.npc.npc(43, 4, "Hello! Welcome to pyRPG!\nI would suggest entering the\n portal to the right.\nIt leads to the\n Forgotten Catacombs."))

    # Upper left. This is the WARRIOR house
    for x in range(10,20): # Make walls
        world.map[x][0] = [display.WHITE, display.BLACK, '#', False]
        world.map[x][5] = [display.WHITE, display.BLACK, '#', False]
    for y in range(0,6):
        world.map[10][y] = [display.WHITE, display.BLACK, '#', False]
        world.map[20][y] = [display.WHITE, display.BLACK, '#', False]
   
    for x in range(11,20): # Fill inside
        for y in range(1,5):
            world.map[x][y] = [display.WHITE, display.BLACK, ".", True]
    world.objects.append(bg_changer.bg_changer(15, 5, "warrior", [display.WHITE, display.BLACK, '.', True]))
    world.map[15][1] = [display.YELLOW, display.YELLOW, '@', False] # Chest in house
    war_chest_items = [\
        item.item(t1_warrior.hat_name   , t1_warrior.hat_type   , t1_warrior.hat_value   , t1_warrior.hat_on_equip   , t1_warrior.hat_on_unequip   , 1, t1_warrior.hat_attributes   ),\
        item.item(t1_warrior.shirt_name , t1_warrior.shirt_type , t1_warrior.shirt_value , t1_warrior.shirt_on_equip , t1_warrior.shirt_on_unequip , 1, t1_warrior.shirt_attributes ),\
        item.item(t1_warrior.weapon_name, t1_warrior.weapon_type, t1_warrior.weapon_value, t1_warrior.weapon_on_equip, t1_warrior.weapon_on_unequip, 1, t1_warrior.weapon_attributes),\
        item.item(t1_warrior.ring_name  , t1_warrior.ring_type  , t1_warrior.ring_value  , t1_warrior.ring_on_equip  , t1_warrior.ring_on_unequip  , 1, t1_warrior.ring_attributes  ),\
        item.item(t1_warrior.pants_name , t1_warrior.pants_type , t1_warrior.pants_value , t1_warrior.pants_on_equip , t1_warrior.pants_on_unequip , 1, t1_warrior.pants_attributes )\
      ]

    world.objects.append(chest.chest(15, 2, war_chest_items)) # This chest contains stuff for warriors.
    world.objects.append(chest.chest(14, 1, war_chest_items)) # This chest contains stuff for warriors.
    world.objects.append(chest.chest(16, 1, war_chest_items)) # This chest contains stuff for warriors.


    # Lower left. This is the MAGE house
    for x in range(16,25):
        world.map[x][16] = [display.WHITE, display.BLACK, '#', False]
        world.map[x][19] = [display.WHITE, display.BLACK, '#', False]
    for y in range(16,20):
        world.map[16][y] = [display.WHITE, display.BLACK, '#', False]
        world.map[25][y] = [display.WHITE, display.BLACK, '#', False]
   
    for x in range(17,25):
        for y in range(17,19):
            world.map[x][y] = [display.WHITE, display.BLACK, ".", True]
    world.objects.append(bg_changer.bg_changer(20, 16, "mage", [display.WHITE, display.BLACK, '.', True]))
    world.map[24][18] = [display.YELLOW, display.YELLOW, '@', False] # Chest in house
    mage_chest_items = [\
        item.item(t1_mage.hat_name   , t1_mage.hat_type   , t1_mage.hat_value   , t1_mage.hat_on_equip   , t1_mage.hat_on_unequip   , 1, t1_mage.hat_attributes   ),\
        item.item(t1_mage.shirt_name , t1_mage.shirt_type , t1_mage.shirt_value , t1_mage.shirt_on_equip , t1_mage.shirt_on_unequip , 1, t1_mage.shirt_attributes ),\
        item.item(t1_mage.weapon_name, t1_mage.weapon_type, t1_mage.weapon_value, t1_mage.weapon_on_equip, t1_mage.weapon_on_unequip, 1, t1_mage.weapon_attributes),\
        item.item(t1_mage.ring_name  , t1_mage.ring_type  , t1_mage.ring_value  , t1_mage.ring_on_equip  , t1_mage.ring_on_unequip  , 1, t1_mage.ring_attributes  ),\
        item.item(t1_mage.pants_name , t1_mage.pants_type , t1_mage.pants_value , t1_mage.pants_on_equip , t1_mage.pants_on_unequip , 1, t1_mage.pants_attributes )\
      ]
    world.objects.append(chest.chest(24, 17, mage_chest_items)) # This chest contains stuff for mages.
    world.objects.append(chest.chest(23, 18, mage_chest_items))


    # Top right house. This is the EVERYONE house
    for x in range(42,49): # Make walls
        world.map[x][0] = [display.WHITE, display.BLACK, '#', False]
        world.map[x][5] = [display.WHITE, display.BLACK, '#', False]
    for y in range(0,5):
        world.map[42][y] = [display.WHITE, display.BLACK, '#', False]
        world.map[48][y] = [display.WHITE, display.BLACK, '#', False]
   
    for x in range(43,48): # Fill inside
        for y in range(1,5):
            world.map[x][y] = [0, 1, ".", True]
    world.map[45][5] = [0, 1, ".", True] # Doorway

    world.map[45][1] = [display.YELLOW, display.YELLOW, '@', False] # Chest in house
    all_chest_items = [\
        item.item(enemy_info.ring_name , enemy_info.ring_type , enemy_info.ring_value , enemy_info.ring_on_equip , enemy_info.ring_on_unequip , 1, enemy_info.ring_attributes ),\
        item.item(enemy_info.hat_name  , enemy_info.hat_type  , enemy_info.hat_value  , enemy_info.hat_on_equip  , enemy_info.hat_on_unequip  , 1, enemy_info.hat_attributes  ),\
        item.item(enemy_info.pants_name, enemy_info.pants_type, enemy_info.pants_value, enemy_info.pants_on_equip, enemy_info.pants_on_unequip, 1, enemy_info.pants_attributes)\
      ]
    world.objects.append(chest.chest(45, 2, all_chest_items)) # This chest contains stuff for everyone.
    world.objects.append(chest.chest(44, 1, all_chest_items)) # And the interaction on the left...
    world.objects.append(chest.chest(46, 1, all_chest_items)) # And on the right

    # Lower right. This is the THIEF house
    for x in range(40,49):
        world.map[x][14] = [display.WHITE, display.BLACK, '#', False]
        world.map[x][19] = [display.WHITE, display.BLACK, '#', False]
    for y in range(14,20):
        world.map[40][y] = [display.WHITE, display.BLACK, '#', False]
        world.map[49][y] = [display.WHITE, display.BLACK, '#', False]
   
    for x in range(41,49):
        for y in range(15,19):
            world.map[x][y] = [0, 1, ".", True]
    world.objects.append(bg_changer.bg_changer(44, 14, "thief", [display.WHITE, display.BLACK, '.', True]))
    world.map[44][18] = [display.YELLOW, display.YELLOW, '@', False] # Chest in house
    thief_chest_items = [\
        item.item(t1_thief.hat_name   , t1_thief.hat_type   , t1_thief.hat_value   , t1_thief.hat_on_equip   , t1_thief.hat_on_unequip   , 1, t1_thief.hat_attributes   ),\
        item.item(t1_thief.shirt_name , t1_thief.shirt_type , t1_thief.shirt_value , t1_thief.shirt_on_equip , t1_thief.shirt_on_unequip , 1, t1_thief.shirt_attributes ),\
        item.item(t1_thief.weapon_name, t1_thief.weapon_type, t1_thief.weapon_value, t1_thief.weapon_on_equip, t1_thief.weapon_on_unequip, 1, t1_thief.weapon_attributes),\
        item.item(t1_thief.ring_name  , t1_thief.ring_type  , t1_thief.ring_value  , t1_thief.ring_on_equip  , t1_thief.ring_on_unequip  , 1, t1_thief.ring_attributes  ),\
        item.item(t1_thief.pants_name , t1_thief.pants_type , t1_thief.pants_value , t1_thief.pants_on_equip , t1_thief.pants_on_unequip , 1, t1_thief.pants_attributes )\
      ]

    world.objects.append(chest.chest(43, 18, thief_chest_items)) # This chest contains stuff for thiefs.
    world.objects.append(chest.chest(45, 18, thief_chest_items)) 
    world.objects.append(chest.chest(44, 17, thief_chest_items)) 


 