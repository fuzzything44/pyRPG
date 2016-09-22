import display
from objects import world_object
import world

def see_exp(obj, delta_time):
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
    if (closest_enemy is not None) and ("EXP" in closest_enemy.attributes):
        exp_str = "EXP:" + str(int(closest_enemy.attributes["EXP"]))
        spaces_str = ' ' * (34 - len(exp_str))
        str_to_print = exp_str + spaces_str
    else:
        str_to_print = "No enemies nearby                 "
    display.printc(display.HAT_X, display.HAT_Y, str_to_print)
        

see_exp_off = world_object.no_func

def see_str(obj, delta_time):
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
    if (closest_enemy is not None) and ("damage" in closest_enemy.attributes):
        str_str = "Strength:" + str(int(closest_enemy.attributes["damage"]))
        spaces_str = ' ' * (32 - len(str_str))
        str_to_print = str_str + spaces_str
    else:
        str_to_print = "No enemies nearby               "
    display.printc(display.PANTS_X, display.PANTS_Y, str_to_print)
        

see_str_off = world_object.no_func

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
    if (closest_enemy is not None) and ("HP" in closest_enemy.attributes):
        hp_str = "HP:" + str(int(closest_enemy.attributes["HP"]))
        spaces_str = ' ' * (33 - len(hp_str))
        str_to_print = hp_str + spaces_str
    else:
        str_to_print = "No enemies nearby                "
    display.printc(display.RING_X, display.RING_Y, str_to_print)
        

see_hp_off = world_object.no_func

