import display
import world

def start():
    """Gives the main menu option to load a file, create a new file, or exit"""
    display.printc(28, 10, "Welcome to pyRPG!")
    display.printc(31, 11, "Load a file")
    display.printc(31, 12, "New game")
    display.printc(31, 13, "Exit game")
    display.refresh()
    opt = 0
    can_up = True
    can_down = True
    while True:
        display.printc(30, opt + 11, ' ')
        if can_up and (display.keyDown(ord('W')) or display.keyDown(display.CONST.VK_UP)):
            opt -= 1
            if opt < 0:
                opt = 2
            can_up = False
        else:
            can_up = True

        if can_down and (display.keyDown(ord('S')) or display.keyDown(display.CONST.VK_DOWN)):
            opt += 1
            if opt > 2:
                opt = 0
            can_down = False
        else:
            can_down = True
        display.printc(30, opt + 11, '>')
        display.refresh()      

        if display.keyDown(ord('E')) or display.keyDown(display.CONST.VK_RETURN):
            # Option chosen.
            if opt == 0:
                break
            if opt == 1:
                break
            if opt == 2:
                display.end() # They chose exit

         
