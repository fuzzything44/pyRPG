def poison(obj, delta_time):
    try:
        obj.attributes["HP"] -= 15.0 * delta_time / 10000
    except:
        pass

def venom(obj, delta_time):
    try:
        obj.attributes["HP"] -= 25.0 * delta_time / 10000
    except:
        pass

def deadlypoison(obj, delta_time):
    try:
        obj.attributes["HP"] -= 45.0 * delta_time / 10000
    except:
        pass