from items import item

hat_name = "Iron Helmet"
pants_name = "Iron Leggings"
ring_name = "Iron Ring"
shirt_name = "Iron Breastplate"
weapon_name = "Iron Longsword"

hat_type = "hat"
pants_type = "pants"
ring_type = "ring"
shirt_type = "shirt"
weapon_type = "weapon"

hat_value = 0
pants_value = 0
ring_value = 0
shirt_value = 0
weapon_value = 0

hat_attributes = {\
    "maxHP_mod" : 10    \
  }
pants_attributes = {\
    "maxHP_mod" : 15    \
  }
ring_attributes = {\
    "maxHP_mod" : 5,    \
    "str_mod" : 5,      \
  }
shirt_attributes = {\
    "maxHP_mod" : 25    \
  }
weapon_attributes = {\
    "range" : 3,        \
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