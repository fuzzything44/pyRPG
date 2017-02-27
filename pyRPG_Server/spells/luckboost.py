import display
from effects import effect

def luckboost(player):
    if "lucky_day" in player.attributes["effects"]:
        player.attributes["effects"]["lucky_day"].time += 15000
    else:
        player.attributes["effects"]["lucky_day"] = effect.effect(player, 15000, "Extra Lucky", {"luck" : 10})

manaCost = 15
icon = "\\fy | \n-$-\n | \\fw"
name = "Lucky Day"
