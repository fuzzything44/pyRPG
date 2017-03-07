import display
import world

from effects import fire
from objects.General import base_attack

class fire_rain(base_attack.base_attack):
    """Sits and hurts stuff."""
    def __init__(this, posX, posY, damage, owner, team = None):
        super().__init__(posX, posY, damage, owner, team)
        this.attributes["time_left"] = 11111

    def update(this, delta_time):
        this.attributes["time_left"] -= delta_time
        if this.attributes["time_left"] < 0:
            world.to_del.append(this)

    def collide(this, oth):
        if not (this.attributes["team"] & base_attack.get_team(oth)) and ("effects" in oth.attributes):
            if "burning" not in oth.attributes["effects"]:
                oth.attributes["effects"]["burning"] = fire.fire(oth, 10000, 0.2 * this.attributes["damage"])
            else:
                oth.attributes["effects"]["burning"].time += 5000
                oth.attributes["effects"]["burning"].damage += this.attributes["damage"] / 7.0
        super().collide(oth)

    def color(this):
        return display.RED



