import display
import world

from effects import effect

from objects.Player import fireball_obj
from objects import world_object

class flame(effect.effect):
    def __init__(self, owner):
        super().__init__(owner, 1)

    def tick(this, delta_time):
        if display.keyDown(ord('I')) and (not world.out_of_bounds(this.owner.X, this.owner.Y - 1)):
            world.objects.append(fireball_obj.fireball_atk(this.owner.X, this.owner.Y - 1, 0, -1, 1.25*this.owner.attributes["magic"], 7, 100, this.owner))
            this.time = 0
        if display.keyDown(ord('J')) and (not world.out_of_bounds(this.owner.X - 1, this.owner.Y)):
            world.objects.append(fireball_obj.fireball_atk(this.owner.X - 1, this.owner.Y, -1, 0, 1.25*this.owner.attributes["magic"], 7, 100, this.owner))
            this.time = 0 
        if display.keyDown(ord('K')) and (not world.out_of_bounds(this.owner.X, this.owner.Y + 1)):
            world.objects.append(fireball_obj.fireball_atk(this.owner.X, this.owner.Y + 1, 0, 1, 1.25*this.owner.attributes["magic"], 7, 100, this.owner))
            this.time = 0 
        if display.keyDown(ord('L')) and (not world.out_of_bounds(this.owner.X + 1, this.owner.Y)):
            world.objects.append(fireball_obj.fireball_atk(this.owner.X + 1, this.owner.Y, 1, 0, 1.25*this.owner.attributes["magic"], 7, 100, this.owner))
            this.time = 0