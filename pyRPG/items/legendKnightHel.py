name ="Legendary knights helmet"
type = "hat"
attributes = {}
def on_equip (this,player):
    player.attributes["maxHP"]+30
def on_unequip (this, player):
    player.attributes["maxHP"]-30
