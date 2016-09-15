import display
import world

# Import all maps
from maps import Tutorial
from maps import town
from maps import credits
from maps import StoneDungeon

def make_from_file(file_in, file_out):
    data = []
    # Read in the input file
    with open(file_in, 'r') as data_file:
        data = data_file.readlines()
        data_file.close()
    # Find all definitions:
    chr_defs = {}
    # Populate chr_defs. Pretty much any character easily typed on keyboard is here.
    for chr in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`~-_=+[{]}\\|;:'\",./<>? ":
        chr_defs[chr] = "[0, 1, '" + chr + "', True]\n"

    while data[0] != "end\n":
        # Otherwise, line should be in the form of CHR = [fgc, bgc, chr, solid]
        if data[0] != '\n': # Not an empty line
            chr = data[0][0]
            assignment = data[0][data[0].index('=') + 1:] # Remove everything before the first =
            chr_defs[chr] = assignment
        data = data[1:] # Remove first line
    data = data[1:] # Remove the line for end.

    with open(file_out, 'w') as out_file:
    # Print opening stuff
        out_file.write("# This file automatically generated from a template. That's why it defines the world one at a time instead of using loops\n")
        out_file.write("import display\nimport world\n\n") # Start of map stuff.
        out_file.write("def generate():\n") # And the generage function
        out_file.write("    world.objects.clear()\n")
        out_file.write("    world.map = [[ world.WORLD_NOTHING for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]\n")
        # Variables used in generation
        x_coord = 0 # x coordinate of the map
        y_coord = 0 # y coordinate of the map

        for line in data: # Do stuff with every line
            line = line[:-1] # Remove the newline from the end of it.
            if line != "": # Don't do things with lines that have nothing on them.
                for chr in line:
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
    if ("+tutorial" in make_what) or (("all" in make_what) and ("-tutorial" not in make_what)):
        Tutorial.start.generate()
        world.save("start")

        Tutorial.tut1.generate()
        world.save("tut1")
        
        Tutorial.tut2.generate()
        world.save("tut2")

        Tutorial.tutboss.generate()
        world.save("tutboss")
        
    if ("+town" in make_what) or (("all" in make_what) and ("-town" not in make_what)):
        town.generate()
        world.save("town")
        
    if ("+stonedungeon" in make_what) or (("all" in make_what) and ("-stonedungeon" not in make_what)):
        StoneDungeon.stonboss.generate()
        world.save("stoneboss")
        
        StoneDungeon.stonstart.generate()
        world.save("stonestart")
        
        StoneDungeon.ston1.generate()
        world.save("stone1")
        
        StoneDungeon.ston2.generate()
        world.save("stone2")

    if ("+credits" in make_what) or (("all" in make_what) and ("-credits" not in make_what)):
        credits.generate()
        world.save("credits")
 
