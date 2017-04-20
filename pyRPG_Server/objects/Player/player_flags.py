# Flag definitions
TUT_MONEY_GIVEN = 0 # If tutorial money has been given or not
SKILL_TUTORIAL = 1  # If they have the tutorial skill

def get_flag(player, flag):
    if len(player.attributes["flags"]) <= flag: # Need to lengthen
        num_additions = flag - len(player.attributes["flags"]) + 1
        player.attributes["flags"].extend([0] * num_additions) # Add missing flags
    return player.attributes["flags"][flag]

def set_flag(player, flag, value):
    if len(player.attributes["flags"]) <= flag: # Need to lengthen
        num_additions = flag - len(player.attributes["flags"]) + 1
        player.attributes["flags"].extend([0] * num_additions) # Add missing flags
    player.attributes["flags"][flag] = value
