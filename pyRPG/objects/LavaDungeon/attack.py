import math
import random

import display
import world

from objects.General import base_attack

class circle_attack(base_attack.base_attack):
    def __init__(this, damage, radius, owner):
        super().__init__(0, 0, damage, owner)
        this.attributes.update({\
            "theta" : random.randrange(0, 360),
            "radius" : radius
          })

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
    
