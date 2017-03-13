import random

import display
import world

from objects import world_object
from objects.Loot import lootbag
from objects.Loot import money

class enemy_base(world_object.world_object):
    """Basic enemy. Checks for death, defines color."""
    def __init__(this, posX, posY, health = 1, damage = 1, exp = 1, money = 0, drops = [], spawner = None):
        """Parameters:
            posX: The X position of the enemy.
            posY: The Y position of the enemy.
            health: The health of the enemy.
            damage: How much damage the enemy does.
            exp: How much EXP is granted to player on death.
            money: How much money is dropped. Can be up to 10% greater after luck mods.
            drops: A list of [item, int]. Gives an int percent chance to drop item. 100% drops are unaffected by luck.
"""
        super().__init__(posX, posY, "enemy", world_object.TEAM_ENEMY)
        this.attributes.update({"HP" : health, "damage" : damage, "EXP" : exp, "money" : money, "items" : drops, "effects" : {}, "dmg_dist" : {}, "spawner" : spawner})

    def update(this, delta_time):
        "Updates effects. Checks if dead. If so, dies."
        # Update all effects.
        eff_del_list = []
        for eff_name in this.attributes["effects"]:
            eff = this.attributes["effects"][eff_name]
            eff.tick(delta_time)  # Tick effect
            if eff.time <= 0:           # Remove effect
                eff_del_list.append(eff_name)
        for eff_name in eff_del_list:
            this.attributes["effects"][eff_name].uneffect(this)
            del this.attributes["effects"][eff_name]
        del eff_del_list
        # Check if dead.
        if this.attributes["HP"] <= 0: # TODO: bring back to normal
            this.die()

    def color(this):
        "Returns cyan. DO NOT CHANGE!"
        return display.CYAN

    def char(this):
        return 'Q'

    def die(this):
        "Deletes this, gives player EXP, drops money, drops items."
        world.to_del.append(this) # Delete
        if this.attributes["spawner"] is not None:
            this.attributes["spawner"].attributes["current_enemy"] = None # Tell spawner we died.

        for plr in this.attributes["dmg_dist"]:
            plr.attributes["gainexp"](plr, this.attributes["EXP"])

        # Drop money. Dropped is their luck times the drop amount plus 0-10%.
        if this.attributes["money"] > 0:
            world.objects.append(money.money(this.X, this.Y, this.attributes["money"]))

        # Drop items
        # What priority players get drops in
        drop_priority = sorted(this.attributes["dmg_dist"], key=this.attributes["dmg_dist"].get, reverse=True)

        if len(drop_priority) == 0:
            return # Don't drop stuff if no one killed
        # What drops each player gets
        drops = [[] for x in range(len(drop_priority))]
        # Where we are in the priority list
        priority_index = 0
        for drop in this.attributes["items"]:
            print("Rolling drop...", drop)
            # Roll die, see if it drops
            if random.randrange(0, 100) < (drop[1] * (1.0 + drop_priority[priority_index].attributes["luck"] / 100)):
                drops[priority_index].append(drop[0]) # They got the item!
            priority_index += 1
            if priority_index >= len(drop_priority):
                priority_index = 0

        for ind in range(len(drop_priority)): # For all players that damaged...
            world.objects.append(lootbag.lootbag(this.X, this.Y, drop_priority[ind], drops[ind])) # Give drops

