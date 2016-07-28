from random import randrange

import display
import world

from items import item
from items import bread
from objects import attack
from objects import chest
from objects import money
from objects import world_object
from spells import spell

def update(this, delta_time):
    eff_del_list = []
    for eff in this.attributes["effects"]:
        this.attributes["effects"][eff][0](this, delta_time)       # Tick code
        this.attributes["effects"][eff][2] -= delta_time           # Lower time
        if this.attributes["effects"][eff][2] <= 0:                # Remove effect
            eff_del_list.append(eff)
    for to_del in eff_del_list:
        this.attributes["effects"][to_del][1](this)
        del this.attributes["effects"][to_del]
    del eff_del_list
    if this.attributes["HP"] <= 0:
        world.to_del.append(this)
        chest_attr = {"canopen" : False, "contents": [item.item(bread.name, bread.type, bread.equip, bread.unequip, 10, bread.attributes)]}
        world.map[25][10] = world.WORLD_CHEST
        display.printc(25, 15, '@', display.YELLOW)
        # Add actual chests
        world.objects.append(world_object.world_object(chest.chest_update, chest.chest_collide, chest.chest_char, chest.chest_col, chest.chest_type, 24, 10, chest_attr))
        world.objects.append(world_object.world_object(chest.chest_update, chest.chest_collide, chest.chest_char, chest.chest_col, chest.chest_type, 26, 10, chest_attr))
        world.objects.append(world_object.world_object(chest.chest_update, chest.chest_collide, chest.chest_char, chest.chest_col, chest.chest_type, 25, 9, chest_attr))
        world.objects.append(world_object.world_object(chest.chest_update, chest.chest_collide, chest.chest_char, chest.chest_col, chest.chest_type, 25, 11, chest_attr))
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give experience
    else:        
        if randrange(0, this.attributes["mov_spd"]) < delta_time:  
            newX = this.X + randrange(-1, 2)
            newY = this.Y + randrange(-1, 2)
            # Don't walk out of bounds or on a wall...
            if (newX >= 0) and (newX < world.WORLD_X) and (newY >= 0) and (newY < world.WORLD_Y) and (world.map[newX][newY][2]):
                this.X = newX
                this.Y = newY

def collide(this, obj):
    if obj.type == "player":
        obj.attributes["HP"] -= this.attributes["damage"]
        this.X += 1
        if this.X == world.WORLD_X:
            this.X = 0


def color(this):
  return display.CYAN

def char(this):
  return 'B'

type = "enemy"

attributes =                     \
    { "HP" : 100.0,                     \
      "MP" : 50,                        \
      "effects" : {},                   \
      "mov_spd" : 200,                    \
      "atk_spd" : 150,                   \
      "damage" : 10,                      \
      "EXP" : 5
    }