import display
import world

from objects.Player import attack
from objects.Player import frostshot_obj
from objects import world_object


def freeze(obj, delta_time):
    if display.keyDown(ord('I')) and (obj.Y != 0) and (world.map[obj.X][obj.Y - 1][2]) :
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
    if display.keyDown(ord('J')) and (obj.X != 0) and (world.map[obj.X - 1][obj.Y][2]):
        world.objects.append(world_object.world_object(frostshot_obj.update, frostshot_obj.collide,\
          frostshot_obj.char, frostshot_obj.color, frostshot_obj.type, obj.X - 1, obj.Y,\
          {"to_move": 0,\
           "speed":   100,\
           "movex":   -1, \
           "movey":   0,\
           "range":   7,\
           "owner":   obj,\
           "damage":  1.25*obj.attributes['magic'],}))
        obj.attributes["effects"]["frostshot"][2] -= 1000000 
    if display.keyDown(ord('K')) and (obj.Y != 19) and (world.map[obj.X][obj.Y + 1][2]):
        world.objects.append(world_object.world_object(frostshot_obj.update, frostshot_obj.collide,\
          frostshot_obj.char, frostshot_obj.color, frostshot_obj.type, obj.X, obj.Y + 1,\
          {"to_move": 0,\
           "speed":   100,\
           "movex":   0, \
           "movey":   1,\
           "range":   7,\
           "owner":   obj,\
           "damage":  1.25*obj.attributes['magic'],}))
        obj.attributes["effects"]["frostshot"][2] -= 1000000 
    if display.keyDown(ord('L')) and (obj.X != 49) and (world.map[obj.X + 1][obj.Y][2]):
        world.objects.append(world_object.world_object(frostshot_obj.update, frostshot_obj.collide,\
          frostshot_obj.char, frostshot_obj.color, frostshot_obj.type, obj.X + 1, obj.Y,\
          {"to_move": 0,\
           "speed":   100,\
           "movex":   1, \
           "movey":   0,\
           "range":   7,\
           "owner":   obj,\
           "damage":  1.25*obj.attributes['magic'],}))
        obj.attributes["effects"]["frostshot"][2] -= 1000000 
