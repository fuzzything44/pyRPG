from items import item
from effects import enemy_info
from objects import world_object

class info_hat(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Helm of Knowledge", "hat", 0, quantity, {"disp_data" : "Lets you see enemy EXP"})
    # Apply the effect that lets them see EXP
    def equip(this, player):
        player.attributes["effects"]["see_exp"] = [enemy_info.see_exp, enemy_info.see_exp_off, float("inf")]
    def unequip(this, player):
        player.attributes["effects"]["see_exp"] = [world_object.no_func, enemy_info.see_exp_off, 0] # No time left on seeing EXP
    

class info_pants(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Pants of Force", "pants", 0, quantity, {"disp_data" : "Lets you see enemy strength"})
    # Apply the effect that lets them see str
    def pants_on_equip(this, player):
        player.attributes["effects"]["see_str"] = [enemy_info.see_str, enemy_info.see_str_off, float("inf")]
    def pants_on_unequip(this, player):
        player.attributes["effects"]["see_str"] = [world_object.no_func, enemy_info.see_str_off, 0] # No time left on seeing EXP

class info_ring(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Ring of Blood", "ring", 0, quantity, {"disp_data" : "Lets you see enemy strength"})
    # Apply the effect that lets them see HP
    def ring_on_equip(this, player):
        player.attributes["effects"]["see_hp"] = [enemy_info.see_hp, enemy_info.see_hp_off, float("inf")]
    def ring_on_unequip(this, player):
        player.attributes["effects"]["see_hp"] = [world_object.no_func, enemy_info.see_hp_off, 0] # No time left on seeing HP

