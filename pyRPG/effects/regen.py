def regen1(obj, delta_time):
    try:
        obj.attributes["HP"] += 10.0 * delta_time / 10000
    except:
        pass

def regen2(obj, delta_time):
    try:
        obj.attributes["HP"] += 20.0 * delta_time / 10000
    except:
        pass

def regen3(obj, delta_time):
    try:
        obj.attributes["HP"] += 30.0 * delta_time / 10000
    except:
        pass