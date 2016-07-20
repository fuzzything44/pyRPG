name ="Dumbledore's pants"
type = "pants"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"]+50, ["maxHP"]+6
def on_unequip (this, player):
    player.attributes["maxMP"]-50, ["maxHP"]-6
