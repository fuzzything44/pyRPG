name ="okay ring"
type = "ring"
attributes = {}
def on_equip (this,player):
    player.attributes["magic"] += 8
def on_unequip (this, player):
    player.attributes["magic"] -= 8
