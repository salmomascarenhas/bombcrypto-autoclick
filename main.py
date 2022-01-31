import threading
from time import sleep

import pyautogui

DELAY_BETWEEN_COMMANDS = 1.0


def main():
    initializedPyAutoGui()
    countDownTimer()

    threading.Thread(target=allHeroesStart).start()
    sleep(420)
    threading.Thread(target=dontSleepScreen).start()

    # allHeroesStop()


    print('Done.')


def initializedPyAutoGui():
    pyautogui.FAILSAFE = False

def countDownTimer():
    print('Starting', end='', flush=True)
    for i in range(0, 10):
        print('.',end='')
        sleep(1)
    print('Go')

def reportedPositionMouse(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(1)

def holdKey(key, seconds=1.00):
    pyautogui.keyDown(key)
    sleep(seconds)
    pyautogui.keyUp(key)
    sleep(DELAY_BETWEEN_COMMANDS)

def allHeroesStart():
    while True:
        # Open the above menu and open tab heroes.
        pyautogui.moveTo(674, 685,0.25)
        sleep(1)
        pyautogui.click()
        sleep(1)
        pyautogui.moveTo(674, 695,0.25)
        pyautogui.click()
        sleep(1)


        #  Click on the button to all go to work.
        pyautogui.moveTo(595, 271,0.25)
        sleep(1)
        pyautogui.click()
        sleep(1)

        #  Button to close window heroes.
        pyautogui.moveTo(734,221,0.25)
        pyautogui.click()
        sleep(1)

        # Click on center scren to return at the game.
        pyautogui.moveTo(666, 439,0.25)
        pyautogui.click()

        print('All heroes are working!')
        sleep(7200)

def allHeroesStop():
    # Open the above menu and open tab heroes.
    pyautogui.moveTo(674, 685,0.25)
    sleep(1)
    pyautogui.click()
    sleep(1)
    pyautogui.click()
    sleep(1)


    #  Click on the button to all go back stop from work.
    pyautogui.moveTo(652, 266,0.25)
    sleep(1)
    pyautogui.click()
    sleep(1)

    #  Button to close window heroes.
    pyautogui.moveTo(734,221,0.25)
    pyautogui.click()
    sleep(1)

    # Click on center scren to return at the game.
    pyautogui.moveTo(666, 439,0.25)
    pyautogui.click()

    print('All heroes are stoped!')

def dontSleepScreen():
    while True:
        pyautogui.moveRel(xOffset=10,yOffset=0,duration=0.25)
        sleep(1)
        pyautogui.moveRel(xOffset=-10,yOffset=0,duration=0.25)
        sleep(1)
        pyautogui.click()
        sleep(420)
    

if __name__ == "__main__":
    main()
