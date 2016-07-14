def fire(obj, delta_time):
    try:
        obj.attributes["HP"] -= 15.0 * delta_time / 1000
    except:
        pass

def bigfire(obj, delta_time):
    try:
        obj.attributes["HP"] -= 30.0 * delta_time / 1000
    except:
        pass

def hugefire(obj, delta_time):
    try:
        obj.attributes["HP"] -= 50 * delta_time / 1000
    except:
        pass
def magicfire(obj, delta_time):
    try:
        obj.attributes["MP"] -= 10 * delta_time / 1000
    except:
        pass