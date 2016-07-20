name ="Legendary knight leg piece"
type = "Pants"
attributes = {}
def on_equip (this,player):
    player.attributes["maxHP"] += 50
    player.attributes["strength"] += 30
def on_unequip (this, player):
    player.attributes["maxHP"] -= 50
    player.attributes["strength"] -= 30
