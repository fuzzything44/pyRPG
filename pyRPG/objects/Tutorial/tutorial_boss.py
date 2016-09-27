from random import randrange

import display
import world

from items import item
from items import bread
from objects.Player import attack
from objects.Loot import chest
from objects.Loot import money
from objects import world_object
from objects import obj_maker
from spells import spell

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
    # Attack code
    this.attributes["to_atk"] -= delta_time
    if this.attributes["to_atk"] <= 0:
        this.attributes["to_atk"] = this.attributes["atk_spd"] - 200 + this.attributes["HP"] # He attacks faster with less HP
        # Find which direction to shoot
        diffX = world.player.X - this.X # How much it needs to move left to hit player
        diffY = world.player.Y - this.Y # How much it needs to move down to hit player
        if diffX < 0:
            diffX = -1
        else:
            diffX = int(not not diffX)
        if diffY < 0:
            diffY = -1
        else:
            diffY = int(not not diffY)
        world.objects.append(obj_maker.make(attack, this.X + diffX, this.Y + diffY, {"movex" : diffX, "movey" : diffY, "damage" : this.attributes["damage"], "range" : this.attributes["range"], "speed" : 250, "to_move" : 125, "owner" : this}))
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
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give experience
        world.load("tutorial.boss-killed")
        world.objects = [world.player] + world.objects
        world.player.X = 10
        world.player.Y = 10
        world.dispworld()
        return True

def collide(this, obj):
    if obj.type == "player":
        obj.attributes["HP"] -= this.attributes["damage"]
        this.X += 1
        if this.X == world.WORLD_X:
            this.X = 0


def color(this):
    return display.CYAN

def char(this):
    return 'B'

type = 'enemy'

attributes =        \
    {"HP": 150.0,   \
     "effects": {}, \
     "to_atk" : 500,\
     "mov_spd": 500,\
     "atk_spd": 900,\
     "damage": 7,  \
     "EXP": 10,     \
     "range": 5,    \
}