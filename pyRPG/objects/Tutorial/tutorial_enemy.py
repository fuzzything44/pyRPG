import random

import display
import world

from objects import world_object

def update(this, delta_time):
    if this.attributes["HP"] <= 0:
        world.to_del.append(this) # Delete
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give exp

# Deals some damage...
def collide(this, oth):
    if "HP" in oth.attributes:
        oth.attributes["HP"] -= this.attributes["damage"]
        oth.X += random.randrange(0, 2) * 2 - 1 # Bounce back other a bit. Left or right
        if oth.X < 0: # Make sure they don't exit the world.
            oth.X += 2
        if oth.X >= world.WORLD_X:
            oth.X -= 2

def char(this):
    return 'Q'

def color(this):
    return display.CYAN

type = "enemy"
attributes = {      \
    "HP" : 1,       \
    "damage" : 1,   \
    "EXP" : 1       \
  }