import time

import display
import world

from items import item

from objects import attack
from objects import world_object

from spells import fireball
from spells import first_aid
from spells import frostshot
from spells import spell

from items import bread
def player_update(this, delta_time):
    display.printc(8, 0, str(int(this.attributes["HP"])) + "/" + str(int(this.attributes["maxHP"])) + "  ")
    display.printc(8, 1, str(int(this.attributes["MP"])) + "/" + str(int(this.attributes["maxMP"])) + "  ")
    display.printc(10, 2, str(this.attributes["money"]) + "     ")
    display.printc(12, 3, str(this.attributes["level"]))
    display.printc(5, 4, str(this.attributes["level"] ** 2 - this.attributes["EXP"]) + " to level        ")
    try:
        if display.keyDown(ord('W')) and (not "del_up" in this.attributes["effects"]):
            if world.map[this.X][this.Y - 1][2]:
                this.Y -= 1
            if this.Y < 0:
                this.Y = 0
            this.attributes["effects"]["del_up"] = [world_object.no_func, world_object.no_func, this.attributes["mov_spd"]]
        if display.keyDown(ord('S')) and (not "del_down" in this.attributes["effects"]):
            if world.map[this.X][this.Y + 1][2]:
                this.Y += 1
            if this.Y > 22:
                this.Y = 22
            this.attributes["effects"]["del_down"] = [world_object.no_func, world_object.no_func, this.attributes["mov_spd"]]
        if display.keyDown(ord('A')) and (not "del_left" in this.attributes["effects"]):
            if world.map[this.X - 1][this.Y][2]:
                this.X -= 1
            if this.X < 0:
                this.X = 0
            this.attributes["effects"]["del_left"] = [world_object.no_func, world_object.no_func, this.attributes["mov_spd"]]
        if display.keyDown(ord('D')) and (not "del_right" in this.attributes["effects"]):
            if world.map[this.X + 1][this.Y][2]:
                this.X += 1
            if this.X > 77:
                this.X = 77
            this.attributes["effects"]["del_right"] = [world_object.no_func, world_object.no_func, this.attributes["mov_spd"]]
        if display.keyDown(ord(' ')) and this.attributes["can_cast"]:
            this.attributes["spell"].cast(this)
            this.attributes["can_cast"] = False
        if not display.keyDown(ord(' ')):
            this.attributes["can_cast"] = True
        # Attacks!
        if (display.keyDown(ord('I'))) and (this.Y != 0) and (world.map[this.X][this.Y - 1][2]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, this.X, this.Y - 1, \
                {"movex" : 0, "movey": -1, "range" : this.attributes["weapon"].attributes["range"], "damage" : (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
            this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, this.attributes["atk_spd"]]
        if (display.keyDown(ord('J'))) and (this.X != 0) and (world.map[this.X - 1][this.Y][2]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, this.X - 1, this.Y, \
                {"movex" : -1, "movey": 0, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["strength"]*this.attributes["weapon"].attributes["damage"]//2, "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
            this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, this.attributes["atk_spd"]]
        if (display.keyDown(ord('K'))) and (this.Y != 19) and (world.map[this.X][this.Y + 1][2]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, this.X, this.Y + 1, \
                {"movex" : 0, "movey": 1, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["strength"]*this.attributes["weapon"].attributes["damage"]//2, "speed" : 100, "to_move" : 0, "owner" : this}\
            ))                                                                                                                                                                  
            this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, this.attributes["atk_spd"]]
        if (display.keyDown(ord('L'))) and (this.X != 49) and (world.map[this.X + 1][this.Y][2]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, this.X + 1, this.Y, \
                {"movex" : 1, "movey": 0, "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["strength"]*this.attributes["weapon"].attributes["damage"]//2, "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
            this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, this.attributes["atk_spd"]]

        if display.keyDown(display.CONST.VK_LSHIFT) and this.attributes["can_item"]:
            this.attributes["consumable"].attributes["use"](this)
            this.attributes["can_item"] = False
            this.attributes["consumable"].amount -= 1
            if this.attributes["consumable"].amount == 0:
                this.attributes["consumable"] = item.item("Nothing", "consumable", world_object.no_func, world_object.no_func, 1, {"icon" : ["   ", "   ", "   "], "color" : 0, "use" : world_object.no_func})
                this.attributes["consumable"].draw()
        if not display.keyDown(display.CONST.VK_SHIFT):
            this.attributes["can_item"] = True

    except Exception as ex:
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
        display.refresh()
        time.sleep(1)
        display.flushinp()
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

player_type = "player"

def gain_exp(this, amount):
    this.attributes["EXP"] += amount
    while this.attributes["EXP"] >= this.attributes["level"]**2: # They levelled up!
        this.attributes["EXP"] -= this.attributes["level"]**2 # Remove EXP required for level
        this.attributes["level"] += 1 # Duh.
        if this.attributes["level"] == 2:
            if this.attributes["class"] == "mage":
                try:
                    this.attributes["items"].append(spell.spell(fireball.manaCost, fireball.fireball, fireball.name, fireball.icon, fireball.color))
                except Exception as ex:
                    pass
            if this.attributes["class"] == "warrior":
                try:
                    this.attributes["items"].append(spell.spell(first_aid.manaCost, first_aid.FirstAid, first_aid.name, first_aid.icon, first_aid.color))
                except:
                    pass
            if this.attributes["class"] == "thief":
                pass
        if this.attributes["level"] == 4:
            if this.attributes["class"] == "mage":
                this.attributes["items"].append(spell.spell(frostshot.manaCost, frostshot.frostshot, frostshot.name, frostshot.icon, frostshot.color))
        if this.attributes["class"] == "warrior":
            this.attributes["maxHP"] += 15 # Give stats. TODO: Give them based on class
            this.attributes["maxMP"] += 5
            this.attributes["mov_spd"] -= 1
            this.attributes["atk_spd"] -= 2
            this.attributes["magic"] += 1
            this.attributes["strength"] += 4
        if this.attributes["class"] == "mage":
            this.attributes["maxHP"] += 5 # Give stats. TODO: Give them based on class
            this.attributes["maxMP"] += 10
            this.attributes["mov_spd"] -= 2
            this.attributes["atk_spd"] -= 2
            this.attributes["magic"] += 4
            this.attributes["strength"] += 2
        if this.attributes["class"] == "thief":
            this.attributes["maxHP"] += 10  # Give stats. TODO: Give them based on class
            this.attributes["maxMP"] += 10
            this.attributes["mov_spd"] -= 4
            this.attributes["atk_spd"] -= 3
            this.attributes["magic"] += 2
            this.attributes["strength"] += 3

        this.attributes["HP"] = this.attributes["maxHP"] # HP restore on level
        this.attributes["MP"] = this.attributes["maxMP"] # MP restore on level
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
      "class" : "newb",                 \
      "spell" : spell.spell(0, world_object.no_func, ["   ", "   ", "   "], display.WHITE), \
      "weapon" : item.item("", "weapon", world_object.no_func, world_object.no_func),       \
      "hat" : item.item("", "hat", world_object.no_func, world_object.no_func),             \
      "shirt" : item.item("", "shirt", world_object.no_func, world_object.no_func),         \
      "pants" : item.item("", "pants", world_object.no_func, world_object.no_func),         \
      "ring" : item.item("", "ring", world_object.no_func, world_object.no_func),           \
      "consumable" : item.item("", "consumable", world_object.no_func, world_object.no_func, {"icon" : ["   ", "   ", "   "], "color" : 0, "use" : world_object.no_func}), \
      "mov_spd" : 200,                    \
      "atk_spd" : 500,                   \
      "can_cast" : True,                 \
      "can_item" : True,                 \
      "magic" : 5,                       \
      "strength" : 5,                    \
      "gainexp" : gain_exp               \
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
    while (choice == 1) or (choice == 2):
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
    if type != "spell": # Spells don't have equip and unequip functions.
        world.player.attributes[type].unequip(world.player.attributes[type], world.player) # Unequip the old item.
        world.player.attributes[type] = options[15 * curr_page + choice - 3]
        world.player.attributes[type].equip(world.player.attributes[type], world.player) # Equip new item
    else:
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
 
