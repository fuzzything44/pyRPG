name ="Dr. Strange's boots"
type = "shoes"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"]+30, ["maxHP"]+3
def on_unequip (this, player):
    player.attributes["maxMP"]-8, ["maxHP"]-3
