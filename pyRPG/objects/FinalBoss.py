from random import randrange

import display
import world

from items import item
from objects import attack
from objects import world_object

def FinalBoss_update(this, delta_time):
    # Movement code
    if not ("mov_del" in this.attributes["effects"]):
        diffX = this.X - world.player.X # How much it needs to move left to hit player
        diffY = this.Y - world.player.Y # How much it needs to move down to hit player
        if diffX < 0:
            this.X -= 1
        else:
            this.X += 1
        if diffY < 0:
            this.Y -= 1
        else:
            this.Y += 1

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
        world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, \
        this.X + 1, this.Y, {"movex" : 1, "movey": 0, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, \
        this.X - 1, this.Y, {"movex" : -1, "movey": 0, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, \
        this.X, this.Y + 1, {"movex" : 0, "movey": 1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, \
        this.X, this.Y - 1, {"movex" : 0, "movey": -1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, \
        this.X + 1, this.Y + 1, {"movex" : 1, "movey": 1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, \
        this.X + 1, this.Y - 1, {"movex" : 1, "movey": -1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, \
        this.X - 1, this.Y + 1, {"movex" : -1, "movey": 1, "range" : this.attributes["range"], "damage" : this.attributes["damage"], "speed" : 300, "to_move" : 0, "owner" : this}\
        ))
        world.objects.append(world_object.world_object(attack.attk_update, attack.attk_coll, attack.attk_char, attack.attk_color, attack.attk_type, \
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
    else:        
        pass

def FinalBoss_collide(this, obj):
    pass

def FinalBossColor(this):
    return display.RED

def FinalBossChar(this):
    return 'P'

FinalBoss_type = 'enemy'

FinalBoss_attributes = \
    {"HP": 1000.0,  \
     "lastHP" : 1000.0, \
     "MP": 1000.0,  \
     "effects": {}, \
     "mov_spd": 400, \
     "atk_spd": 600, \
     "damage": 30, \
     "EXP": 300, \
     "range": 10, \
}