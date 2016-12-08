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
from spells import heal
from spells import lifesteal
from spells import spell

import pickle

import struct
import select

# Key defs
KEY_W = 0
KEY_A = 1
KEY_S = 2
KEY_D = 3

KEY_I = 4
KEY_J = 5
KEY_K = 6
KEY_L = 7

KEY_SHIFT = 8
KEY_SPACE = 9
KEY_ENTER = 10

KEY_UP = 11
KEY_Q = 11

KEY_DOWN = 12
KEY_E    = 12

# Not actually a key but packed with them. What map they think they're in.
KEY_MAPID = 13


class player(world_object.world_object):
    """description of class"""
    def __init__(this, posX, posY, sock, addr):
        super().__init__(posX, posY, "player")
        this.attributes.update({\
            "socket" : sock,    \
            "address" : addr,   \
            "timeout" : 0,      \
            "current_map" : 0,  \
            "sidebar" : "",     \
            "current_menu" : None,\
            "keys"    : [0] * 13\
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
              "items" : [],                     \
              "class" : "warrior",              \
              "spell" : spell.spell(heal.manaCost, heal.heal, heal.name, heal.icon),                \
              "weapon" : item.item("", "weapon", 0, 1, {"damage" : 1, "range" : 1}),                \
              "hat" : item.item("", "hat", 0),                                                      \
              "shirt" : item.item("", "shirt", 0),         \
              "pants" : item.item("", "pants", 0),         \
              "ring" : item.item("", "ring", 0),           \
              "consumable" : item.item("Nothing", "consumable", 0, 1, {"icon" : "   \n   \n   ", "color" : 0, "use" : world_object.no_func}), \
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
        if select.select([this.attributes["socket"]], [], [], 0) != ([], [], []):
            try:
                (this.attributes["keys"], addr) = this.attributes["socket"].recvfrom(65507)
                while select.select([this.attributes["socket"]], [], [], 0) != ([], [], []):
                    this.attributes["socket"].recvfrom(65507)
                this.attributes["timeout"] = 0
                if this.attributes["keys"][KEY_MAPID] != this.attributes["current_map"]:
                    pass# Send map data to player
                    data = bytearray(2) + pickle.dumps(world.map)
                    data[0] = 1
                    data[1] = this.attributes["current_map"]
                    this.attributes["socket"].sendto(data, this.attributes["address"])
            except ConnectionResetError as ex:
                world.to_del_plr.append(this)
                return
        else:
            this.attributes["timeout"] += delta_time
            if this.attributes["timeout"] > 1000:
                world.to_del_plr.append(this)
                return

        # Check HP diff for flash on hit stuff
        if this.attributes["HP"] < this.attributes["lastHP"]:
            this.attributes["sincehit"] = 0
        else:
            this.attributes["sincehit"] += delta_time
    
        # Check for movement
        if this.attributes["keys"][KEY_W] and (not "del_up" in this.attributes["effects"]):
            if (this.Y > 0) and world.map[this.X][this.Y - 1][3]:
                this.Y -= 1
            this.attributes["effects"]["del_up"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if this.attributes["keys"][KEY_S] and (not "del_down" in this.attributes["effects"]):
            if (this.Y < world.WORLD_Y - 1) and world.map[this.X][this.Y + 1][3]:
                this.Y += 1
            this.attributes["effects"]["del_down"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if this.attributes["keys"][KEY_A] and (not "del_left" in this.attributes["effects"]):
            if (this.X > 0) and world.map[this.X - 1][this.Y][3]:
                this.X -= 1
            this.attributes["effects"]["del_left"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))
        if this.attributes["keys"][KEY_D] and (not "del_right" in this.attributes["effects"]):
            if (this.X < world.WORLD_X - 1) and world.map[this.X + 1][this.Y][3]:
                this.X += 1
            this.attributes["effects"]["del_right"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["mov_spd"])))

        # Check for spell cast
        if this.attributes["keys"][KEY_SPACE] and this.attributes["can_cast"]:
            this.attributes["spell"].cast(this)
            this.attributes["can_cast"] = False
        if not this.attributes["keys"][KEY_SPACE]:
            this.attributes["can_cast"] = True

        # Attacks!
        if this.attributes["keys"][KEY_I] and (this.Y != 0) and (world.map[this.X][this.Y - 1][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y - 1, 0, -1, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
    
        if this.attributes["keys"][KEY_J] and (this.X != 0) and (world.map[this.X - 1][this.Y][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X - 1, this.Y, -1, 0, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
    
        if this.attributes["keys"][KEY_K] and (this.Y != 19) and (world.map[this.X][this.Y + 1][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X, this.Y + 1, 0, 1, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
    
        if this.attributes["keys"][KEY_L] and (this.X != 49) and (world.map[this.X + 1][this.Y][3]) and (not "del_atk" in this.attributes["effects"]):
            world.objects.append(attack.attack(this.X + 1, this.Y, 1, 0, (this.attributes["strength"] * this.attributes["weapon"].attributes["damage"] // 2), this.attributes["weapon"].attributes["range"], 100, this))
            this.attributes["effects"]["del_atk"] = effect.effect(this, 500/(1+2.718**(.01*this.attributes["atk_spd"])))
            # Or with our constants in python, time = 500/(1+2.718^(.01x)), which is a nice logistic formula.
    
        # Check for item use
        if this.attributes["keys"][KEY_SHIFT] and this.attributes["can_item"] and (this.attributes["consumable"].name != "Nothing"):
            this.attributes["consumable"].use(this)
            this.attributes["can_item"] = False
            this.attributes["consumable"].amount -= 1
            if this.attributes["consumable"].amount == 0:
                del this.attributes["items"][this.attributes["items"].index(this.attributes["consumable"])]
                this.attributes["consumable"] = item.item("Nothing", "consumable", 0, 1, {"icon" : "   \n   \n   ", "color" : 0})
        if not this.attributes["keys"][KEY_SHIFT]:
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
        hp = struct.pack("!I", int(this.attributes["HP"])) + struct.pack("!I", int(this.attributes["maxHP"]))
        mp = struct.pack("!I", int(this.attributes["MP"])) + struct.pack("!I", int(this.attributes["maxMP"]))
        level = struct.pack("!I", this.attributes["level"])
        exp = struct.pack("!I", int(0.5*this.attributes["level"]**2 + 0.5*this.attributes["level"] + 4 - this.attributes["EXP"]))

        spell_len = struct.pack("!I", len(this.attributes["spell"].image))
        spell_image = bytearray(this.attributes["spell"].image, 'utf-8')

        item_len = struct.pack("!I", len(this.attributes["consumable"].attributes["icon"]))
        item_image = bytearray(this.attributes["consumable"].attributes["icon"], 'utf-8')

        # So we need an int for length and then all the data.
        sidebar_data = None
        if this.attributes["current_menu"] is None:
            sidebar_data = bytearray(this.attributes["sidebar"], 'utf-8')
        else:
            sidebar_data = this.attributes["current_menu"].disp()
        sidebar_len  = struct.pack("!I", len(sidebar_data))
        # Sidebar stuff is sent, so now we zero it out.
        this.attributes["sidebar"] = ""
        
        
        return hp + mp + level + exp + spell_len + spell_image + item_len + item_image + sidebar_len + sidebar_data

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
