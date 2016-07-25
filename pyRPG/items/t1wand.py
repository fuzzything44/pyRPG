name = "Wand"
type = "weapon"
attributes = { "damage" : 3, "range": 7}
def on_equip (this,player):
    player.attributes["magic"] += 2
def on_unequip (this, player):
    player.attributes["magic"] -= 2

