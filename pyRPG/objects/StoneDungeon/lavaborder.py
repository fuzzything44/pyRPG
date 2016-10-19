import world
from effects import fire
from objects import world_object

class lavaborder(world_object.world_object):
    def __init__(this):
        super().__init__(0, 0, "damage")
        this.attributes["sincehit"] = 101
    def update(this, delta_time):
        this.attributes["sincehit"] += delta_time
    
        # If they're on the border...
        if (world.player.X == 0) or (world.player.X == world.WORLD_X - 1) or (world.player.Y == 0) or (world.player.Y == world.WORLD_Y - 1):
             if this.attributes["sincehit"] > 100:
                 world.player.attributes["HP"] -= 10
                 this.attributes["sincehit"] = 0
                 world.player.attributes["effects"]["fire"] = [fire.fire, world_object.no_func, 1000]
    