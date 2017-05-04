import array
import copy
import json
import time

import display
import world

from effects import effect

from items import item
from items import no_item
from items import start as start_items

from objects.Player import attack
from objects import world_object

import spells

import struct
import select


class player(world_object.world_object):
    def __init__(this, posX, posY, pipe, name):
        super().__init__(posX, posY, "player", world_object.TEAM_PLAYER)
        this.blocks_map_exit = True
        this.attributes.update({    # Multiplayer info
            "pipe" : pipe,          # Pipe to get and send data to the websocket
            "name" : name,          # Name they set

            "timeout" : 0,          # Time since last message, for timeouts
            "current_map" : 0,      # Increments on map change so we know when to stop sending map BG data
            "sidebar" : "",         # What the sidebar currently shows
            "current_menu" : None,  # What menu needs to be shown. If not none, displayed instead of sidebar

            "esc_menu" : None,      # For inventory management, will override current_menu
            "esc_menu_type" : "",   # Tracking what current esc_menu is doing. Main, inventory, ect...
            "set_name" : "",        # Tracking what to set (ex hat, spell...)
            "set_list" : [],        # List of what options correspond to when setting.

            "keys" : bytearray(display.NUM_KEYS), # What keys are down.
            "can_spell_cycle" : True, # Can we change the current spell? (So last update UO weren't down)

            "using_inv" : False,    # Are they using their inventory now? If so we send different stuff.
            "inv_data" : bytearray(0), # Inventory data to send
            "maxHP" : 100.0,
            "HP" : 100.0,
            "maxMP" : 50,
            "MP" : 50,
            "money" : 0,
            "effects" : {},
            "EXP" : 0,
            "level" : 1,
            "items" : [start_items.start_hat(), start_items.start_pants(), start_items.start_ring(), start_items.start_shirt(), start_items.start_weapon()],
            "spells" : [spells.spell.spell(spells.heal.manaCost, spells.heal.heal, spells.heal.name, spells.heal.icon)],
            "class" : "warrior",
            "spell" : 0,                      # Index of spells for current spell
            "weapon" : no_item.no_weapon(),
            "hat"    : no_item.no_hat(),
            "shirt"  : no_item.no_shirt(),
            "pants"  : no_item.no_pants(),
            "ring"   : no_item.no_ring(),
            "consumable" : no_item.no_consumable(),
            "mov_spd" : 0,                    # How quickly they move
            "atk_spd" : 0,                    # How quickly they attack
            "can_cast" : True,
            "can_item" : True,
            "magic" : 5,                      # How good spells are
            "strength" : 5,                   # How much damage regular attacks do.
            "luck" : 0,                       # Luck will change item and money drops
            "gainexp" : gain_exp,
            "lastHP" : 100.0,                 # What was their HP last frame?
            "sincehit" : 300,                 # How long since they were hit
            "respawnX" : posX,
            "respawnY" : posY,
            "respawnMap" : "start",
            "flags" : array.array('b')        # A very general list. For tracking progress through dungeons.
            })

    def update(this, delta_time):
        if this.attributes["pipe"].poll():
            message = json.loads(this.attributes["pipe"].recv())
            if message["type"] == 'keydown':
                pass # TODO: Find what key went down, set it.
            elif message["type"]== 'keyup':
                pass # TODO: Find what key went up, set it.
            elif inpt[0] == 1:
                pass # Inventory stuff... TODO: Actually add checking if there's stuff here.
            this.attributes["timeout"] = 0
        else:
            this.attributes["timeout"] += delta_time
            print(this.attributes["timeout"])
            if this.attributes["timeout"] > 1000:
                print("Timeout")
                world.to_del_plr.append(this)
                return
        if this.attributes["esc_menu"] is not None:
            opt = this.attributes["esc_menu"].update()

            if opt is not None: # They chose an option
                if this.attributes["esc_menu_type"] == "main":
                    if opt == 0:
                        this.attributes["esc_menu"] = None
                    elif opt == 1:
                        # TODO: remove this once full screen inventory works
                        this.attributes["esc_menu"] = display.menu("Inventory\nMax HP: \\frRed\n\\fwMax MP: \\fbBlue\n\\fwMovement Speed: \\fgGreen\n\\fwAttack Speed: White\nMagic Power: \\fcCyan\n\\fwStrength: \\fmMagenta\n\\fwLuck: \\fyYellow\\fw", this, "Back", "Set Consumable", "Set Weapon", "Set Hat", "Set Shirt", "Set Pants", "Set Ring")
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "inv"
                    elif opt == 2:
                        options = [] # All options to go in the menu.
                        spell_list = this.attributes["spells"] # The spell corresponding to the option
                        for spl in spell_list:    # Find all items
                            options.append(spl.name + "(" + str(spl.amount) + ")")
                        this.attributes["esc_menu"] = display.menu("Set to what?", this, "Back", *options)
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "spell"
                    elif opt == 3:
                        options = [] # All options to go in the menu.
                        spell_list = this.attributes["spells"] # The spell corresponding to the option
                        for spl in spell_list:    # Find all items
                            options.append(spl.name + "(" + str(spl.amount) + ")")
                        this.attributes["esc_menu"] = display.menu("Switch what spell?", this, "Back", *options)
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "sorder1"
                    elif opt == 4:
                        this.attributes["esc_menu"] = None
                        world.to_del_plr.append(this)
                        return
                elif this.attributes["esc_menu_type"] == "inv": # Let them choose what item to set
                    # TODO: remove once full screen inventory works
                    if opt == 0:
                        this.attributes["esc_menu"] = display.menu("Options:", this, "Close Menu", "Inventory", "Spells", "Switch Spell Order","Exit Server")
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "main"
                    else:
                        # What type of item they are setting
                        set_type = ["consumable", "weapon", "hat", "shirt", "pants", "ring"][opt - 1]
                        this.attributes["set_name"] = set_type
                        options = [] # All options to go in the menu.
                        items = [] # The item corresponding to the option
                        for itm in this.attributes["items"]:
                            if itm.type == set_type:
                                options.append(itm.name +"(" + str(itm.amount) + ")" + itm.attributes["disp_data"])
                                items.append(itm)
                        this.attributes["esc_menu"] = display.menu("Set to what?", this, "Back", *options)
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "set"
                        this.attributes["set_list"] = items
                elif this.attributes["esc_menu_type"] == "set": # Let them set an item
                    if opt != 0:
                        itm = this.attributes["set_list"][opt - 1]                  # Find chosen item
                        if itm in this.attributes["items"]:     # If they have the item
                            this.attributes[this.attributes["set_name"]].unequip(this)  # Unequip other item
                            this.attributes[this.attributes["set_name"]] = itm          # Put in equipped slot
                            itm.equip(this)                                             # Equip
                    this.attributes["esc_menu"] = display.menu("Inventory\nMax HP: \\frRed\n\\fwMax MP: \\fbBlue\n\\fwMovement Speed: \\fgGreen\n\\fwAttack Speed: White\nMagic Power: \\fcCyan\n\\fwStrength: \\fmMagenta\n\\fwLuck: \\fyYellow\\fw", this, "Back", "Set Consumable", "Set Weapon", "Set Hat", "Set Shirt", "Set Pants", "Set Ring")
                    this.attributes["esc_menu"].is_esc_menu = True
                    this.attributes["esc_menu_type"] = "inv"

                elif this.attributes["esc_menu_type"] == "spell": # Let them set a spell
                    if opt != 0:
                        this.attributes["spell"] = opt - 1
                    this.attributes["esc_menu"] = display.menu("Options:", this, "Close Menu", "Inventory", "Spells", "Switch Spell Order", "Exit Server")
                    this.attributes["esc_menu"].is_esc_menu = True
                    this.attributes["esc_menu_type"] = "main"

                elif this.attributes["esc_menu_type"] == "sorder1":
                    if opt != 0:
                        this.attributes["spell_switch"] = opt - 1 # First switch option.
                        options = [] # All options to go in the menu.
                        spell_list = this.attributes["spells"] # The spell corresponding to the option
                        for spl in spell_list:    # Find all items
                            options.append(spl.name + "(" + str(spl.amount) + ")")
                        this.attributes["esc_menu"] = display.menu("Switch with what?", this, *options)
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "sorder2"
                    else:
                        this.attributes["esc_menu"] = display.menu("Options:", this, "Close Menu", "Inventory", "Spells", "Switch Spell Order", "Exit Server")
                        this.attributes["esc_menu"].is_esc_menu = True
                        this.attributes["esc_menu_type"] = "main"
                elif this.attributes["esc_menu_type"] == "sorder2":
                    # Switch spells
                    this.attributes["spells"][this.attributes["spell_switch"]], this.attributes["spells"][opt] = this.attributes["spells"][opt], this.attributes["spells"][this.attributes["spell_switch"]]
                    this.attributes["esc_menu"] = display.menu("Options:", this, "Close Menu", "Inventory", "Spells", "Switch Spell Order", "Exit Server")
                    this.attributes["esc_menu"].is_esc_menu = True
                    this.attributes["esc_menu_type"] = "main"
        # Open ESC menu if needed.
        if this.attributes["keys"][display.KEY_ESC] and this.attributes["esc_menu"] is None:
            this.attributes["esc_menu"] = display.menu("Options:", this, "Close Menu", "Inventory", "Spells", "Switch Spell Order","Exit Server")
            this.attributes["esc_menu"].is_esc_menu = True
            this.attributes["esc_menu_type"] = "main"

        if this.attributes["keys"][display.KEY_INVENTORY]:
            this.attributes["using_inv"] = True
            data = bytearray([2]) # Header byte
            for itm in this.attributes["items"]:
                itm_data  = bytearray()
                itm_data += bytearray(itm.type, 'utf-8') + bytearray(1) # Put a null byte after so split works.
                itm_data += bytearray(itm.name + itm.attributes["disp_data"], 'utf-8')
                if itm == this.attributes[itm.type]: # If equipped
                    itm_data += bytearray(" \\fg(Equipped)\\fw", 'utf-8')
                itm_data += bytearray(1) + bytearray(itm.description, 'utf-8') + bytearray(1)
                itm_data += struct.pack("!I", itm.amount)
                itm_data += struct.pack("!I", itm.value)
                data += struct.pack("!I", len(itm_data)) + itm_data
            this.attributes["inv_data"] = data
        # Check HP diff for flash on hit stuff
        if this.attributes["HP"] < this.attributes["lastHP"]:
            this.attributes["sincehit"] = 0
        else:
            this.attributes["sincehit"] += delta_time

        # Check for movement. TODO: maybe add speed multiplier?
        if this.attributes["keys"][display.KEY_MOV_UP] and (not "del_up" in this.attributes["effects"]):
            if (this.Y > 0) and world.map[this.X][this.Y - 1][3]:
                this.Y -= 1
            this.attributes["effects"]["del_up"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if this.attributes["keys"][display.KEY_MOV_DOWN] and (not "del_down" in this.attributes["effects"]):
            if (this.Y < world.WORLD_Y - 1) and world.map[this.X][this.Y + 1][3]:
                this.Y += 1
            this.attributes["effects"]["del_down"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if this.attributes["keys"][display.KEY_MOV_LEFT] and (not "del_left" in this.attributes["effects"]):
            if (this.X > 0) and world.map[this.X - 1][this.Y][3]:
                this.X -= 1
            this.attributes["effects"]["del_left"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if this.attributes["keys"][display.KEY_MOV_RIGHT] and (not "del_right" in this.attributes["effects"]):
            if (this.X < world.WORLD_X - 1) and world.map[this.X + 1][this.Y][3]:
                this.X += 1
            this.attributes["effects"]["del_right"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))

        # Check for spell cast
        if this.attributes["keys"][display.KEY_SPELL] and this.attributes["can_cast"]:
            this.attributes["spells"][this.attributes["spell"]].cast(this)
            this.attributes["can_cast"] = False
        if not this.attributes["keys"][display.KEY_SPELL]:
            this.attributes["can_cast"] = True

        # Check for spell cycle
        if this.attributes["keys"][display.KEY_LASTSPELL] and this.attributes["can_spell_cycle"]:
            if this.attributes["spell"] == 0: # Cycle to end of list if at start
                this.attributes["spell"] = len(this.attributes["spells"])
            this.attributes["spell"] -= 1     # Cycle backwards
            this.attributes["can_spell_cycle"] = False
        if this.attributes["keys"][display.KEY_NEXTSPELL] and this.attributes["can_spell_cycle"]:
            this.attributes["spell"] += 1
            if this.attributes["spell"] >= len(this.attributes["spells"]): # If at end of list, cycle to start
                this.attributes["spell"] = 0
            this.attributes["can_spell_cycle"] = False
        if not (this.attributes["keys"][display.KEY_LASTSPELL] or this.attributes["keys"][display.KEY_NEXTSPELL]):
            this.attributes["can_spell_cycle"] = True

        # Attacks! TODO: maybe add speed multiplier? So you can have really slow weapons.
        if this.attributes["keys"][display.KEY_ATK_UP] and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y, 0, -1, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))

        if this.attributes["keys"][display.KEY_ATK_LEFT] and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y, -1, 0, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))

        if this.attributes["keys"][display.KEY_ATK_DOWN] and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y, 0, 1, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))

        if this.attributes["keys"][display.KEY_ATK_RIGHT] and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y, 1, 0, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
            # Or with our constants in python, time = 500/(1+2.718^(.01x)), which is a nice logistic formula.

        # Check for item use
        if this.attributes["keys"][display.KEY_ITEM] and this.attributes["can_item"] and (this.attributes["consumable"].name != "Nothing"):
            this.attributes["consumable"].use(this)
            this.attributes["can_item"] = False
            this.attributes["consumable"].amount -= 1
            if this.attributes["consumable"].amount <= 0:
                del this.attributes["items"][this.attributes["items"].index(this.attributes["consumable"])]
                this.attributes["consumable"] = no_item.no_consumable()
        if not this.attributes["keys"][display.KEY_ITEM]:
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

        this.attributes["lastHP"] = this.attributes["HP"] # Reset lastHP, done after effect updating.

        if this.attributes["sidebar"].count('\n') == sidebar_len:
            this.attributes["sidebar"] += " No effects\n"

        if this.attributes["HP"] <= 0: # Dead
            for eff_name, eff in this.attributes["effects"].items():
                eff.uneffect(this)
            this.attributes["effects"].clear()

            this.attributes["HP"] = this.attributes["maxHP"]                    # Recover HP
            this.X = this.attributes["respawnX"]                                # Return to last saved place
            this.Y = this.attributes["respawnY"]
            world.move_requests.append((this.attributes["respawnMap"], this))   # At last saved map...
            world.to_del_plr.append(this)                                       # Exit from this map.
            print("Player died")

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



    # All extra data to be sent. So HP/MP, equip stuff, sidebar stuff.
    def extra_data(this):
        if this.attributes["HP"] < 0:
            this.attributes["HP"] = 0
        hp = struct.pack("!I", int(this.attributes["HP"])) + struct.pack("!I", int(this.attributes["maxHP"]))
        mp = struct.pack("!I", int(this.attributes["MP"])) + struct.pack("!I", int(this.attributes["maxMP"]))
        level = struct.pack("!I", this.attributes["level"])
        exp = struct.pack("!I", exp_req(this.attributes["level"]) - this.attributes["EXP"])
        gold = struct.pack("!I", this.attributes["money"])
        spell_image = bytearray(this.attributes["spells"][this.attributes["spell"]].image, 'utf-8')
        spell_len = struct.pack("!I", len(spell_image))

        item_image = bytearray(this.attributes["consumable"].attributes["icon"], 'utf-8')
        item_len = struct.pack("!I", len(item_image))

        equip_info = bytes()
        for type in ["weapon", "hat", "shirt", "pants", "ring"]:
            type_info   = bytearray(this.attributes[type].name, 'utf-8')
            type_len    = struct.pack("!I", len(type_info))
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

