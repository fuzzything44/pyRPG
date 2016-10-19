import random

import display
import world

from objects import world_object
from objects.Loot import lootbag
from objects.Loot import money

class enemy_base(world_object.world_object):
    def __init__(this, posX, posY, health = 1, damage = 1, exp = 1, money = 0, drops = []):
        super().__init__(posX, posY, "enemy")
        this.attributes.update({"HP" : health, "damage" : damage, "EXP" : exp, "money" : money, "items" : drops})

    def update(this, delta_time):
        if this.attributes["HP"] <= 0:
            this.die()

    def color(this):
        return display.CYAN

    def die(this):
        world.to_del.append(this) # Delete
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give exp

        # Drop money. Dropped is their luck times the drop amount plus 0-10%.
        moneydrop = int(.01*this.attributes["money"]*(100 + world.player.attributes["luck"])*(1 + 0.1*random.randrange(0, 10)))
        if moneydrop > 0:
            world.objects.append(money.money(this.X, this.Y, moneydrop))

        # Drop items
        dropped_items = []
        for drop in this.attributes["items"]:
            # Roll die, see if it drops
            if randrange(0, 100) < (drop[1] * (1.0 + world.player.attributes["luck"] / 100)):
                dropped_items.append(drop[0]) # They got the item!
        if len(dropped_items) > 0:
            world.objects.append(obj_maker.make(lootbag, this.X, this.Y, {"contents" : dropped_items}))

