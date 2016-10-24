import display
import world

from objects.Player import attack
from objects.Player import frostshot_obj
from objects import world_object


def freeze(obj, delta_time):
    if display.keyDown(ord('I')) and (not world.out_of_bounds(obj.X, obj.Y - 1)):
        world.objects.append(frostshot_obj.frostshot_atk(obj.X, obj.Y - 1, 0, -1, 1.25*obj.attributes["magic"], 7, 100, obj))
        obj.attributes["effects"]["frostshot"][2] = 0 
    if display.keyDown(ord('J')) and (not world.out_of_bounds(obj.X - 1, obj.Y)):
        world.objects.append(frostshot_obj.frostshot_atk(obj.X - 1, obj.Y, -1, 0, 1.25*obj.attributes["magic"], 7, 100, obj))
        obj.attributes["effects"]["forstshot"][2] = 0 
    if display.keyDown(ord('K')) and (not world.out_of_bounds(obj.X, obj.Y + 1)):
        world.objects.append(frostshot_obj.frostshot_atk(obj.X, obj.Y + 1, 0, 1, 1.25*obj.attributes["magic"], 7, 100, obj))
        obj.attributes["effects"]["frostshot"][2] = 0 
    if display.keyDown(ord('L')) and (not world.out_of_bounds(obj.X + 1, obj.Y)):
        world.objects.append(frostshot_obj.frostshot_atk(obj.X + 1, obj.Y, 1, 0, 1.25*obj.attributes["magic"], 7, 100, obj))
        obj.attributes["effects"]["frostshot"][2] = 0