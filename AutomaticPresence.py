import pyautogui
import time


def main():
    open_browser()
    # scroll_ebook()
    find_button_position()
    # advance_slides()


def open_browser():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')


def advance_slides():
    # Modelo novo
    dir_x = 1848
    esq_x = 211
    dir_y = 767
    esq_y = 880
    
    loops = 10
    pyautogui.FAILSAFE = False
    while True:
        for i in range(1, loops):
            pyautogui.move(xOffset=esq_x, yOffset=esq_y, duration=1)
            pyautogui.click(dir_x, dir_y, interval=0.5)
            time.sleep(4)
        for i in range(1, (loops - 2)):
            pyautogui.move(xOffset=dir_x, yOffset=dir_y, duration=1.5)
            pyautogui.click(esq_x, esq_y, interval=0.5)
            time.sleep(4)


def find_button_position():
    while True:
        pos = pyautogui.position()
        print(f'x: {pos.x}, y: {pos.y}')
        time.sleep(2)


def scroll_ebook():
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(1095, 674)
    while True:
        for i in range(1, 200):
            pyautogui.scroll(-100)
            pyautogui.moveTo(1095, 674, 0.5)
            pyautogui.moveTo(1188, 674, 0.5)
        for i in range(1, 200):
            pyautogui.scroll(100)
            pyautogui.moveTo(1095, 674, 0.5)
            pyautogui.moveTo(1188, 674, 0.5)
        pyautogui.move(329, 529, duration=1)


if __name__ == '__main__':
    main()
