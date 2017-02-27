import display
import world

from effects import effect

from objects.Player import attack
from objects.Player import frostshot_obj
from objects import world_object

class freeze(effect.effect):
    def __init__(this, owner):
        super().__init__(owner, float("inf"), "Frostball")

    def tick(this, delta_time):
        super().tick(delta_time)
        if display.keyDown(ord('I')) and (not world.out_of_bounds(this.owner.X, this.owner.Y - 1)):
            world.objects.append(frostshot_obj.frostshot_atk(this.owner.X, this.owner.Y - 1, 0, -1, .5*this.owner.attributes["magic"], 7, 100, this.owner))
            this.time = 0 
        if display.keyDown(ord('J')) and (not world.out_of_bounds(this.owner.X - 1, this.owner.Y)):
            world.objects.append(frostshot_obj.frostshot_atk(this.owner.X - 1, this.owner.Y, -1, 0, .5*this.owner.attributes["magic"], 7, 100, this.owner))
            this.time = 0 
        if display.keyDown(ord('K')) and (not world.out_of_bounds(this.owner.X, this.owner.Y + 1)):
            world.objects.append(frostshot_obj.frostshot_atk(this.owner.X, this.owner.Y + 1, 0, 1, .5*this.owner.attributes["magic"], 7, 100, this.owner))
            this.time = 0 
        if display.keyDown(ord('L')) and (not world.out_of_bounds(this.owner.X + 1, this.owner.Y)):
            world.objects.append(frostshot_obj.frostshot_atk(this.owner.X + 1, this.owner.Y, 1, 0, .5*this.owner.attributes["magic"], 7, 100, this.owner))
            this.time = 0