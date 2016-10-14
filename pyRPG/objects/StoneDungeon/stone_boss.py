from random import randrange

import display
import world

from items import item
from objects.Player import attack
from objects.Loot import chest
from objects import world_object

def update(this, delta_time):
    # Movement code
    if not ("mov_del" in this.attributes["effects"]):
        diffX = this.X - world.player.X # How much it needs to move left to hit player
        diffY = this.Y - world.player.Y # How much it needs to move down to hit player
        if diffX < 0:
            this.X += 1
        else:
            this.X -= (not not diffX) # Should give either 1 or 0.
        if diffY < 0:
            this.Y += 1
        else:
            this.Y -= (not not diffY)
        # Add boundary checking
        if this.X == 0: # Left side
            this.X += 1
        if this.X == world.WORLD_X - 1: # Right side
            this.X -= 1
        if this.Y == 0: # Top
            this.Y += 1
        if this.Y == world.WORLD_Y - 1: # Bottom
            this.Y -= 1
        this.attributes["effects"]["mov_del"] = [world_object.no_func, world_object.no_func, this.attributes["mov_spd"]]
    if not ("atk_del" in this.attributes["effects"]):
        # Attack!
        world.objects.append(obj_maker.make(attack, \
        this.X + 1, this.Y, {"movex" : 1, "movey": 0, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(obj_maker.make(attack, \
        this.X - 1, this.Y, {"movex" : -1, "movey": 0, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(obj_maker.make(attack, \
        this.X, this.Y + 1, {"movex" : 0, "movey": 1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(obj_maker.make(attack, \
        this.X, this.Y - 1, {"movex" : 0, "movey": -1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(obj_maker.make(attack, \
        this.X + 1, this.Y + 1, {"movex" : 1, "movey": 1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(obj_maker.make(attack, \
        this.X + 1, this.Y - 1, {"movex" : 1, "movey": -1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(obj_maker.make(attack, \
        this.X - 1, this.Y + 1, {"movex" : -1, "movey": 1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(obj_maker.make(attack, \
        this.X - 1, this.Y - 1, {"movex" : -1, "movey": -1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        this.attributes["effects"]["atk_del"] = [world_object.no_func, world_object.no_func, this.attributes["atk_spd"]]
    eff_del_list = []
    for eff in this.attributes["effects"]:
        this.attributes["effects"][eff][0](this, delta_time)       # Tick code
        this.attributes["effects"][eff][2] -= delta_time           # Lower time
        if this.attributes["effects"][eff][2] <= 0:                # Remove effect
            eff_del_list.append(eff)
    for to_del in eff_del_list:
        this.attributes["effects"][to_del][1](this)
        del this.attributes["effects"][to_del]
    del eff_del_list
    if this.attributes["HP"] < this.attributes["lastHP"]:
        diff = this.attributes["lastHP"] - this.attributes["HP"] # Difference in HP between this frame and last frame
        if diff > 10: # Soft damage cap
            diff = 10 + ((diff - 10) ** .75)
        if diff > 50: # Hard damage cap
            diff = 50
        this.attributes["lastHP"] -= diff
        this.attributes["HP"] = this.attributes["lastHP"]
    if this.attributes["HP"] <= 0:
        world.to_del.append(this)
        chest_attr = {"contents": []}
        world.map[25][10] = world.WORLD_CHEST
        display.printc(25, 15, '@', display.YELLOW)
        # Add actual chests
        world.objects.append(obj_maker.make(chest, 24, 10, chest_attr))
        world.objects.append(obj_maker.make(chest, 26, 10, chest_attr))
        world.objects.append(obj_maker.make(chest, 25, 9, chest_attr))
        world.objects.append(obj_maker.make(chest, 25, 11, chest_attr))
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give experience


def collide(this, obj):
    pass

def color(this):
    return display.RED

def char(this):
    return 'P'

type = 'enemy'

attributes = \
    {"HP": 1000.0,  \
     "lastHP" : 1000.0, \
     "MP": 1000.0,  \
     "effects": {}, \
     "mov_spd": 400, \
     "atk_spd": 1000, \
     "damage": 30, \
     "EXP": 300, \
     "range": 10, \
}