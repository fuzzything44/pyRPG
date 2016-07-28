def fire(obj, delta_time):
    if "HP" in obj.attributes:
        obj.attributes["HP"] -= 15.0 * delta_time / 1000


def bigfire(obj, delta_time):
    if "HP" in obj.attributes:
        obj.attributes["HP"] -= 30.0 * delta_time / 1000

def hugefire(obj, delta_time):
    if "HP" in obj.attributes:
        obj.attributes["HP"] -= 50 * delta_time / 1000

def magicfire(obj, delta_time):
    if "MP" in obj.attributes:
        obj.attributes["MP"] -= 10 * delta_time / 1000
