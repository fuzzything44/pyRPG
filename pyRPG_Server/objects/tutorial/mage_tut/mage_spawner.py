import random

import display
import world

from objects import world_object

from objects.tutorial.mage_tut import mage_enemy

class mage_spawner(world_object.world_object):
    """Spawns war_enemies"""

    def __init__(this, posX, posY):
        super().__init__(posX, posY, "spawner")
        this.attributes["collided"] = False

    def update(this, delta_time):
        if not this.attributes["collided"] and (random.randint(0, 2000) < delta_time): # Possibly respawn enemy.
            s_enemy = mage_enemy.mage_enemy(this.X, this.Y)
            world.objects.append(s_enemy)
            this.attributes["current_enemy"] = s_enemy
        this.attributes["collided"] = False

    def collide(this, obj):
        this.attributes["collided"] = True

    def color(this):
        return display.RED

    def char(this):
        return '+'

    


