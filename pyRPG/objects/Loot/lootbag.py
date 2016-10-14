import display
import world

from objects.Loot import chest

class lootbag(chest.chest):
    def update(this, delta_time):
        if len(this.attributes["contents"]) == 0:
            world.to_del.append(this)

    def char(this):
        return 'L'
    
    def color(this):
        return display.YELLOW
    