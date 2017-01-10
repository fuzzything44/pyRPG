import time

import display
import world

from effects import effect

from items import item
from items import start as start_items

from objects.Player import attack
from objects import world_object

from spells import fireball
from spells import first_aid
from spells import frostshot
from spells import heal
from spells import lifesteal
from spells import spell

import pickle

import struct
import select


class player(world_object.world_object):
    def __init__(this, posX, posY, sock, addr):
        super().__init__(posX, posY, "player")
        this.attributes.update({    # Multiplayer info
            "socket" : sock,        # Socket to get data from
            "address" : addr,       # Where to send data
            "timeout" : 0,          # Time since last message, for timeouts
            "current_map" : 0,      # Increments on map change so we know when to stop sending map BG data
            "sidebar" : "",         # What the sidebar currently shows
            "current_menu" : None,  # What menu needs to be shown. If not none, displayed instead of sidebar

            "esc_menu" : None,      # For inventory management, will override current_menu
            "esc_menu_type" : "",   # Tracking what current esc_menu is doing. Main, inventory, ect...
            "set_name" : "",        # Tracking what to set (ex hat, spell...)
            "set_list" : [],        # List of what options correspond to when setting.

            "keys" : bytearray(15)  # What keys are down.
         })
        this.attributes.update({                \
              "maxHP" : 100.0,                  \
              "HP" : 100.0,                     \
              "maxMP" : 50,                     \
              "MP" : 50,                        \
              "money" : 0,                      \
              "effects" : {},                   \
              "EXP" : 0,                        \
              "level" : 1,                      \
              "items" : [start_items.start_hat(), start_items.start_pants(), start_items.start_ring(), start_items.start_shirt(), start_items.start_weapon(), spell.spell(heal.manaCost, heal.heal, heal.name, heal.icon)],\
              "class" : "warrior",              \
              "spell" : spell.spell(heal.manaCost, heal.heal, heal.name, heal.icon),            \
              "weapon" : item.item("No weapon", "weapon", 0, 1, {"damage" : 1, "range" : 1}),   \
              "hat" : item.item("No hat", "hat", 0),                \
              "shirt" : item.item("No shirt", "shirt", 0),          \
              "pants" : item.item("No pants", "pants", 0),          \
              "ring" : item.item("No ring", "ring", 0),             \
              "consumable" : item.item("Nothing", "consumable", 0, 1, {"icon" : "   \n   \n   ", "color" : 0, "use" : world_object.no_func}), \
              "mov_spd" : 0,                    # How quickly they move
              "atk_spd" : 0,                    # How quickly they attack
              "can_cast" : True,                \
              "can_item" : True,                \
              "magic" : 5,                      # How good spells are 
              "strength" : 5,                   # How much damage regular attacks do. 
              "luck" : 0,                       # Luck will change item and money drops
              "gainexp" : gain_exp,             \
              "lastHP" : 100.0,                 # What was their HP last frame?
              "sincehit" : 300,                 # How long since they were hit
              "respawnX" : posX,                \
              "respawnY" : posY,                \
              "respawnMap" : "start",           \
              "flags" : []                      # A very general list. For tracking progress through dungeons.
            })

    def update(this, delta_time):
        if select.select([this.attributes["socket"]], [], [], 0) != ([], [], []):
            try:
                (inpt, addr) = this.attributes["socket"].recvfrom(65507)
                this.attributes["keys"] = bytearray(inpt)
                while select.select([this.attributes["socket"]], [], [], 0) != ([], [], []):
                    this.attributes["socket"].recvfrom(65507)
                this.attributes["timeout"] = 0
            except ConnectionResetError as ex:
                print("Connection lost")
                this.attributes["socket"].close()
                world.to_del_plr.append(this)
                return
        else:
            this.attributes["timeout"] += delta_time
            if this.attributes["timeout"] > 1000:
                print("Timeout")
                this.attributes["socket"].close()
                world.to_del_plr.append(this)
                return


        if this.attributes["esc_menu"] is not None:
            opt = this.attributes["esc_menu"].update()

            if opt is not None: # They chose an option
                if this.attributes["esc_menu_type"] == "main":
                    if opt == 0:
                        this.attributes["esc_menu"] = None
                    elif opt == 1:
                        this.attributes["esc_menu"] = display.menu("Inventory\nMax HP: \\frRed\n\\fwMax MP: \\fbBlue\n\\fwMovement Speed: \\fgGreen\n\\fwAttack Speed: White\nMagic Power: \\fcCyan\n\\fwStrength: \\fmMagenta\n\\fwLuck: \\fyYellow\\fw", this, "Back", "Set Consumable", "Set Weapon", "Set Hat", "Set Shirt", "Set Pants", "Set Ring")
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "inv"
                    elif opt == 2:
                        options = [] # All options to go in the menu.
                        spell_list = [] # The spell corresponding to the option
                        for opt in this.attributes["items"]:    # Find all items
                            if opt.type == "spell":             # Do stuff if they're actually a spell
                                options.append(opt.name + "(" + str(opt.amount) + ")")
                                spell_list.append(opt)
                        this.attributes["esc_menu"] = display.menu("Set to what?", this, "Back", *options)
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "spell"
                        this.attributes["set_list"] = spell_list
                    elif opt == 3:
                        this.attributes["socket"].close()
                        world.to_del_plr.append(this)
                elif this.attributes["esc_menu_type"] == "inv": # Let them choose what item to set
                    if opt == 0:
                        this.attributes["esc_menu"] = display.menu("Options:", this, "Close Menu", "Inventory", "Spells", "Exit Server")
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "main"
                    else:
                        # What type of item they are setting
                        set_type = ["consumable", "weapon", "hat", "shirt", "pants", "ring"][opt - 1]
                        this.attributes["set_name"] = set_type
                        options = [] # All options to go in the menu.
                        items = [] # The item corresponding to the option
                        for opt in this.attributes["items"]:
                            if opt.type == set_type:
                                if set_type == "spell":
                                    options.append(opt.name + "(" + str(opt.amount) + ")")
                                else:
                                    options.append(opt.name +"(" + str(opt.amount) + ")" + opt.attributes["disp_data"])
                                items.append(opt)
                        this.attributes["esc_menu"] = display.menu("Set to what?", this, "Back", *options)
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "set"
                        this.attributes["set_list"] = items
                elif this.attributes["esc_menu_type"] == "set": # Let them set an item
                    if opt != 0:
                        itm = this.attributes["set_list"][opt - 1]                  # Find chosen item
                        this.attributes[this.attributes["set_name"]].unequip(this)  # Unequip other item
                        this.attributes[this.attributes["set_name"]] = itm          # Put in equipped slot
                        itm.equip(this)                                             # Equip
                    this.attributes["esc_menu"] = display.menu("Inventory\nMax HP: \\frRed\n\\fwMax MP: \\fbBlue\n\\fwMovement Speed: \\fgGreen\n\\fwAttack Speed: White\nMagic Power: \\fcCyan\n\\fwStrength: \\fmMagenta\n\\fwLuck: \\fyYellow\\fw", this, "Back", "Set Consumable", "Set Weapon", "Set Hat", "Set Shirt", "Set Pants", "Set Ring")
                    this.attributes["esc_menu"].is_esc_menu = True
                    this.attributes["esc_menu_type"] = "inv"

                elif this.attributes["esc_menu_type"] == "spell": # Let them set a spell
                    if opt != 0:
                        this.attributes["spell"] = this.attributes["set_list"][opt - 1]
                    this.attributes["esc_menu"] = display.menu("Options:", this, "Close Menu", "Inventory", "Spells", "Exit Server")
                    this.attributes["esc_menu"].is_esc_menu = True
                    this.attributes["esc_menu_type"] = "main"

        # Open ESC menu if needed.
        if this.attributes["keys"][display.KEY_ESC] and this.attributes["esc_menu"] is None:
            this.attributes["esc_menu"] = display.menu("Options:", this, "Close Menu", "Inventory", "Spells", "Exit Server")
            this.attributes["esc_menu"].is_esc_menu = True
            this.attributes["esc_menu_type"] = "main"

        # Check HP diff for flash on hit stuff
        if this.attributes["HP"] < this.attributes["lastHP"]:
            this.attributes["sincehit"] = 0
        else:
            this.attributes["sincehit"] += delta_time
    
        # Check for movement
        if this.attributes["keys"][display.KEY_W] and (not "del_up" in this.attributes["effects"]):
            if (this.Y > 0) and world.map[this.X][this.Y - 1][3]:
                this.Y -= 1
            this.attributes["effects"]["del_up"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if this.attributes["keys"][display.KEY_S] and (not "del_down" in this.attributes["effects"]):
            if (this.Y < world.WORLD_Y - 1) and world.map[this.X][this.Y + 1][3]:
                this.Y += 1
            this.attributes["effects"]["del_down"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if this.attributes["keys"][display.KEY_A] and (not "del_left" in this.attributes["effects"]):
            if (this.X > 0) and world.map[this.X - 1][this.Y][3]:
                this.X -= 1
            this.attributes["effects"]["del_left"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if this.attributes["keys"][display.KEY_D] and (not "del_right" in this.attributes["effects"]):
            if (this.X < world.WORLD_X - 1) and world.map[this.X + 1][this.Y][3]:
                this.X += 1
            this.attributes["effects"]["del_right"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))

        # Check for spell cast
        if this.attributes["keys"][display.KEY_SPACE] and this.attributes["can_cast"]:
            this.attributes["spell"].cast(this)
            this.attributes["can_cast"] = False
        if not this.attributes["keys"][display.KEY_SPACE]:
            this.attributes["can_cast"] = True

        # Attacks!
        if this.attributes["keys"][display.KEY_I] and (this.Y != 0) and (world.map[this.X][this.Y - 1][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y - 1, 0, -1, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
    
        if this.attributes["keys"][display.KEY_J] and (this.X != 0) and (world.map[this.X - 1][this.Y][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X - 1, this.Y, -1, 0, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
    
        if this.attributes["keys"][display.KEY_K] and (this.Y != 19) and (world.map[this.X][this.Y + 1][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y + 1, 0, 1, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
    
        if this.attributes["keys"][display.KEY_L] and (this.X != 49) and (world.map[this.X + 1][this.Y][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X + 1, this.Y, 1, 0, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
            # Or with our constants in python, time = 500/(1+2.718^(.01x)), which is a nice logistic formula.
    
        # Check for item use
        if this.attributes["keys"][display.KEY_SHIFT] and this.attributes["can_item"] and (this.attributes["consumable"].name != "Nothing"):
            this.attributes["consumable"].use(this)
            this.attributes["can_item"] = False
            this.attributes["consumable"].amount -= 1
            if this.attributes["consumable"].amount == 0:
                del this.attributes["items"][this.attributes["items"].index(this.attributes["consumable"])]
                this.attributes["consumable"] = item.item("Nothing", "consumable", 0, 1, {"icon" : "   \n   \n   ", "color" : 0})
        if not this.attributes["keys"][display.KEY_SHIFT]:
            this.attributes["can_item"] = True
    
        # Update all effects.
        this.attributes["sidebar"] += "Effects:\n"
        sidebar_len = this.attributes["sidebar"].count('\n')

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

        if this.attributes["sidebar"].count('\n') == sidebar_len:
            this.attributes["sidebar"] += " No effects\n"

        if this.attributes["HP"] <= 0: # Dead
            this.attributes["HP"] = this.attributes["maxHP"]                    # Recover HP
            this.X = this.attributes["respawnX"]                                # Return to last saved place
            this.Y = this.attributes["respawnY"]
            world.move_requests.append((this.attributes["respawnMap"], this))   # At last saved map...
            world.to_del_plr.append(this)                                       # Exit from this map.

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
    
    def map_data(this):
        if this.attributes["keys"][display.KEY_MAPID] != this.attributes["current_map"]:
            # Send map data to player
            data = bytearray(2)
            data[0] = 1
            data[1] = this.attributes["current_map"]
            map_data = pickle.dumps(world.map)
            data += struct.pack("!I", len(map_data))
            data += map_data
            return data
        else:
            return bytearray(1)


    # All extra data to be sent. So HP/MP, equip stuff, sidebar stuff.
    def extra_data(this):
        hp = struct.pack("!I", int(this.attributes["HP"])) + struct.pack("!I", int(this.attributes["maxHP"]))
        mp = struct.pack("!I", int(this.attributes["MP"])) + struct.pack("!I", int(this.attributes["maxMP"]))
        level = struct.pack("!I", this.attributes["level"])
        exp = struct.pack("!I", int(0.5*this.attributes["level"]**2 + 0.5*this.attributes["level"] + 4 - this.attributes["EXP"]))
        gold = struct.pack("I", this.attributes["money"])
        spell_len = struct.pack("!I", len(this.attributes["spell"].image))
        spell_image = bytearray(this.attributes["spell"].image, 'utf-8')

        item_len = struct.pack("!I", len(this.attributes["consumable"].attributes["icon"]))
        item_image = bytearray(this.attributes["consumable"].attributes["icon"], 'utf-8')

        equip_info = bytes()
        for type in ["weapon", "hat", "shirt", "pants", "ring"]:
            type_len    = struct.pack("!I", len(this.attributes[type].name))
            type_info   = bytearray(this.attributes[type].name, 'utf-8')
            equip_info += type_len + type_info


        # So we need an int for length and then all the data.
        sidebar_data = None
        if this.attributes["esc_menu"] is not None:
            sidebar_data = bytearray(this.attributes["esc_menu"].disp(), 'utf-8')
        elif this.attributes["current_menu"] is None:
            sidebar_data = bytearray(this.attributes["sidebar"], 'utf-8')
        else:
            sidebar_data = bytearray(this.attributes["current_menu"].disp(), 'utf-8')
        sidebar_len  = struct.pack("!I", len(sidebar_data))
        # Sidebar stuff is sent, so now we zero it out.
        this.attributes["sidebar"] = ""
        
        
        return hp + mp + level + exp + gold + spell_len + spell_image + item_len + item_image + equip_info + sidebar_len + sidebar_data

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
