def regen1(obj, delta_time):
    try:
        obj.attributes["HP"] += 1.0 * obj.attributes["magic"] * delta_time / 1000
        if obj.attributes["HP"] > obj.attributes["maxHP"]:
            obj.attributes["HP"] = obj.attributes["maxHP"]
    except:
        pass

def regen2(obj, delta_time):
    try:
        obj.attributes["HP"] += 2.0  * obj.attributes["magic"] * delta_time / 1000
        if obj.attributes["HP"] > obj.attributes["maxHP"]:
            obj.attributes["HP"] = obj.attributes["maxHP"]
    except:
        pass

def regen3(obj, delta_time):
    try:
        obj.attributes["HP"] += 3.0 * obj.attributes["magic"] * delta_time / 1000
        if obj.attributes["HP"] > obj.attributes["maxHP"]:
            obj.attributes["HP"] = obj.attributes["maxHP"]
    except:
        pass