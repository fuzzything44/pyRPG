import world
from effects import fire
from objects import world_object

def update(this, delta_time):
    this.attributes["sincehit"] += delta_time

    # If they're on the border...
    if (world.player.X == 0) or (world.player.X == world.WORLD_X - 1) or (world.player.Y == 0) or (world.player.Y == world.WORLD_Y - 1):
         if this.attributes["sincehit"] > 100:
             world.player.attributes["HP"] -= 10
             this.attributes["sincehit"] = 0
             world.player.attributes["effects"]["fire"] = [fire.fire, world_object.no_func, 1000]


def collide(this, oth):
    pass

def char(this):
    return '\0'

def color(this):
    return 0

type = "damage"

attributes = {"sincehit" : 101 }