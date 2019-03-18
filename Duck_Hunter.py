#! python3
import autopy
import keyboard

gameURL = "http://www.gotoandplay.it/_games/_nesDuckHunt/nesDuckHunt.php"


def findDuck(startArea):
    screen = autopy.bitmap.capture_screen()
    pos = screen.find_color((252, 116, 96), 0.03,
                            ((startArea[0], startArea[1]), (800, 400)))
    if pos:
        # print("Found Duck at: %s" % str(pos))
        autopy.mouse.move(pos[0]+20, pos[1])
        autopy.mouse.click()


def findGameArea():
    for i in range(10):
        screen = autopy.bitmap.capture_screen()
        pos = screen.find_color((66, 198, 255), 0.03)
        if pos:
            # print("Game Area: " + str(pos))
            return pos
    exit()


def exitGame():
    if keyboard.is_pressed('q'):
        # print('Exit Duck AIM BOT !!')
        return True
    return False


startArea = findGameArea()
for i in range(1000):
    findDuck(startArea)
    if exitGame() == True:
        break
