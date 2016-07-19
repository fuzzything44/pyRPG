import time
import sys

from objects import attack
import display
from items import item
import world
from objects import world_object
from spells import spell
from random import randrange

def enemy_update(this, delta_time):
    if this.attributes["HP"] < 0:
      world.to_del.append(this)
    else:        
      #if randrange(0, 1000) = 999:  
       # this.X += randrange(-1, 2)
       # this.Y += randrange(-1, 2)
      #else:
      pass

def enemy_collide(this, obj):
  pass

def enemyColor(this):
  return display.CYAN

def enemyChar(this):
  return 'Q'

enemy_type = "enemy"

enemy_attributes =                     \
    { "HP" : 100.0,                     \
      "MP" : 50,                        \
      "effects" : {},                   \
      "mov_spd" : 30,                    \
      "atk_spd" : 150,                   \
      "damage" : 5                      \
    }