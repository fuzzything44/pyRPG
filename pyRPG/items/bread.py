name = "Bread"

def use(own):
    try:
        own.attributes["HP"] += 1
        if own.attributes["HP"] > own.attributes["maxHP"]:
            own.attributes["HP"] = own.attributes["maxHP"]
    except:
        pass