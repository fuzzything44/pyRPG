import display
import world

from objects.LavaDungeon import reset_lever
from objects.General import lever

bridge_pos = [(11, 10), (12, 10), (13, 10), (14, 10), (15, 10), (16, 10), (16, 11), (17, 11), (18, 11), (19, 11), (20, 11), (21, 11), (22, 11), (23, 11), (24, 11), (25, 11), (26, 11), (27, 11), (28, 11), (29, 11)]

class bridge_lever(lever.lever):
    def __init__(this, posX, posY, ):
        super().__init__(posX, posY, remove_bridge, make_bridge)

def remove_bridge(lever):
    for elem in bridge_pos:
        world.map[elem[0]][elem[1]] = [display.RED, display.RED, '#', True]
    for obj in world.objects:
        if obj.type == "timer-lever":
            world.to_del.append(obj)
    world.dispworld()

def make_bridge(lever):
    for elem in bridge_pos:
        world.map[elem[0]][elem[1]] = [display.WHITE, display.BLACK, '=', True]
    # Add timer to reset lever
    world.objects.append(reset_lever.reset_lever(15000, lever, 0))
    world.dispworld()