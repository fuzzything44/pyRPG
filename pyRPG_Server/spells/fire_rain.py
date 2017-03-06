import world

from objects.Player import fire_rain

def fire_rain(player):
    for x in range(-2, 3):
        for y in range(-2, 3):
            if not world.out_of_bounds(x, y):
                world.objects.append(fire_rain.fire_rain(x, y, 1.0 * player.attributes["magic"], player))

manaCost = 40
icon = "\\fr;;;\n;;;\n;;;\\fw"
name = "Fire Rain"
