import random

import display
import world

from objects.General import enemy_base

class enemy(enemy_base.enemy_base):   
    # Deals some damage...
    def collide(this, oth):
        if "HP" in oth.attributes:
            oth.attributes["HP"] -= this.attributes["damage"]
            oth.X += random.randrange(0, 2) * 2 - 1 # Bounce back other a bit. Left or right
            if oth.X < 0: # Make sure they don't exit the world.
                oth.X += 2
            if oth.X >= world.WORLD_X:
                oth.X -= 2
    
    def char(this):
        return 'Q'
