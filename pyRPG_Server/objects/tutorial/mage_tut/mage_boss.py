import math
import random

import world

from effects import effect

from items import t1_consumables
from items import tutorial_quest_items

from objects import world_object
from objects import General

from objects.tutorial.mage_tut import directed_attack
from objects.tutorial.mage_tut import boss_slime

class mage_boss(General.enemy_base.enemy_base):
    def __init__(this, posX, posY, owner):
        super().__init__(posX, posY, 300, 25, 15, 10, [\
            (tutorial_quest_items.any_rare_reward(1), 500),   \
            (tutorial_quest_items.mage_rare_reward(1), 10), \
            (t1_consumables.t1_mana(5), 20),    \
            (t1_consumables.t1_mana(5), 20),    \
            (t1_consumables.t1_mana(5), 20),    \
            (t1_consumables.t1_mana(5), 20),    \
            (t1_consumables.t1_mana(5), 20)     \
          ], owner)
        this.attributes["go_diag"] = False
        this.attributes["going_to"] = (this.X, this.Y)

    def update(this, delta_time):
        super().update(delta_time)

        # Attack
        if "atk_del" not in this.attributes["effects"]:
            if this.attributes["go_diag"]:
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 1 , 1 , 200, False))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 1 , -1, 200, False))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, -1, 1 , 200, False))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, -1, -1, 200, False))
            else:                                                                                                                
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 1 , 0 , 100, False))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, -1, 0 , 100, False))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 0 , 1 , 100, False))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 0 , -1, 100, False))
            this.attributes["go_diag"] = not this.attributes["go_diag"]
            this.attributes["effects"]["atk_del"] = effect.effect(this, 500)

        # Move
        if "mov_del" not in this.attributes["effects"]:
            if (this.X, this.Y) == this.attributes["going_to"]: # If we're where we want to be, choose new location to go.
                this.attributes["going_to"] = (random.randint(0, world.WORLD_X - 1), random.randint(0, world.WORLD_Y - 1))

                if (this.X, this.Y) == this.attributes["going_to"]: # If we randomized to same coord.
                    this.attributes["going_to"] = (25, 10) # Just move to middle
                    if (this.X, this.Y) == this.attributes["going_to"]: # If it already was in the middle and we randomized middle
                        this.attributes["going_to"] = (15, 7) # Go wherever.

            dist_x = 0
            dist_y = 0
            if this.X == this.attributes["going_to"][0]: # Move on y
                dist_y = this.attributes["going_to"][1] - this.Y
                dist_y = dist_y / abs(dist_y)
            else:
                dist_x = this.attributes["going_to"][0] - this.X
                dist_x = dist_x / abs(dist_x)

            # Now we actually move
            world.objects.append(boss_slime.boss_slime(this.X, this.Y, this))
            this.X += int(dist_x)
            this.Y += int(dist_y)
            this.attributes["effects"]["mov_del"] = effect.effect(this, 300)


    def collide(this, obj):
        if (not this.team & obj.team) and ("HP" in obj.attributes) and (obj.attributes["name"] + "-attack-del" not in this.attributes["effects"]): 
            # If collides with something, damage it. Wait to damage again for 500ms
            obj.attributes["HP"] -= this.attributes["damage"]
            this.attributes["effects"][obj.attributes["name"] + "-attack-del"] = effect.effect(this, 500)

    def char(this):
        return 'B'




