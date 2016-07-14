import time
from random import randrange

import world
import world_object
import invis_dmg
import player
import chest
import display

display.start()


world.player = world_object.world_object(player.player_update, player.collide, player.player_char, player.player_color, 10, 10, player.player_attributes)


world.objects.append(world.player)
world.objects.append(world_object.world_object(invis_dmg.invis_dmg_update, invis_dmg.invis_fire_dmg_collide, invis_dmg.invis_dmg_char, invis_dmg.invis_dmg_color, 10, 15, {"type" : "damage", "name" : "lava"}))
world.objects.append(world_object.world_object(chest.chest_update, chest.chest_collide, chest.chest_char, chest.chest_col, 16, 10, chest.chest_attributes))

# Print world out
for x in range(world.WORLD_X):
    for y in range(world.WORLD_Y):
        display.printc(x, y + 5, world.map[x][y][1], world.map[x][y][0])

# Print top pane
display.printc(5, 0, "HP:")
display.printc(5, 1, "MP:")
display.printc(5, 2, "Gold:")
display.printc(5, 3, "Level")

# Current spell and item border
display.printc(25, 0, "+++++ +++++   Weapon:")
display.printc(25, 1, "+\|/+ +   +   Hat:")
display.printc(25, 2, "+-+-+ +   +   Pants:")
display.printc(25, 3, "+/|\+ +   +   Shoes:")
display.printc(25, 4, "+++++ +++++   Ring:")

start_time = time.time()

while True: # Main game loop
    key = display.getch()

    delta_time = int((time.time() - start_time) * 1000)
    start_time = time.time()
    # Loop through all objects. Update and redraw all of them.
    for index in range(len(world.objects)):
        obj = world.objects[index]
        # Redraw world tile, unless the object is invisible
        if obj.getChar() != '\0':
            display.printc(obj.getCoords()[0], obj.getCoords()[1] + 5, world.map[obj.getCoords()[0]][obj.getCoords()[1]][1], world.map[obj.getCoords()[0]][obj.getCoords()[1]][0])
        # Update it
        obj.update(key, delta_time)
        for coll in world.objects:    # Check for collision
            if (coll.getCoords() == obj.getCoords()) & (not coll is obj) :
                obj.collide(coll)

        #Check if out of bounds
        if (obj.getCoords()[0] >= world.WORLD_X) | (obj.getCoords()[0] < 0) | (obj.getCoords()[1] >= world.WORLD_Y) | (obj.getCoords()[1] < 0):
            world.to_del.append(obj)
        else:
            # And now redraw it
            display.printc(obj.getCoords()[0], obj.getCoords()[1] + 5, obj.getChar(), obj.getColor())
    # Delete objects that need to be deleted.
    for obj in world.to_del:
        try:
            # Don't print too high!
            if (obj.Y < 0):
                obj.Y = 0
            display.printc(obj.X, obj.Y + 5, world.map[obj.X][obj.Y][1], world.map[obj.X][obj.Y][0])
        except: # Deleted for being out of bounds.
            pass
        try:
            world.objects.remove(obj)
        except ValueError:
            pass # Been put in list multiple times.
    world.to_del.clear()
    if key == 27:
        while display.menu("Options:", [[], ["inventory params"], ["Spell Params"], []], ["Resume", lambda: 0], ["Inventory", lambda x: 0], ["Spells", lambda x: 0], ["Exit", display.end]):
            pass

display.end()
