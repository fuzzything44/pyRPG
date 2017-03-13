import random

import display
import world

from objects import world_object

from objects.tutorial.war_tut import war_enemy

class war_spawner(world_object.world_object):
    """Spawns war_enemies"""

    def __init__(this, posX, posY):
        super().__init__(posX, posY, "spawner")
        this.attributes["current_enemy"] = None

    def update(this, delta_time):
        if this.attributes["current_enemy"] is None and (random.randint(0, 2000) < delta_time): # Possibly respawn enemy.
            s_enemy = war_enemy.war_enemy(this.X, this.Y, this)
            world.objects.append(s_enemy)
            this.attributes["current_enemy"] = s_enemy

    def color(this):
        return display.RED

    def char(this):
        return '%'

    


