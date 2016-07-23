def regen1(obj, delta_time):
    try:
        obj.attributes["HP"] += 1.0 * delta_time / 1000
    except:
        pass

def regen2(obj, delta_time):
    try:
        obj.attributes["HP"] += 2.0 * delta_time / 1000
    except:
        pass

def regen3(obj, delta_time):
    try:
        obj.attributes["HP"] += 3.0 * delta_time / 1000
    except:
        pass