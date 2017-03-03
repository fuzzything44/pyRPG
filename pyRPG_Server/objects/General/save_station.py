import display
import world

from objects import world_object

class save_station(world_object.world_object):
    """Lets players set new respawn location"""

    def __init__(this, posX, posY):
        super().__init__(posX, posY, "savepoint")

    def update(this, delta_time):
        for plr in world.players:
            if ((plr.X - this.X) ** 2 + (plr.Y - this.Y) ** 2) < 4:
                if plr.X == plr.attributes["respawnX"] and plr.Y == plr.attributes["respawnY"] and plr.attributes["respawnMap"] == world.world_name:
                    plr.attributes["sidebar"] += "Respawn Location set\n"
                else:
                    plr.attributes["sidebar"] += "Press E to set respawn\n"

                if plr.attributes["keys"][display.KEY_E] and plr.attributes["current_menu"] is None and plr.attributes["esc_menu"] is None: # They pressed E
                    plr.attributes["respawnMap"] = world.world_name
                    plr.attributes["respawnX"] = plr.X
                    plr.attributes["respawnY"] = plr.Y


    def char(this):
        return 'S'

    def color(this):
        return display.YELLOW




