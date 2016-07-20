import world
from objects import *

def generate():
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
    world.objects = []
    world.objects.append(world_object.world_object(MiniBoss.MiniBoss_update, MiniBoss.MiniBosscollide, MiniBoss.MiniBossChar, MiniBoss.MiniBossColor, MiniBoss.MiniBoss_type, 25, 10, dict(MiniBoss.MiniBoss_attributes)))
