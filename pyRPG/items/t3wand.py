name = "Elder Wand"
type = "weapon"
attributes = { "damage" : 20, "range": 10}
def on_equip (this,player):
    player.attributes["magic"] += 30
def on_unequip (this, player):
    player.attributes["magic"] -= 30

