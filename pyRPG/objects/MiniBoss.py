from random import randrange

import display
import world

from items import item
from objects import attack
from objects import world_object
from spells import spell

def MiniBoss_update(this, delta_time):
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
    if this.attributes["HP"] <= 0:
        world.to_del.append(this)
    else:        
        if randrange(0, this.attributes["mov_spd"]) < delta_time:  
            this.X += randrange(-1, 2)
            this.Y += randrange(-1, 2)
            if this.X < 0:
                this.X = 0
            if this.Y < 0:
                this.Y = 0

def MiniBosscollide(this, obj):
    if obj.type == "player":
        obj.attributes["HP"] -= this.attributes["damage"]
        this.X += 1


def MiniBossColor(this):
  return display.RED

def MiniBossChar(this):
  return 'p'

MiniBoss_type = "enemy"

MiniBoss_attributes =                     \
    { "HP" : 100.0,                     \
      "MP" : 50,                        \
      "effects" : {},                   \
      "mov_spd" : 200,                    \
      "atk_spd" : 150,                   \
      "damage" : 10,                      \
      "EXP" : 5
    }