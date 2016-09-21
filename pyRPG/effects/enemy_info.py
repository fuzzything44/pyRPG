import display
from objects import world_object
import world

def see_hp(obj, delta_time):
    # First, find closest enemy
    closest_enemy = None
    closest_dist_sq = float("inf")
    for other in world.objects:
        if other.type == "enemy": # If they're an enemy...
            dist_sq = (obj.X - other.X)**2 + (obj.Y - other.Y)**2 # Find distance
            if dist_sq < closest_dist_sq: # If this one is closer
                closest_enemy = other     # Now it's the one we check with
                closest_dist_sq = dist_sq
    # Now re-print enemy HP. So HP + spaces equal to extra space
    if closest_enemy is not None:
        hp_str = str(int(closest_enemy.attributes["HP"]))
        spaces_str = ' ' * (33 - len(hp_str))
        str_to_print = hp_str + spaces_str
    else:
        str_to_print = "No enemies nearby                "
    display.printc(44, 4, str_to_print)
        

see_hp_off = world_object.no_func