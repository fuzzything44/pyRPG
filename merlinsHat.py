name ="Merlin's hat"
type = "hat"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"]+30, ["maxHP"]+3
def on_unequip (this, player):
    player.attributes["maxMP"-30, ["maxHP"]-3
