import world

# Import all maps
import maps

def make_from_file(file_in, file_out):
    data = []
    # Read in the input file
    with open(file_in, 'r') as data_file:
        data = data_file.readlines()
        data_file.close()
    # Find all definitions:
    chr_defs = {}
    # Populate chr_defs. Pretty much any character easily typed on keyboard is here.
    for chr in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`~-_=+[{]}\\|;:\",./<>? ":
        chr_defs[chr] = "[0, 1, '" + chr + "', True]\n"
    chr_defs["'"] = "[0, 1, '\\'', True]\n"

    while data[0][:3] != "end":
        # Otherwise, line should be in the form of CHR = [fgc, bgc, chr, solid]
        if data[0] != '\n': # Not an empty line
            chr = data[0][0]
            assignment = data[0][data[0].index('=') + 1:] # Remove everything before the first =
            chr_defs[chr] = assignment
        data = data[1:] # Remove first line
    # Now take the last character.
    default_char = data[0][3]
    data = data[1:] # Remove the line for end.

    with open(file_out, 'w') as out_file:
    # Print opening stuff
        out_file.write("# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops\n")
        out_file.write("import display\nimport world\n\n") # Start of map stuff.
        out_file.write("def generate():\n") # And the generage function
        out_file.write("    world.objects.clear()\n")
        if default_char == '\n': # They didn't set a default, so default is world_nothing
            out_file.write("    world.map = [[ world.WORLD_NOTHING for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]\n")
        else:
            out_file.write("    world.map = [[" + chr_defs[default_char][:-1] + " for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]\n")
        # Variables used in generation
        x_coord = 0 # x coordinate of the map
        y_coord = 0 # y coordinate of the map

        for line in data: # Do stuff with every line
            line = line[:-1] # Remove the newline from the end of it.
            for chr in line:
                if chr != default_char: # If it's not default, it needs to be placed in.
                    # Write the map location.
                    out_file.write("    world.map[" + str(x_coord) + "][" + str(y_coord) + "] = ")
                    # Write out the tile
                    out_file.write(chr_defs[chr])
                x_coord += 1
            y_coord += 1
            x_coord = 0
        out_file.close()

def make(make_what):
    # World generation
    if ("+start " in make_what) or (("+all " in make_what) and ("-tutorial " not in make_what)):
        print("Making start", end = "")
        
        maps.start.generate()
        world.save("start")
        print(".")

    if ("+war_tut " in make_what) or ("+tutorial " in make_what and "-war_tut " not in make_what) or (("+all " in make_what) and ("-tutorial " not in make_what or "-war_tut " not in make_what)):
        print("Making warrior tutorial", end = "")
        
        maps.tutorial.war_tut.warrior_start.generate()
        world.save("warrior_start")
        print(".", end="")

        maps.tutorial.war_tut.war_tut_1.generate()
        world.save("war_tut_1")
        print('.')

    if ("+test_dungeon " in make_what) or ("+all " in make_what and "-test_dungeon " not in make_what):
        print("Making test dungeon", end = "")

        maps.test_dungeon.start.generate()
        world.save("test_dungeon_start")
        print(".", end="")

        maps.test_dungeon.test_dungeon_1.generate()
        world.save("test_dungeon_1")
        print(".")
        


if __name__ == "__main__":
    #make_from_file("maps/tutorial/war_tut/war_tut_1.txt", "maps/tutorial/war_tut/war_tut_1.py")
    print("Make what maps?")
    print("Options: (use +opt_name for that map (or everything under it), use -opt to exclude option")
    print("all")
    print("|--start")
    print("|--tutorial")
    print("|  |--war_tut")
    print("|  |--mage_tut(NOT MADE YET)")
    print("|  |--thief_tut(NOT MADE YET)")
    print("|--test_dungeon")



    make(input() + " ")
