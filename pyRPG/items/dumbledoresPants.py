name ="Dumbledore's pants"
type = "pants"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"] += 50
    player.attributes["maxHP"] += 30
    player.attributes["magic"] += 40
def on_unequip (this, player):
    player.attributes["maxMP"] -= 50
    player.attributes["maxHP"] -= 30
    player.attributes["magic"] -= 40
