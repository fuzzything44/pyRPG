import math
import random

import world

from effects import effect

from items import t1_consumables
from items import tutorial_quest_items

from objects import world_object
from objects import General

from objects.tutorial.mage_tut import directed_attack

class adv_mage_enemy(General.enemy_base.enemy_base):
    """Stays still, shoots up/down/left/right at even intervals"""
    def __init__(this, posX, posY, spawner):
        super().__init__(posX, posY, 16, 15, 3, 0, [(t1_consumables.t1_mana(), 50), (tutorial_quest_items.mage_quest_item(), 100)], spawner)
        this.attributes.update({\
                "theta" : random.randrange(0, 10),
                "radius" : 4    \
            })

    def update(this, delta_time):
        super().update(delta_time)

        # Move
        this.attributes["theta"] += (delta_time * .002 / this.attributes["radius"])   
        this.X = int(this.attributes["radius"] * math.cos(this.attributes["theta"]) + this.attributes["spawner"].X)
        this.Y = int(this.attributes["radius"] * math.sin(this.attributes["theta"]) + this.attributes["spawner"].Y)
        if this.X < 0:
            this.X = 0
        if this.X >= world.WORLD_X:
            this.X = world.WORLD_X - 1
        if this.Y < 0:
            this.Y = 0
        if this.Y >= world.WORLD_Y:
            this.Y = world.WORLD_Y - 1


        # Attack
        if "atk_del" not in this.attributes["effects"]:
            closest_player = None
            dist = float("Inf")
            for plr in world.players: # Find closest player
                if (this.X - plr.X) ** 2 + (this.Y - plr.Y) ** 2 < dist:
                    closest_player = plr
                    dist = (this.X - plr.X) ** 2 + (this.Y - plr.Y) ** 2
            if closest_player is not None:
                x_dist = this.X - closest_player.X 
                y_dist = this.Y - closest_player.Y 
                x_mov = 0
                y_mov = 0
                if abs(x_dist) > abs(y_dist):
                    x_mov =  -1 if x_dist > 0 else 1
                else:
                    y_mov =  -1 if y_dist > 0 else 1

                world.objects.append(directed_attack.directed_attack(this.X + x_mov, this.Y + y_mov, this.attributes["damage"], this, x_mov, y_mov, 150, True, 10))
            this.attributes["effects"]["atk_del"] = effect.effect(this, 1000)
            

    def char(this):
        return 'W'




