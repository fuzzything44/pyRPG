name = "dagger"
type = "weapon"
attributes = { "damage" : 2, "range": 1}
def on_equip (this,player):
    player.attributes["atk_spd"] -= 5
def on_unequip (this, player):
    player.attributes["atk_spd"] += 5