def exp_req(lvl): # Weird exponential/polynomial EXP requirement.
  return int(2 * 1.4 ** lvl + lvl ** 3 + lvl + 1)

def gain_exp(this, amount):
    this.attributes["EXP"] += amount
    # Takes 0.5L^2 + .5L + 4 EXP to level
    while this.attributes["EXP"] >= exp_req(this.attributes["level"]): # They levelled up!
        this.attributes["EXP"] -= exp_req(this.attributes["level"]) # Remove EXP required for level
        if this.attributes["level"] >= 20: # Max level
            this.attributes["HP"] = this.attributes["maxHP"] # HP restore
            this.attributes["MP"] = this.attributes["maxMP"] # MP restore
            continue

        this.attributes["level"] += 1 # Duh.
        if this.attributes["level"] in spells.spell_gain_levels:               # They have a spell to gain
            sp_index = spells.spell_gain_levels.index(this.attributes["level"])
            if this.attributes["class"] == "warrior":
                this.attributes["spells"].append(copy.deepcopy(spells.warrior_spells[sp_index])) # Copy in case something changes in the
            if this.attributes["class"] == "mage":                                               #  spell. ex: a spell that teleports you
                this.attributes["spells"].append(copy.deepcopy(spells.mage_spells[sp_index]))    #  to where you were when it was last cast
            if this.attributes["class"] == "thief":                                              #  would need a saved state.
                this.attributes["spells"].append(copy.deepcopy(spells.thief_spells[sp_index]))

        if this.attributes["class"] == "warrior":
            this.attributes["maxHP"] += 15 # Give stats.
            this.attributes["maxMP"] += 5
            this.attributes["mov_spd"] += 1
            this.attributes["atk_spd"] += 1
            this.attributes["magic"] += 1
            this.attributes["strength"] += 2
        if this.attributes["class"] == "mage":
            this.attributes["maxHP"] += 10 # Give stats.
            this.attributes["maxMP"] += 15
            this.attributes["mov_spd"] += 3
            this.attributes["atk_spd"] += 3
            this.attributes["magic"] += 3
            this.attributes["strength"] += 1
        if this.attributes["class"] == "thief":
            this.attributes["maxHP"] += 5  # Give stats.
            this.attributes["maxMP"] += 10
            this.attributes["mov_spd"] += 5
            this.attributes["atk_spd"] += 5
            this.attributes["magic"] += 2
            this.attributes["strength"] += 3

        this.attributes["HP"] = this.attributes["maxHP"] # HP restore on level
        this.attributes["MP"] = this.attributes["maxMP"] # MP restore on level
