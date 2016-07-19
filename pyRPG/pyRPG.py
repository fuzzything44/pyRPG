import time

import world
from objects import world_object
from objects import invis_dmg
from objects import player
from objects import chest
from objects import enemy
from objects import portal
import display
import main_menu
import map2

display.start()
main_menu.start()
# Title menu!
# Needs world selection menu. Probably try for a scrolling menu with basic graphics if possible.


world.load("test_worlda")
world.load_player("notasave")
try:
    map2.generate()
except Exception as ex:
    pass
world.save("test_world")

#world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]
#world.map[2][3] = world.WORLD_CHEST
#world.objects.append(world_object.world_object(enemy.enemy_update, enemy.enemy_collide, enemy.enemyChar, enemy.enemyColor, enemy.enemy_type, 7, 7, enemy.enemy_attributes))
#world.objects.append(world_object.world_object(chest.chest_update, chest.chest_collide, chest.chest_char, chest.chest_col, chest.chest_type, 3, 3, chest.chest_attributes))
#world.objects.append(world_object.world_object(portal.update, portal.collide, portal.char, portal.color, portal.type, 0,10,{"newmap": "test_world", "locx": 25, "locy": 10}))
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
display.printc(display.SPELL_BOX_START, 0, "+++++ +++++   Weapon:")
display.printc(display.SPELL_BOX_START, 1, "+   + +   +   Hat:")
display.printc(display.SPELL_BOX_START, 2, "+   + +   +   Shirt:")
display.printc(display.SPELL_BOX_START, 3, "+   + +   +   Pants:")
display.printc(display.SPELL_BOX_START, 4, "+++++ +++++   Ring:")


start_time = time.time()

while True: # Main game loop
    # Refresh screen
    display.refresh()

    delta_time = int((time.time() - start_time) * 1000)
    if delta_time > 20:
        delta_time = 5
    start_time = time.time()
    # Loop through all objects. Update and redraw all of them.
    for index in range(len(world.objects)):
        obj = world.objects[index]
        # Redraw world tile, unless the object is invisible
        if obj.getChar() != '\0':
            display.printc(obj.getCoords()[0], obj.getCoords()[1] + 5, world.map[obj.getCoords()[0]][obj.getCoords()[1]][1], world.map[obj.getCoords()[0]][obj.getCoords()[1]][0])
        # Update it
        obj.update(delta_time)
        for coll in world.objects:    # Check for collision
            if (coll.getCoords() == obj.getCoords()) and (not coll is obj) :
                obj.collide(coll)

        #Check if out of bounds
        if (obj.getCoords()[0] >= world.WORLD_X) or (obj.getCoords()[0] < 0) or (obj.getCoords()[1] >= world.WORLD_Y) or (obj.getCoords()[1] < 0):
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
    if display.keyDown(display.CONST.VK_ESCAPE):
        while display.menu("Options:", [[], [], ["spell"], []], ["Resume", lambda: 0], ["Inventory", player.inventory_menu], ["Spells", player.set_active], ["Exit", display.end]):
            world.player.attributes["spell"].draw()
            try:
                world.player.attributes["consumable"].attributes["draw"]()
            except:
                pass
            display.refresh()
        