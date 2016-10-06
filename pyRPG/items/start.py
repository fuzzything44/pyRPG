from items import item

hat_name    = "No0b hat"
pants_name  = "No0b pants"
ring_name   = "No0b ring"
shirt_name  = "No0b shirt"
weapon_name = "Fists"

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
    "maxHP_mod" : 1      \
  }

pants_attributes = {\
    "luck_mod" : 1 \
  }

ring_attributes = {\
    "maxMP_mod" : 1 \
  }

shirt_attributes = {\
    "maxHP_mod" : 1,    \
    "maxMP_mod" : 1,    \
    "mov_spd_mod" : 1,  \
    "atk_spd_mod" : 1,  \
    "magic_mod" : 1,    \
    "str_mod" : 1,      \
    "luck_mod" : 1      \
  }

weapon_attributes = {\
    "range" : 2,    \
    "damage" : 1    \
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