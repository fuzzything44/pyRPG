import display

def heal(player):
    if ("HP" in player.attributes) and ("maxHP" in player.attributes):
        player.attributes["HP"] += 1.5*player.attributes["magic"]
        if player.attributes["HP"] >= player.attributes["maxHP"]:
            player.attributes["HP"] = player.attributes["maxHP"]

manaCost = 5
icon = ["\\|/", "-+-", "/|\\"]
color = display.WHITE
name = "Heal"