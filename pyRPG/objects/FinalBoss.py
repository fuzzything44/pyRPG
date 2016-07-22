from random import randrange

import display
import world

from items import item
from objects import attack
from objects import world_object
from spells import spell

def FinalBoss_update(this, delta_time):
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
        pass

def FinalBoss_collide(this, obj):
    pass

def FinalBossColor(this):
    return display.RED

def FinalBossChar(this):
    return 'P'

FinalBoss_type = 'enemy'

FinalBoss_attributes = \
    {"HP": 1000.0, \
     "MP": 1000.0, \
     "effects": {}, \
     "mov_spd": 40, \
     "attk_spd": 60, \
     "damage": 30, \
     "EXP": 10000, \
     "range": 10, \
}