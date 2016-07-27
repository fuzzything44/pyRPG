name = "Good dagger"
type = "weapon"
attributes = { "damage" : 5, "range": 2}
def on_equip (this,player):
    player.attributes["atk_spd"] -= 10
def on_unequip (this, player):
    player.attributes["atk_spd"] += 10

