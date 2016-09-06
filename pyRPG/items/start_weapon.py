from items import item

name = "Your fists"
type = "weapon"

attributes = {\
    "range" : 2,    \
    "damage" : 1    \
  }

on_equip = item.reg_equip
on_unequip = item.reg_unequip