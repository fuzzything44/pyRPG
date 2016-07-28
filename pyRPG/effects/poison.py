def poison(obj, delta_time):
    if "HP" in obj.attributes:
        obj.attributes["HP"] -= 15.0 * delta_time / 10000

def venom(obj, delta_time):
    if "HP" in obj.attributes:
        obj.attributes["HP"] -= 25.0 * delta_time / 10000


def deadlypoison(obj, delta_time):
    if "HP" in obj.attributes:
        obj.attributes["HP"] -= 45.0 * delta_time / 10000
