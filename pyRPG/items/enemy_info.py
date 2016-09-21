from items import item
from effects import enemy_info
from objects import world_object

hat_name = ""
pants_name = ""
ring_name = "Stethoscope"
shirt_name = ""
weapon_name = ""

hat_type = "hat"
pants_type = "pants"
ring_type = "ring"
shirt_type = "shirt"
weapon_type = "weapon"

hat_attributes = {\
    "disp_data" : ""    \
  }
pants_attributes = {\
    "disp_data" : ""    \
  }
ring_attributes = {\
    "disp_data" : "Lets you see enemy HP"    \
  }
shirt_attributes = {\
    "disp_data" : ""    \
  }
weapon_attributes = {\
    "disp_data" : ""    \
  }

# Apply the effect that lets them see HP
def stethoscope_equip(this, player):
    player.attributes["effects"]["see_hp"] = [enemy_info.see_hp, enemy_info.see_hp_off, float("inf")]
def stethoscope_unequip(this, player):
    player.attributes["effects"]["see_hp"] = [world_object.no_func, world_object.no_func, 0] # No time left on seeing HP

hat_on_equip = item.reg_equip
hat_on_unequip = item.reg_unequip
pants_on_equip = item.reg_equip
pants_on_unequip = item.reg_unequip
ring_on_equip = stethoscope_equip
ring_on_unequip = stethoscope_unequip
shirt_on_equip = item.reg_equip
shirt_on_unequip = item.reg_unequip
weapon_on_equip = item.reg_equip
weapon_on_unequip = item.reg_unequip