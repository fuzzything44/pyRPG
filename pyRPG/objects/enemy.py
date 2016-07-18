import time
import sys

from objects import attack
import display
from items import item
import world
from objects import world_object
from spells import spell

def enemy_update(this, delta_time):
  pass


def enemy_collide(this, obj):
  pass

def enemyColor(this):
  return display.CYAN

def enemyChar(this):
  return 'Q'



enemy_attributes =                     \
    { "HP" : 100.0,                     \
      "MP" : 50,                        \
      "effects" : {},                   \
      "mov_spd" : 30,                    \
      "atk_spd" : 150,                   \
    }