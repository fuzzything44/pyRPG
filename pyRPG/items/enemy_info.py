from items import item
from effects import enemy_info
from objects import world_object

hat_name = "Helm of Knowledge"
pants_name = "Pants of Force"
ring_name = "Ring of Blood"

hat_type = "hat"
pants_type = "pants"
ring_type = "ring"

hat_attributes = {\
    "disp_data" : "Lets you see enemy EXP"    \
  }
pants_attributes = {\
    "disp_data" : "Lets you see enemy strength"    \
  }
ring_attributes = {\
    "disp_data" : "Lets you see enemy HP"    \
  }


# Apply the effect that lets them see EXP
def hat_on_equip(this, player):
    player.attributes["effects"]["see_exp"] = [enemy_info.see_exp, enemy_info.see_exp_off, float("inf")]
def hat_on_unequip(this, player):
    player.attributes["effects"]["see_exp"] = [world_object.no_func, enemy_info.see_exp_off, 0] # No time left on seeing EXP
# Apply the effect that lets them see str
def pants_on_equip(this, player):
    player.attributes["effects"]["see_str"] = [enemy_info.see_str, enemy_info.see_str_off, float("inf")]
def pants_on_unequip(this, player):
    player.attributes["effects"]["see_str"] = [world_object.no_func, enemy_info.see_str_off, 0] # No time left on seeing EXP
# Apply the effect that lets them see HP
def ring_on_equip(this, player):
    player.attributes["effects"]["see_hp"] = [enemy_info.see_hp, enemy_info.see_hp_off, float("inf")]
def ring_on_unequip(this, player):
    player.attributes["effects"]["see_hp"] = [world_object.no_func, enemy_info.see_hp_off, 0] # No time left on seeing HP

