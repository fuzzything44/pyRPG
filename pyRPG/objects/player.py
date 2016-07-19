import time
import sys

from objects import attack
import display
from items import item
import world
from objects import world_object
from spells import spell
from spells import fireball

def player_update(this, delta_time):
    display.printc(8, 0, str(int(this.attributes["HP"])) + "/" + str(int(this.attributes["maxHP"])) + "  ")
    display.printc(8, 1, str(int(this.attributes["MP"])) + "/" + str(int(this.attributes["maxMP"])) + "  ")
    display.printc(10, 2, str(this.attributes["money"]) + "     ")
    display.printc(12, 3, str(this.attributes["level"]))
    display.printc(5, 4, str(this.attributes["level"] ** 2 - this.attributes["EXP"]) + " to level        ")
    try:
        if display.keyDown(ord('W')) & (not "del_up" in this.attributes["effects"]):
            if world.map[this.X][this.Y - 1][2]:
                this.Y -= 1
            if this.Y < 0:
                this.Y = 0
            this.attributes["effects"]["del_up"] = [lambda a, b: 0, lambda x: 0, this.attributes["mov_spd"]]

        if display.keyDown(ord('S')) & (not "del_down" in this.attributes["effects"]):
            if world.map[this.X][this.Y + 1][2]:
                this.Y += 1
            if this.Y > 22:
                this.Y = 22
            this.attributes["effects"]["del_down"] = [lambda a, b: 0, lambda x: 0, this.attributes["mov_spd"]]
        if display.keyDown(ord('A')) & (not "del_left" in this.attributes["effects"]):
            if world.map[this.X - 1][this.Y][2]:
                this.X -= 1
            if this.X < 0:
                this.X = 0
            this.attributes["effects"]["del_left"] = [lambda a, b: 0, lambda x: 0, this.attributes["mov_spd"]]
        if display.keyDown(ord('D')) & (not "del_right" in this.attributes["effects"]):
            if world.map[this.X + 1][this.Y][2]:
                this.X += 1
            if this.X > 77:
                this.X = 77
            this.attributes["effects"]["del_right"] = [lambda a, b: 0, lambda x: 0, this.attributes["mov_spd"]]
        if display.keyDown(ord(' ')) & this.attributes["can_cast"]:
            this.attributes["spell"].cast(this)
            this.attributes["can_cast"] = False
        else:
            this.attributes["can_cast"] = True
        # Attacks!
        if (display.keyDown(ord('I'))) & (this.Y != 0) & (world.map[this.X][this.Y - 1][2]) & (not "del_atk" in this.attributes["effects"]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, this.X, this.Y - 1, \
                {"movex" : 0, "movey": -1, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["weapon"].attributes["damage"], "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
            this.attributes["effects"]["del_atk"] = [lambda a, b: 0, lambda x: 0, this.attributes["atk_spd"]]
        if (display.keyDown(ord('J'))) & (this.X != 0) & (world.map[this.X - 1][this.Y][2]) & (not "del_atk" in this.attributes["effects"]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, this.X - 1, this.Y, \
                {"movex" : -1, "movey": 0, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["weapon"].attributes["damage"], "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
            this.attributes["effects"]["del_atk"] = [lambda a, b: 0, lambda x: 0, this.attributes["atk_spd"]]
        if (display.keyDown(ord('K'))) & (this.Y != 19) & (world.map[this.X][this.Y + 1][2]) & (not "del_atk" in this.attributes["effects"]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, this.X, this.Y + 1, \
                {"movex" : 0, "movey": 1, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["weapon"].attributes["damage"], "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
            this.attributes["effects"]["del_atk"] = [lambda a, b: 0, lambda x: 0, this.attributes["atk_spd"]]
        if (display.keyDown(ord('L'))) & (this.X != 49) & (world.map[this.X + 1][this.Y][2]) & (not "del_atk" in this.attributes["effects"]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, this.X + 1, this.Y, \
                {"movex" : 1, "movey": 0, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["weapon"].attributes["damage"], "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
            this.attributes["effects"]["del_atk"] = [lambda a, b: 0, lambda x: 0, this.attributes["atk_spd"]]

        if display.keyDown(display.CONST.VK_LSHIFT):
            pass # Use item

    except:
        pass
    
    eff_del_list = []
    # Update all effects.
    for eff in this.attributes["effects"]:
        this.attributes["effects"][eff][0](this, delta_time)       # Tick code
        this.attributes["effects"][eff][2] -= delta_time           # Lower time
        if this.attributes["effects"][eff][2] <= 0:                # Remove effect
            eff_del_list.append(eff)
    for to_del in eff_del_list:
        this.attributes["effects"][to_del][1](this)
        del this.attributes["effects"][to_del]
    del eff_del_list
    if this.attributes["HP"] <= 0:
        display.printc(33, 9,  "+++++++++++++", display.RED)
        display.printc(33, 10, "+ You DIED! +", display.RED)
        display.printc(33, 11, "+++++++++++++", display.RED)
        key = -1
        while key == -1:
            key = display.getch()

        display.end()

def collide(this, oth):
    if oth.type == "money":
        this.attributes["money"] += oth.attributes["value"];
        # Now to delete it
        world.to_del.append(oth)

def player_char(this):
    return 'P'

def player_color(this):
    if "poison" in this.attributes["effects"]:
        return display.GREEN
    if "fire" in this.attributes["effects"]:
        return display.RED
    if "regen" in this.attributes["effects"]:
        return display.BLUE
    if this.attributes["money"] > 50:
        return display.YELLOW
    return display.WHITE

def heal(player):
    player.attributes["HP"] += 25
    if player.attributes["HP"] > player.attributes["maxHP"]:
        player.attributes["HP"] = player.attributes["maxHP"]

player_type = "player"
# effects is a dictionary of (string) effect name to [(func) tick(player, delta_time), (func) on_remove(player), time_left]
# items is a dictionary of (string) item name to ITEM or to SPELL
# TODO: change current spell to conform to basic spells. Also have basic equips in inventory.
player_attributes =                     \
    { "maxHP" : 100.0,                  \
      "HP" : 100.0,                     \
      "maxMP" : 50,                     \
      "MP" : 50,                        \
      "money" : 0,                      \
      "effects" : {},                   \
      "EXP" : 0,                        \
      "level" : 1,                      \
      "items" : [],                     \
      "spell" : spell.spell(25, fireball.fireball, ["\\|/", "-0-", "/|\\"]), \
      "weapon" : item.item("Broken Sword", "weapon", lambda x, y: 0, lambda x, y: 0),    \
      "hat" : item.item("Cloth Hat", "hat", lambda x, y: 0, lambda x, y: 0),             \
      "shirt" : item.item("Cloth Shirt", "shirt", lambda x, y: 0, lambda x, y: 0),       \
      "pants" : item.item("Cloth Pants", "pants", lambda x, y: 0, lambda x, y: 0),       \
      "ring" : item.item("Useless ring", "ring", lambda x, y: 0, lambda x, y: 0),        \
      "consumable" : item.item("Nothing", "consumable", lambda x, y: 0, lambda x, y: 0), \
      "mov_spd" : 30,                           \
      "atk_spd" : 150,                            \
      "can_cast" : True,                          \
      "magic" : 5
    }


def set_active(type):
    options = [] # All options to go in the menu.
    for opt in world.player.attributes["items"]:
        if opt.type == type:
            options.append(opt)

    # Now break into pages.
    #Page size is 20 max - 2 for title - 3 for forward/back/exit options = 15 options/page
    PAGE_SIZE = 15
    pages = [[]]
    for opt in options:             # Add every object to the list.
        if len(pages[-1]) == PAGE_SIZE:    # If list overflow, add a new page
            pages.append([])
        # Add option to last element in pages. Also should edits it to give amount held too.
        pages[-1].append([opt.name + "(" + str(opt.amount) + ")", lambda: 0])

    curr_page = 0
    choice = 1
    # So if they choose 1 (prev. page) or 2 (next) page, menu is re-displayed.
    while (choice == 1) | (choice == 2):
        empty_lists = [[] for x in range(len(pages[curr_page]) + 3)]
        choice = display.menu("Set to what?", empty_lists, ["Back", lambda: 0], ["Next Page", lambda: 0], ["Previous Page", lambda: 0], *pages[curr_page])
        if choice == 1:
            curr_page = max(curr_page - 1, 0)
        if choice == 2:
            curr_page += 1
            if curr_page == len(pages):
                curr_page -= 1
    # They chose back
    if not choice:
        return
    # Here we have to figure out what they chose.
    # So if they are on page n, then we must add 15 * n to the items index. So 0th page is items 0-15, 1st page is 15-29, etc...
    # Then, choice == 3 is the first item displayed, so add choice - 3 to that.
    world.player.attributes[type] = options[15 * curr_page + choice - 3]
    
def inventory_menu():
    while display.menu("Inventory", [[], ["consumable"], ["weapon"], ["hat"], ["shirt"], ["pants"], ["ring"]], ["Back", lambda: 0], ["-Set Consumable", set_active], ["-Set Weapon", set_active], ["-Set Hat", set_active], ["-Set Shirt", set_active], ["-Set Pants", set_active], ["-Set Ring", set_active]):
        # Redraw equip names.
        display.printc(46, 0, ' ' * 33)
        display.printc(46, 0, world.player.attributes["weapon"].name[:33])
        display.printc(43, 1, ' ' * 36)
        display.printc(43, 1, world.player.attributes["hat"].name[:36])
        display.printc(45, 2, ' ' * 34)
        display.printc(45, 2, world.player.attributes["shirt"].name[:34]) 
        display.printc(45, 3, ' ' * 34)
        display.printc(45, 3, world.player.attributes["pants"].name[:34])
        display.printc(44, 4, ' ' * 35)
        display.printc(44, 4, world.player.attributes["ring"].name[:35])
 
