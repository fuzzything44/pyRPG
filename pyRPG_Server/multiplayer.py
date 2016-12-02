import select

import display
from objects import world_object
import world
from effects import effect

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

class player(world_object.world_object):
    """description of class"""
    def __init__(this, posX, posY, sock, addr):
        super().__init__(posX, posY, "player")
        this.attributes.update({\
            "socket" : sock,    \
            "address" : addr,   \
            "timeout" : 0,      \
            "keys"    : [0] * 11\
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
              #"spell" : spell.spell(0, world_object.no_func, ["   ", "   ", "   "], display.WHITE), \
              #"weapon" : item.item("", "weapon", 0, 1, {"damage" : 1, "range" : 1}),                \
              #"hat" : item.item("", "hat", 0),                                                      \
              #"shirt" : item.item("", "shirt", 0),         \
              #"pants" : item.item("", "pants", 0),         \
              #"ring" : item.item("", "ring", 0),           \
              #"consumable" : item.item("Nothing", "consumable", 0, 1, {"icon" : ["   ", "   ", "   "], "color" : 0, "use" : world_object.no_func}), \
              "mov_spd" : 0,                    # How quickly they move
              "atk_spd" : 0,                    # How quickly they attack
              "can_cast" : True,                 \
              "can_item" : True,                 \
              "magic" : 5,                      # How good spells are 
              "strength" : 5,                   # How much damage regular attacks do. 
              "luck" : 0,                       # Luck will change item and money drops
              #"gainexp" : gain_exp,              \
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
            except ConnectionResetError as ex:
                world.to_del_plr.append(this)
                return
        else:
            this.attributes["timeout"] += delta_time
            if this.attributes["timeout"] > 100000000000000:
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
                this.attributes["consumable"] = item.item("Nothing", "consumable", 0, 1, {"icon" : ["   ", "   ", "   "], "color" : 0})
                this.attributes["consumable"].draw()
        if not this.attributes["keys"][KEY_SHIFT]:
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
    



