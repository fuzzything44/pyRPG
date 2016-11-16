import time

import display
import world

from effects import effect

from items import item

from objects.Player import attack
from objects import world_object

from spells import fireball
from spells import first_aid
from spells import frostshot
from spells import lifesteal
from spells import spell

class player(world_object.world_object):
    def __init__(this, posX, posY):
        super().__init__(posX, posY, "player")
        # effects is a dictionary of (string) effect name to [(func) tick(player, delta_time), (func) on_remove(player), time_left]
        # items is a list of ITEMs or to SPELLs
        this.attributes.update({                \
              "maxHP" : 100.0,                  \
              "HP" : 100.0,                     \
              "maxMP" : 50,                     \
              "MP" : 50,                        \
              "money" : 0,                      \
              "effects" : {},                   \
              "EXP" : 0,                        \
              "level" : 1,                      \
              "items" : [],                     \
              "class" : "warrior",              \
              "spell" : spell.spell(0, world_object.no_func, ["   ", "   ", "   "], display.WHITE), \
              "weapon" : item.item("", "weapon", 0, 1, {"damage" : 1, "range" : 1}),                \
              "hat" : item.item("", "hat", 0),                                                      \
              "shirt" : item.item("", "shirt", 0),         \
              "pants" : item.item("", "pants", 0),         \
              "ring" : item.item("", "ring", 0),           \
              "consumable" : item.item("Nothing", "consumable", 0, 1, {"icon" : ["   ", "   ", "   "], "color" : 0, "use" : world_object.no_func}), \
              "mov_spd" : 0,                    # How quickly they move
              "atk_spd" : 0,                    # How quickly they attack
              "can_cast" : True,                 \
              "can_item" : True,                 \
              "magic" : 5,                      # How good spells are 
              "strength" : 5,                   # How much damage regular attacks do. 
              "luck" : 0,                       # Luck will change item and money drops
              "gainexp" : gain_exp,              \
              "lastHP" : 100.0,                 # What was their HP last frame?
              "sincehit" : 300,                 # How long since they were hit
              "flags" : []                      # A very general list. For tracking progress through dungeons.
            })

    def update(this, delta_time):
        # Reprint top bar status
        display.printc(8, 0, str(int(this.attributes["HP"])) + "/" + str(int(this.attributes["maxHP"])) + "  ")
        display.printc(8, 1, str(int(this.attributes["MP"])) + "/" + str(int(this.attributes["maxMP"])) + "  ")
        display.printc(10, 2, str(this.attributes["money"]) + "     ")
        display.printc(12, 3, str(this.attributes["level"]))
        display.printc(5, 4, str(int(0.5*this.attributes["level"]**2 + 0.5*this.attributes["level"] + 4 - this.attributes["EXP"])) + " to level        ")
        # Check HP diff for flash on hit stuff
        if this.attributes["HP"] < this.attributes["lastHP"]:
            this.attributes["sincehit"] = 0
        else:
            this.attributes["sincehit"] += delta_time
    
        # Check for movement
        if display.keyDown(ord('W')) and (not "del_up" in this.attributes["effects"]):
            if (this.Y > 0) and world.map[this.X][this.Y - 1][3]:
                this.Y -= 1
            this.attributes["effects"]["del_up"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if display.keyDown(ord('S')) and (not "del_down" in this.attributes["effects"]):
            if (this.Y < world.WORLD_Y - 1) and world.map[this.X][this.Y + 1][3]:
                this.Y += 1
            this.attributes["effects"]["del_down"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if display.keyDown(ord('A')) and (not "del_left" in this.attributes["effects"]):
            if (this.X > 0) and world.map[this.X - 1][this.Y][3]:
                this.X -= 1
            this.attributes["effects"]["del_left"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if display.keyDown(ord('D')) and (not "del_right" in this.attributes["effects"]):
            if (this.X < world.WORLD_X - 1) and world.map[this.X + 1][this.Y][3]:
                this.X += 1
            this.attributes["effects"]["del_right"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))

        # Check for spell cast
        if display.keyDown(ord(' ')) and this.attributes["can_cast"]:
            this.attributes["spell"].cast(this)
            this.attributes["can_cast"] = False
        if not display.keyDown(ord(' ')):
            this.attributes["can_cast"] = True

        # Attacks!
        if (display.keyDown(ord('I'))) and (this.Y != 0) and (world.map[this.X][this.Y - 1][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y - 1, 0, -1, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
    
        if (display.keyDown(ord('J'))) and (this.X != 0) and (world.map[this.X - 1][this.Y][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X - 1, this.Y, -1, 0, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
    
        if (display.keyDown(ord('K'))) and (this.Y != 19) and (world.map[this.X][this.Y + 1][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y + 1, 0, 1, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
    
        if (display.keyDown(ord('L'))) and (this.X != 49) and (world.map[this.X + 1][this.Y][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X + 1, this.Y, 1, 0, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
            # Or with our constants in python, time = 500/(1+2.718^(.01x)), which is a nice logistic formula.
    
        # Check for item use
        if display.keyDown(display.CONST.VK_LSHIFT) and this.attributes["can_item"] and (this.attributes["consumable"].name != "Nothing"):
            this.attributes["consumable"].use(this)
            this.attributes["can_item"] = False
            this.attributes["consumable"].amount -= 1
            if this.attributes["consumable"].amount == 0:
                del this.attributes["items"][this.attributes["items"].index(this.attributes["consumable"])]
                this.attributes["consumable"] = item.item("Nothing", "consumable", 0, 1, {"icon" : ["   ", "   ", "   "], "color" : 0})
                this.attributes["consumable"].draw()
        if not display.keyDown(display.CONST.VK_SHIFT):
            this.attributes["can_item"] = True
    
        # Update all effects.
        eff_del_list = []
        for eff_name in this.attributes["effects"]:
            eff = this.attributes["effects"][eff_name]
            eff.tick(delta_time)  # Tick effect
            if eff.time <= 0:           # Remove effect
                eff_del_list.append(eff_name)
        for eff_name in eff_del_list:
            this.attributes["effects"][eff_name].uneffect(this)
            del this.attributes["effects"][eff_name]
        del eff_del_list
        if this.attributes["HP"] <= 0: #TODO: Actually have things happen when you die.
            display.printc(33, 9,  "+++++++++++++", display.RED)
            display.printc(33, 10, "+ You DIED! +", display.RED)
            display.printc(33, 11, "+++++++++++++", display.RED)
            display.refresh()
            time.sleep(1)
            display.flushinp()
            while display.getch() != -1: # Wait for key release
                pass
            while display.getch() == -1: # Wait for keypress
                pass
    
            display.end()

        # Finally, update lastHP. Done after effects because we don't want effects to make you constantly red
        this.attributes["lastHP"] = this.attributes["HP"]
    
    def char(this):
        return 'P'
    
    def color(this):
        if this.attributes["sincehit"] < 75:
            return display.RED
        elif this.attributes["sincehit"] < 150:
            return display.WHITE
        elif this.attributes["sincehit"] < 225:
            return display.RED
        return display.WHITE
    
def gain_exp(this, amount):
    this.attributes["EXP"] += amount
    # Takes 0.5L^2 + .5L + 4
    while this.attributes["EXP"] >= (0.5*this.attributes["level"]**2 + 0.5*this.attributes["level"] + 4): # They levelled up!
        this.attributes["EXP"] -= (0.5*this.attributes["level"]**2 + 0.5*this.attributes["level"] + 4) # Remove EXP required for level
        this.attributes["level"] += 1 # Duh.
        if this.attributes["level"] == 2:
            if this.attributes["class"] == "mage":
                this.attributes["items"].append(spell.spell(fireball.manaCost, fireball.fireball, fireball.name, fireball.icon, fireball.color))
            if this.attributes["class"] == "warrior":
                this.attributes["items"].append(spell.spell(first_aid.manaCost, first_aid.FirstAid, first_aid.name, first_aid.icon, first_aid.color))
            if this.attributes["class"] == "thief":
                this.attributes["items"].append(spell.spell(lifesteal.manaCost, lifesteal.lifesteal, lifesteal.name, lifesteal.icon, lifesteal.color))
        if this.attributes["level"] == 4:
            if this.attributes["class"] == "mage":
                this.attributes["items"].append(spell.spell(frostshot.manaCost, frostshot.frostshot, frostshot.name, frostshot.icon, frostshot.color))
        if this.attributes["class"] == "warrior":
            this.attributes["maxHP"] += 15 # Give stats.
            this.attributes["maxMP"] += 5
            this.attributes["mov_spd"] += 1
            this.attributes["atk_spd"] += 1
            this.attributes["magic"] += 1
            this.attributes["strength"] += 3
        if this.attributes["class"] == "mage":
            this.attributes["maxHP"] += 5 # Give stats.
            this.attributes["maxMP"] += 15
            this.attributes["mov_spd"] += 3
            this.attributes["atk_spd"] += 3
            this.attributes["magic"] += 3
            this.attributes["strength"] += 1
        if this.attributes["class"] == "thief":
            this.attributes["maxHP"] += 10  # Give stats.
            this.attributes["maxMP"] += 10
            this.attributes["mov_spd"] += 5
            this.attributes["atk_spd"] += 5
            this.attributes["magic"] += 2
            this.attributes["strength"] += 2

        this.attributes["HP"] = this.attributes["maxHP"] # HP restore on level
        this.attributes["MP"] = this.attributes["maxMP"] # MP restore on level

def set_active(type):
    options = [] # All options to go in the menu.
    items = [] # The item corresponding to the option
    for opt in world.player.attributes["items"]:
        if opt.type == type:
            if opt.type == "spell":
                options.append(opt.name + "(" + str(opt.amount) + ")")
            else:
                options.append(opt.name +"(" + str(opt.amount) + ")" + opt.attributes["disp_data"])
            items.append(opt)

    empty_lists = [[] for x in range(len(options) + 1)]
    menu = display.menu("Set to what?", "Back", *options)
    while menu.update() is None:
        display.refresh()

    if menu.update() == 0: # They chose back
        return

    if type != "spell": # Spells don't have equip and unequip functions.
        world.player.attributes[type].unequip(world.player) # Unequip the old item.
        world.player.attributes[type] = items[menu.update() - 1] # Find the new item
        world.player.attributes[type].equip(world.player) # Equip new item
    else:
        world.player.attributes[type] = items[menu.update() - 1]

    
def inventory_menu():
    while True:
        menu = display.menu("Inventory\nMax HP: \\frRed\n\\fwMax MP: \\fbBlue\n\\fwMovement Speed: \\fgGreen\n\\fwAttack Speed: White\nMagic Power: \\fcCyan\n\\fwStrength: \\fmMagenta\n\\fwLuck: \\fyYellow", "Back", "Set Consumable", "Set Weapon", "Set Hat", "Set Shirt", "Set Pants", "Set Ring")
        while menu.update() is None:
            display.refresh()
        if menu.update() != 0:
            set_active([0, "consumable", "weapon", "hat", "shirt", "pants", "ring"][menu.update()])
        # Redraw equip names.
        display.printc(display.WEAPON_X, display.WEAPON_Y, ' ' * 33)
        display.printc(display.WEAPON_X, display.WEAPON_Y, world.player.attributes["weapon"].name[:33])
        display.printc(display.HAT_X, display.HAT_Y, ' ' * 36)
        display.printc(display.HAT_X, display.HAT_Y, world.player.attributes["hat"].name[:36])
        display.printc(display.SHIRT_X, display.SHIRT_Y, ' ' * 34)
        display.printc(display.SHIRT_X, display.SHIRT_Y, world.player.attributes["shirt"].name[:34]) 
        display.printc(display.PANTS_X, display.PANTS_Y, ' ' * 34)
        display.printc(display.PANTS_X, display.PANTS_Y, world.player.attributes["pants"].name[:34])
        display.printc(display.RING_X, display.RING_Y, ' ' * 35)
        display.printc(display.RING_X, display.RING_Y, world.player.attributes["ring"].name[:35])
        if menu.update() == 0:
            return
 
