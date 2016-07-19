name ="Legendary knight chest piece"
type = "shirt"
attributes = {}
def on_equip (this,player):
    player.attributes["maxHP"]+50
def on_unequip (this, player):
    player.attributes["maxHP"]-50
