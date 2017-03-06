import world

def shadowjump(player):
    if "shadowjump_map" in player.attributes and player.attributes["shadowjump_map"] == world.world_name:
        player.X = player.attributes["shadowjump_x"]
        player.Y = player.attributes["shadowjump_y"]
    else:
        player.attributes["shadowjump_map"] = world.world_name
        player.attributes["MP"] += manaCost
    player.attributes["shadowjump_x"] = player.X
    player.attributes["shadowjump_y"] = player.Y
        

manaCost = 30
icon = "\\fx\\bw###\np>P\n###\\fw\\bx"
name = "Shadowjump"
