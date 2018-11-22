import autopy

def findDuck(startArea):
    screen = autopy.bitmap.capture_screen()
    pos = screen.find_color((255,119,99),0.03,((startArea[0], startArea[1]),(800,400)))
    if pos:
        print("Found Duck at: %s" % str(pos))
        autopy.mouse.move(pos[0]+20,pos[1])
        autopy.mouse.click()

def findGameArea():
    for i in range(10):
        screen = autopy.bitmap.capture_screen()
        pos = screen.find_color((0,204,255),0.03)
        if pos:
            print("Game Area: " + str(pos))
            return pos
    exit()

startArea = findGameArea()
for i in range(1000):
    findDuck(startArea)
