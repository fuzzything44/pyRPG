import math

import display
import world

def update(this, delta_time):
    this.attributes["theta"] += (delta_time * .01 / this.attributes["radius"])
    if this.attributes["theta"] > 360:
        this.attributes["theta"] -= 360

    this.X = int(this.attributes["radius"]*math.cos(this.attributes["theta"]) + this.attributes["owner"].X)
    this.Y = int(this.attributes["radius"]*math.sin(this.attributes["theta"]) + this.attributes["owner"].Y)
    if this.X < 0:
        this.X = 0
    if this.X >= world.WORLD_X:
        this.X = world.WORLD_X - 1
    if this.Y < 0:
        this.Y = 0
    if this.Y >= world.WORLD_Y:
        this.Y = world.WORLD_Y - 1




def collide(this, oth):
    if (this.attributes["owner"].type != oth.type) and ("HP" in oth.attributes):
        oth.attributes["HP"] -= this.attributes["damage"]
        world.to_del.append(this)
        this.attributes["owner"].attributes["attack"] = None


    
def char(this):
    return '!'

def color(this):
    return display.MAGENTA

type = "damage"

attributes = {          \
    "damage" : 1,       \
    "owner" : None,     \
    "theta" : 0,        \
    "radius" : 1        \
  }