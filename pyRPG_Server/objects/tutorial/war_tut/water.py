import display
import world

from effects import effect

from objects import world_object

class water(world_object.world_object):
    """Slows players down when they're in water."""

    def __init__(this):
        super().__init__(0, 0, "environmental")

    def update(this, delta_time):
        for plr in world.players:
            if world.map[plr.X][plr.Y] == [display.BLUE, display.BLUE, 'W', True] and "water_slow" not in plr.attributes["effects"]:
                plr.attributes["effects"]["water_slow"] = effect.effect(plr, 999, "Slow", {"mov_spd" : -100})



