name = "Super good dagger"
type = "weapon"
attributes = { "damage" : 15, "range": 1}
def on_equip (this,player):
    player.attributes["atk_spd"] -= 15
def on_unequip (this, player):
    player.attributes["atk_spd"] += 15

