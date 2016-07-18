import display
import world
from objects import world_object
from objects import fireball_obj



def flame(obj, delta_time):
    try:
        if display.keyDown(ord('I')):
            world.objects.append(world_object.world_object(fireball_obj.update, fireball_obj.collide,\
              fireball_obj.char, fireball_obj.color, fireball_obj.type, obj.X, obj.Y + 1,\
              {"to_move": 0,\
               "speed":   40,\
               "movex":   0, \
               "movey":   -1,\
               "range":   7,\
               "owner":   obj,\
               "damage":  1.25*obj.attributes['magic']})) #TODO finish dictionary and copy+paste for other directions