import copy

import world
from objects import lock_portal
from objects import tutorial_enemy
from objects import world_object

def generate():
    world.objects = []
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]    
    world.objects.append(world_object.world_object(lock_portal.update, lock_portal.collide, lock_portal.char, lock_portal.color, lock_portal.type, 49,10,{"newmap": "tutboss", "locx": 0, "locy": 10, "used" : False}))     
    world.objects.append(world_object.world_object(tutorial_enemy.update, tutorial_enemy.collide, tutorial_enemy.char, tutorial_enemy.color, tutorial_enemy.type, 25, 10, tutorial_enemy.attributes))
    
    # Tutorial messages in the map. How to attack, what enemies are
    message =  "This is an enemy. Attack it to kill it."
    message2 = "Use IJKL to attack"
    for index in range(len(message)):
        # The index + 5 centers the message. The 9 is the line right above the enemy.
        world.map[index + 5][9] = [0, message[index], True]
    for index in range(len(message2)):
        # A shorter message needs to have a larger number added to center
        world.map[index + 16][11] = [0, message2[index], True]
    for index in range(world.WORLD_X):
        world.map[index][7] = world.WORLD_WALL
    # Draw arrows pointing to the enemy. Locations are next to the enemy
    world.map[23][10] = [0, '>', True]
    world.map[27][10] = [0, '<', True]
       
    
