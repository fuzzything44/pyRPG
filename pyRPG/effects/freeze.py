import display
import world

from objects import attack
from objects import frostshot_obj
from objects import world_object


def frost(obj, delta_time):
    try:
        if display.keyDown(ord('I')):
            world.objects.append(world_object.world_object(frostshot_obj.update, frostshot_obj.collide,\
              frostshot_obj.char, frostshot_obj.color, frostshot_obj.type, obj.X, obj.Y - 1,\
              {"to_move": 0,\
               "speed":   100,\
               "movex":   0, \
               "movey":   -1,\
               "range":   7,\
               "owner":   obj,\
               "damage":  1.25*obj.attributes['magic'],}))
            obj.attributes["effects"]["frostshot"][2] -= 1000000 
        if display.keyDown(ord('J')):
            world.objects.append(world_object.world_object(frostshot_obj.update, frostshot_obj.collide,\
              frostshot_obj.char, frostshot_obj.color, frostshot_obj.type, obj.X, obj.Y - 1,\
              {"to_move": 0,\
               "speed":   100,\
               "movex":   0, \
               "movey":   -1,\
               "range":   7,\
               "owner":   obj,\
               "damage":  1.25*obj.attributes['magic'],}))
            obj.attributes["effects"]["frostshot"][2] -= 1000000 
        if display.keyDown(ord('K')):
            world.objects.append(world_object.world_object(frostshot_obj.update, frostshot_obj.collide,\
              frostshot_obj.char, frostshot_obj.color, frostshot_obj.type, obj.X, obj.Y - 1,\
              {"to_move": 0,\
               "speed":   100,\
               "movex":   0, \
               "movey":   -1,\
               "range":   7,\
               "owner":   obj,\
               "damage":  1.25*obj.attributes['magic'],}))
            obj.attributes["effects"]["frostshot"][2] -= 1000000 
        if display.keyDown(ord('L')):
            world.objects.append(world_object.world_object(frostshot_obj.update, frostshot_obj.collide,\
              frostshot_obj.char, frostshot_obj.color, frostshot_obj.type, obj.X, obj.Y - 1,\
              {"to_move": 0,\
               "speed":   100,\
               "movex":   0, \
               "movey":   -1,\
               "range":   7,\
               "owner":   obj,\
               "damage":  1.25*obj.attributes['magic'],}))
            obj.attributes["effects"]["frostshot"][2] -= 1000000 
    except Exception as ex:
        pass