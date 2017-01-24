def heal(player):
    player.attributes["HP"] += 1.5*player.attributes["magic"]
    if player.attributes["HP"] >= player.attributes["maxHP"]:
        player.attributes["HP"] = player.attributes["maxHP"]

manaCost = 5
icon = "\\\\|/\n-+-\n/|\\\\"
name = "Heal"