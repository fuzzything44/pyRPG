from items import item

hat_name = "Fedora"
pants_name = "Skinny Jeans"
ring_name = "Iron Ring"
shirt_name = "\"I'm with stupid\" shirt"
weapon_name = "Orange Mocha Frappuccino"

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
    "maxHP_mod" : 5,    \
    "atk_spd_mod" : 5   \
  }
pants_attributes = {\
    "maxHP_mod" : 10,   \
    "mov_spd_mod" : 10  \
  }
ring_attributes = {\
    "luck_mod" : 5,     \
    "str_mod" : 7       \
  }
shirt_attributes = {\
    "maxHP_mod" : 10,   \
    "luck_mod" : 5      \
  }
weapon_attributes = {\
    "range" : 2,        \
    "damage" : 7        \
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