import display

def heal(player):
    try:
        player.attributes["HP"] += 1.5*player.attributes["magic"]
        if player.attributes["HP"] >= player.attributes["maxHP"]:
            player.attributes["HP"] = player.attributes["maxHP"]
    except:
        pass
manaCost = 5
icon = ["\\|/", "-+-", "/|\\"]
color = display.WHITE
name = "Heal"