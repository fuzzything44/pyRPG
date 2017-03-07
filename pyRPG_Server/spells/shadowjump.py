import world

def shadowjump(player):
    x_jump = player.X
    y_jump = player.Y

    if "shadowjump_map" in player.attributes and player.attributes["shadowjump_map"] == world.world_name:
        player.X = player.attributes["shadowjump_x"]
        player.Y = player.attributes["shadowjump_y"]
    else:
        player.attributes["shadowjump_map"] = world.world_name
        player.attributes["MP"] += manaCost
        
    player.attributes["shadowjump_x"] = x_jump
    player.attributes["shadowjump_y"] = y_jump

manaCost = 30
icon = "\\fx\\bw###\np>P\n###\\fw\\bx"
name = "Shadowjump"
