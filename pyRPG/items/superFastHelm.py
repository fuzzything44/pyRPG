name ="Super fast helmet"
type = "helmet"
attributes = {}
def on_equip (this,player):
    player.attributes["move_spd"]+30, ["maxHP"]+3
def on_unequip (this, player):
    player.attributes["move_spd"]-8, ["maxHP"]-3
