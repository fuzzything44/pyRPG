name = "Magick Stick"
type = "weapon"
attributes = { "damage" : 9, "range": 10}
def on_equip (this,player):
    player.attributes["magic"] += 5
def on_unequip (this, player):
    player.attributes["magic"] -= 5

