import world

# Import all maps
from maps import start 
from maps import tut1
from maps import tutboss
from maps import town
from maps import stonstart
from maps import credits
from maps import ston1
from maps import ston2
from maps import stonboss

def make(make_what):
    # World generation
    if ("start" in make_what) or (make_what == "all"):
        start.generate()
        world.save("start")

    if ("start" in make_what) or (make_what == "all"):
        tut1.generate()
        world.save("tut1")
        
    if ("tutboss" in make_what) or (make_what == "all"):
        tutboss.generate()
        world.save("tutboss")
        
    if ("town" in make_what) or (make_what == "all"):
        town.generate()
        world.save("town")
        
    if ("stoneboss" in make_what) or (make_what == "all"):
        stonboss.generate()
        world.save("stoneboss")
        
    if ("stonestart" in make_what) or (make_what == "all"):
        stonstart.generate()
        world.save("stonestart")
        
    if ("credits" in make_what) or (make_what == "all"):
        credits.generate()
        world.save("credits")
        
    if ("stone1" in make_what) or (make_what == "all"):
        ston1.generate()
        world.save("stone1")
        
    if ("stone2" in make_what) or (make_what == "all"):
        ston2.generate()
        world.save("stone2")
    
