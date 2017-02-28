import world

def knockback(player):
    hit_enemies = [] # List of all enemies close enough to hit
    range_sq = 9 # Hits everything within 3 tiles
    for obj in world.objects:
        if obj.type == "enemy" and ((player.X - obj.X) ** 2 + (player.Y - obj.Y) ** 2) <= range_sq:
            hit_enemies.append(obj)

    for hit in hit_enemies:
        hit.attributes["HP"] -= 10
        # Knockback
        diff_x = hit.X - player.X
        diff_y = hit.Y - player.Y

        if diff_x != 0: # Normalize x knockback
            diff_x = int(diff_x / abs(diff_x))
        if diff_y != 0: # Normalize y knockback
            diff_y = int(diff_y / abs(diff_y))

        if diff_x == 0 and diff_y == 0:
            diff_x = 1

        if not world.out_of_bounds(hit.X + diff_x, hit.Y + diff_y) and world.map[hit.X + diff_x][hit.Y + diff_y][3]: # Enemy can move that way
            hit.X += diff_x
            hit.Y += diff_y

        

manaCost = 15
icon = "\\fw \\\\ \n  |\n / "
name = "Smash"
