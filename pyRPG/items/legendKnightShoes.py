name ="Legendary knight shoes"
type = "shoes"
attributes = {}
def on_equip (this,player):
    player.attributes["maxHP"] += 30
    player.attributes["strength"] += 15
def on_unequip (this, player):
    player.attributes["maxHP"] -= 30
    player.attributes["strength"] -= 15
