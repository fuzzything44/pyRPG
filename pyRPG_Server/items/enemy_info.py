from items import item
from effects import enemy_info
from objects import world_object
from effects import enemy_info

class info_hat(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Helm of Knowledge", "hat", "This is actually a monocle.",0, quantity, {"disp_data" : "Lets you see enemy EXP"})
    # Apply the effect that lets them see EXP
    def equip(this, player):
        player.attributes["effects"]["see_exp"] = enemy_info.see_exp(player, float("inf"))
    def unequip(this, player):
        del player.attributes["effects"]["see_exp"]
    

class info_pants(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Pants of Force", "pants", "Everyone needs a good pair of\n magical pants.", 0, quantity, {"disp_data" : "Lets you see enemy strength"})
    # Apply the effect that lets them see str
    def pants_on_equip(this, player):
        player.attributes["effects"]["see_str"] = enemy_info.see_str(player, float("inf"))
    def pants_on_unequip(this, player):
        del player.attributes["effects"]["see_str"]

class info_ring(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Ring of Blood", "ring", "Don't ask how this works.\n You don't want to know.", 0, quantity, {"disp_data" : "Lets you see enemy strength"})
    # Apply the effect that lets them see HP
    def ring_on_equip(this, player):
        player.attributes["effects"]["see_hp"] = enemy_info.see_hp(player, float("inf"))
    def ring_on_unequip(this, player):
        del player.attributes["effects"]["see_hp"]

