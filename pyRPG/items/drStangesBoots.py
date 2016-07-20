name ="Dr. Strange's boots"
type = "shoes"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"] += 30 
    player.attributes["maxHP"] += 10
    player.attributes["magic"] += 10
def on_unequip (this, player):
    player.attributes["maxMP"] -= 30
    player.attributes["maxHP"] -= 10
    player.attributes["magic"] -= 10
