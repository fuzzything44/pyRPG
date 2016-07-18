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
        this.X = randrange(0, world.WORLD_X)
        this.Y = randrange(0, world.WORLD_Y)


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
    }