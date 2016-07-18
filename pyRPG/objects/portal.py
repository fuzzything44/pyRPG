#this does not work at all, I have no clue how to do this
import pickle
from objects import world_object
import objects.player as play

def load(name):
    try:
        with open("res/" + name + ".wrld", "rb") as handle:
            global map, player, objects
            map = pickle.load(handle)
            objects = pickle.load(handle)
            for obj in objects:
                if obj.type == "player":
                    global player
                    player = obj
                    break
    except:
        global map, player, objects
        map = [[ WORLD_NOTHING for y in range(WORLD_Y)] for x in range(WORLD_X)]
        player = world_object.world_object(play.player_update, play.collide, play.player_char, play.player_color, "player", 0, 0, play.player_attributes)
        objects.append(player)

def collide: 
player collides with WORLD_PORTAL:
    draw map 
    set player cords[0][25]