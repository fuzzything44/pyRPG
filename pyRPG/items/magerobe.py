name ="Mage's Robe"
type = "shirt"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"] += 10
    player.attributes["magic"] += 10
    player.attributes["maxHP"] += 5
def on_unequip (this, player):
    player.attributes["maxMP"] -= 10
    player.attributes["maxHP"] -= 5
    player.attributes["magic"] -=10
