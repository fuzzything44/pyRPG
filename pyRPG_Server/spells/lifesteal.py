import world

def lifesteal(player):
    # Find nearest enemy
    locX = player.X # For quicker checking
    locY = player.Y
    
    closest_enemy = None
    dist = 9999
    for obj in world.objects:
        if (obj.type == "enemy") and (((locX - obj.X)**2 + (locY - obj.Y)**2) ** .5 < dist):
            closest_enemy = obj
            dist = ((locX - obj.X)**2 + (locY - obj.Y)**2) ** .5

    # Now that we have the closest enemy, damage it.
    if closest_enemy is not None:
        damage = min(150, player.attributes["magic"] * (player.attributes["maxHP"] / player.attributes["HP"]) * 0.5)

        closest_enemy.attributes["HP"] -= damage
        player.attributes["HP"] += damage
        if player.attributes["HP"] > player.attributes["maxHP"]:
            player.attributes["HP"] = player.attributes["maxHP"]

manaCost = 20
icon = "\\fg ! \n(X)\n ! "
name = "Lifesteal"
