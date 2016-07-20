name ="Legendary knight chest piece"
type = "shirt"
attributes = {}
def on_equip (this,player):
    player.attributes["maxHP"] += 50
    player.attributes["strength"] += 40
def on_unequip (this, player):
    player.attributes["maxHP"] -= 50
    player.attributes["strength"] -= 40
