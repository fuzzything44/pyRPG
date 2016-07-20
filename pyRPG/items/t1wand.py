name = "Wand"
type = "weapon"
attributes = { "damage" : 3, "range": 10}
def on_equip (this,player):
    player.attributes["magic"] += 3
def on_unequip (this, player):
    player.attributes["magic"] -= 3

