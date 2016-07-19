name ="Magic shoes"
type = "shoes"
attributes = {}
def on_equip (this,player):
    player.attributes["magic"] += 2
def on_unequip (this, player):
    player.attributes["magic"] -= 2
