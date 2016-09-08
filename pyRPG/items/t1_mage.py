from items import item

hat_name = "Magical hat"
pants_name = "Pants of Power"
ring_name = "Cubic Zirconium Ring"
shirt_name = "White shirt"
weapon_name = "Aluminum wand"

hat_type = "hat"
pants_type = "pants"
ring_type = "ring"
shirt_type = "shirt"
weapon_type = "weapon"

hat_attributes = {\
    "maxMP_mod" : 10    \
  }
pants_attributes = {\
    "maxMP_mod" : 15    \
  }
ring_attributes = {\
    "maxMP_mod" : 5,    \
    "magic_mod" : 5,      \
  }
shirt_attributes = {\
    "maxMP_mod" : 25    \
  }
weapon_attributes = {\
    "range" : 7,        \
    "damage" : 5        \
  }

hat_on_equip = item.reg_equip
hat_on_unequip = item.reg_unequip
pants_on_equip = item.reg_equip
pants_on_unequip = item.reg_unequip
ring_on_equip = item.reg_equip
ring_on_unequip = item.reg_unequip
shirt_on_equip = item.reg_equip
shirt_on_unequip = item.reg_unequip
weapon_on_equip = item.reg_equip
weapon_on_unequip = item.reg_unequip