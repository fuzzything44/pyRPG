name ="Brooks Mach 3 Speed Dragons"
type = "shoes"
attributes = {}
def on_equip (this,player):
    player.attributes["move_spd"]-=10
    player.attributes["maxHP"]+=3
def on_unequip (this, player):
    player.attributes["move_spd"]+=10
    player.attributes ["maxHP"]-=3
