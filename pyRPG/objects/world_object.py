class world_object:
    """A world_object is any moving or interactable object that can appear in the world, such as the player, an enemy, or a chest.

Functions:
__init___(update_func, collide_func, char_func, color_func, posX, posY, attr): Initializes the object by setting all the functions given
    update_func: This function should update the object. 
    collide_func: This function should handle object collision. It should only change the object you collided with in most cases
    char_func: This function should return the character to display for the object. It's a function so you can change it if you want to.
    color_func: This function should return the color (integer in range [0, 7), see main file for bindings) for the object to be displayed in.
    posX, posY: The X and Y positions the object should start at.
    attr: A dictionary with string keys determining attributes for the object. For example, there may be a "HP" attribute.
update(delta_time): Update based on what key was pressed
getChar(): Return the character to draw
getColor(): Return the color of the object
collide(obj): Handles collision with another world_object
getCoords(): Returns the coordinates of the world_object

In all functions passed during init, another parameter "this" is required as a replacement for self
"""
    def __init__(self, update_func, collide_func, char_func, color_func, posX, posY, start_attributes):
        self.__update_fn = update_func
        self.__collide_fn = collide_func
        self.__getChar_fn = char_func
        self.__getColor_fn = color_func
        self.X = posX
        self.Y = posY
        self.attributes = start_attributes
        return
    def update(self, delta_time):
        self.__update_fn(self, delta_time)
    def collide(self, obj):
        self.__collide_fn(self, obj)
    def getChar(self):
        return self.__getChar_fn(self)
    def getColor(self):
        return self.__getColor_fn(self)
    def getCoords(self):
        return (self.X, self.Y)

