name ="Track shorts"
type = "pants"
attributes = {}
def on_equip (this,player):
    player.attributes["move_spd"]+50, ["maxHP"]+6
def on_unequip (this, player):
    player.attributes["move_spd"]-50, ["maxHP"]-6
