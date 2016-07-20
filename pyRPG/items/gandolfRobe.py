name ="Gandolf's robe"
type = "shirt"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"] += 60
    player.attributes["maxHP"] += 40
    player.attributes["magic"] += 50
def on_unequip (this, player):
    player.attributes["maxMP"] -= 60
    player.attributes["maxHP"] -= 40
    player.attributes["magic"] -= 50
