import time
import sys

import attack
import display
import item
import world
import world_object

def player_update(this, input, delta_time):
    display.printc(8, 0, str(int(this.attributes["HP"])) + "/" + str(int(this.attributes["maxHP"])) + "  ")
    display.printc(8, 1, str(int(this.attributes["MP"])) + "/" + str(int(this.attributes["maxMP"])) + "  ")
    display.printc(10, 2, str(this.attributes["money"]) + "     ")
    display.printc(12, 3, str(this.attributes["level"]))
    display.printc(5, 4, str(this.attributes["level"] ** 2 - this.attributes["EXP"]) + " to level        ")
    try:
        if input == ord('w'):
            if world.map[this.X][this.Y - 1][2]:
                this.Y -= 1
            if this.Y < 0:
                this.Y = 0
        if input == ord('s'):
            if world.map[this.X][this.Y + 1][2]:
                this.Y += 1
            if this.Y > 22:
                this.Y = 22
        if input == ord('a'):
            if world.map[this.X - 1][this.Y][2]:
                this.X -= 1
            if this.X < 0:
                this.X = 0
        if input == ord('d'):
            if world.map[this.X + 1][this.Y][2]:
                this.X += 1
            if this.X > 77:
                this.X = 77
        if input == ord(' '):
            this.attributes["currspell"][0](this)
        # Attacks!
        if (input == ord('i')) & (this.Y != 0) & (world.map[this.X][this.Y - 1][2]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, this.X, this.Y - 1, \
                {"movex" : 0, "movey": -1, "type" : "damage", "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["weapon"].attributes["damage"], "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
        if (input == ord('j')) & (this.X != 0) & (world.map[this.X - 1][this.Y][2]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, this.X - 1, this.Y, \
                {"movex" : -1, "movey": 0, "type" : "damage", "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["weapon"].attributes["damage"], "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
        if (input == ord('k')) & (this.Y != 19) & (world.map[this.X][this.Y + 1][2]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, this.X, this.Y + 1, \
                {"movex" : 0, "movey": 1, "type" : "damage", "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["weapon"].attributes["damage"], "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
        if (input == ord('l')) & (this.X != 49) & (world.map[this.X + 1][this.Y][2]):
            world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, this.X + 1, this.Y, \
                {"movex" : 1, "movey": 0, "type" : "damage", "range" : this.attributes["weapon"].attributes["range"], "damage" : this.attributes["weapon"].attributes["damage"], "speed" : 100, "to_move" : 0, "owner" : this}\
            ))
        if input == ord(';'):
            pass # Use item

    except:
        pass
    
    eff_del_list = []
    # Update all effects.
    for eff in this.attributes["effects"]:
        this.attributes["effects"][eff][0](this, delta_time)       # Tick code
        this.attributes["effects"][eff][1] -= delta_time           # Lower time
        if this.attributes["effects"][eff][1] <= 0:                # Remove effect
            eff_del_list.append(eff)
    for to_del in eff_del_list:
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
    if oth.attributes["type"] == "money":
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
    if this.attributes["money"] > 50:
        return display.YELLOW
    return display.WHITE

def heal(player):
    if player.attributes["MP"] >= 10:
        player.attributes["MP"] -= 10
        player.attributes["HP"] += 25
    if player.attributes["HP"] > player.attributes["maxHP"]:
        player.attributes["HP"] = player.attributes["maxHP"]

# effects is a dictionary of (string) effect name to [(func) tick(player, delta_time), time_left]
# items is a dictionary of (string) item name to ITEM
# spells is a dictionary of (string) eff name to ( (func) use(player), (string) row 1 symbols, (string) row 2 symbols, (string) row 3 symbols)
player_attributes =                     \
    { "type" : "player",                \
      "maxHP" : 100.0,                  \
      "HP" : 100.0,                     \
      "maxMP" : 50,                     \
      "MP" : 50,                        \
      "money" : 0,                      \
      "effects" : {},                   \
      "EXP" : 0,                        \
      "level" : 1,                      \
      "items" : [],                     \
      "spells" : {"heal" : (heal, "\\|/", "-+-", "/|\\")},\
      "currspell" : (heal, " | ", "-+-", " | "), \
      "weapon" : item.item("Broken Sword"),      \
      "hat" : item.item("Cloth Hat"),            \
      "shirt" : item.item("Cloth Shirt"),        \
      "pants" : item.item("Cloth Pants"),        \
      "shoes" : item.item("Tennis Shoes"),       \
      "ring" : item.item("Useless ring"),        \
      "consumable" : item.item("Nothing")        \
    }

def set_active(type):
    options = [] # All options to go in the menu.
    pass # Effectively needs to give a menu of all items of that type (so probably multiple pages) and once one is chosen set it as the active.

def inventory_menu():
    while display.menu("Inventory", [[], ["consumable"], ["weapon"], ["hat"], ["shirt"], ["pants"], ["shoes"], ["ring"]], ["Back", lambda: 0], ["-Set Consumable", set_active], ["-Set Weapon", set_active], ["-Set Hat", set_active], ["-Set Shirt", set_active], ["-Set Pants", set_active], ["-Set Shoes", set_active], ["-Set Ring", set_active]):
        pass

def spell_menu():
    pass