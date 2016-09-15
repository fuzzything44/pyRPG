import copy

from objects import world_object

def make(to_make, x, y, attr = None):
    if attr is None:
        return world_object.world_object(to_make.update, to_make.collide, to_make.char, to_make.color, to_make.type, x, y, copy.deepcopy(to_make.attributes))
    else:
        return world_object.world_object(to_make.update, to_make.collide, to_make.char, to_make.color, to_make.type, x, y, attr)
