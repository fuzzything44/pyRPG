import display
import world

from objects import attack
from objects import fireball_obj
from objects import world_object


def flame(obj, delta_time):
    if display.keyDown(ord('I')) and (not world.out_of_bounds(obj.X, obj.Y - 1)):
        world.objects.append(world_object.world_object(fireball_obj.update, fireball_obj.collide,\
          fireball_obj.char, fireball_obj.color, fireball_obj.type, obj.X, obj.Y - 1,\
          {"to_move": 0,\
           "speed":   100,\
           "movex":   0, \
           "movey":   -1,\
           "range":   7,\
           "owner":   obj,\
           "damage":  1.25*obj.attributes['magic']}))
        obj.attributes["effects"]["fireball"][2] -= 1000000 
    if display.keyDown(ord('J')) and (not world.out_of_bounds(obj.X - 1, obj.Y)):
        world.objects.append(world_object.world_object(fireball_obj.update, fireball_obj.collide,\
          fireball_obj.char, fireball_obj.color, fireball_obj.type, obj.X - 1, obj.Y,\
          {"to_move": 0,\
           "speed":   100,\
           "movex":   -1, \
           "movey":   0,\
           "range":   7,\
           "owner":   obj,\
           "damage":  1.25*obj.attributes['magic']}))
        obj.attributes["effects"]["fireball"][2] -= 1000000 
    if display.keyDown(ord('K')) and (not world.out_of_bounds(obj.X, obj.Y + 1)):
        world.objects.append(world_object.world_object(fireball_obj.update, fireball_obj.collide,\
          fireball_obj.char, fireball_obj.color, fireball_obj.type, obj.X, obj.Y + 1,\
          {"to_move": 0,\
           "speed":   100,\
           "movex":   0, \
           "movey":   +1,\
           "range":   7,\
           "owner":   obj,\
           "damage":  1.25*obj.attributes['magic']}))
        obj.attributes["effects"]["fireball"][2] -= 1000000 
    if display.keyDown(ord('L')) and (not world.out_of_bounds(obj.X + 1, obj.Y)):
        world.objects.append(world_object.world_object(fireball_obj.update, fireball_obj.collide,\
          fireball_obj.char, fireball_obj.color, fireball_obj.type, obj.X + 1, obj.Y,\
          {"to_move": 0,\
           "speed":   100,\
           "movex":   1, \
           "movey":   0,\
           "range":   7,\
           "owner":   obj,\
           "damage":  1.25*obj.attributes['magic']}))
        obj.attributes["effects"]["fireball"][2] -= 1000000