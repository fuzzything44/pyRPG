from random import randrange

import display
import world

from objects.Loot import money
from objects import world_object
from objects import obj_maker
from spells import spell

from objects.LavaDungeon import attack

def update(this, delta_time):
    # If within 5 tiles of player...
    if ((this.X - world.player.X) ** 2 + (this.Y - world.player.Y) ** 2) <= this.attributes["aggro_range"]:
        if not ("mov_del" in this.attributes["effects"]): # Possibly move to player.
            diffX = this.X - world.player.X # How much it needs to move left to hit player
            diffY = this.Y - world.player.Y # How much it needs to move down to hit player
            if diffX < 0 and (world.map[this.X + 1][this.Y][3]): # Make sure you don't move onto a wall
                this.X += 1
            if diffX > 0 and (world.map[this.X - 1][this.Y][3]):
                this.X -= 1
            if diffY < 0 and world.map[this.X][this.Y + 1][3]:
                this.Y += 1
            if diffY > 0 and world.map[this.X][this.Y - 1][3]:
                this.Y -= 1
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
        if (this.attributes["attack"] is None) and ("del_atk" not in this.attributes["effects"]): # Must make a new attack
            this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, this.attributes["atk_spd"]]
            atk = obj_maker.make(attack, 0, 0, {"damage" : this.attributes["damage"], "owner" : this, "theta" : randrange(0, 360), "radius" : randrange(this.attributes["range_min"], this.attributes["range_max"] + 1)})
            world.objects.append(atk)
            this.attributes["attack"] = atk

    # Loop effects
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
    # Possibly die.
    if this.attributes["HP"] <= 0:
        world.to_del.append(this)
        moneydrop = this.attributes["money"] + randrange(0, this.attributes["money"])
        moneydrop += moneydrop*world.player.attributes["luck"]*.01
        moneydrop = max(1, int(moneydrop))
        world.objects.append(obj_maker.make(money, this.X, this.Y, {"value": moneydrop, "taken" : False}))
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give experience

def collide(this, obj):
    if obj.type == "player" and ("del_atk" not in this.attributes["effects"]):
        obj.attributes["HP"] -= this.attributes["damage"]
        this.attributes["effects"]["del_atk"] = [world_object.no_func, world_object.no_func, this.attributes["atk_spd"]]


def color(this):
  return display.CYAN

def char(this):
  return 'Y'

type = "enemy"

attributes =      \
    { "HP" : 30.0,      \
      "effects" : {},   \
      "mov_spd" : 500,  \
      "atk_spd" : 150,  \
      "damage" : 7,     \
      "range_min" : 1,  \
      "range_max" : 5,  \
      "aggro_range" : 100,\
      "EXP" : 10,       \
      "money" : 5,      \
      "attack" : None   \
    }