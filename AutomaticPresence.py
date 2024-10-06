import pyautogui
import time


def main():
    open_browser()
    # scroll_ebook()
    # find_button_position()
    advance_slides()


def open_browser():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')


def advance_slides():
    # First slide model
    dir_x_modelo1 = 1417
    dir_y_modelo1 = 566
    esq_x_modelo1 = 490
    esq_y_modelo1 = 565
    
    # Second slide model
    dir_x_modelo2 = 1419
    dir_y_modelo2 = 568
    esq_x_modelo2 = 504
    esq_y_modelo2 = 563
    
    # Third slide model
    dir_x_modelo3 = 1568
    dir_y_modelo3 = 520
    esq_x_modelo3 = 329
    esq_y_modelo3 = 519
    
    loops = 10
    pyautogui.FAILSAFE = False
    while True:
        for i in range(1, loops):
            pyautogui.move(xOffset=esq_x_modelo3, yOffset=esq_y_modelo3, duration=1)
            pyautogui.click(dir_x_modelo1, dir_y_modelo1, interval=0.5)
            time.sleep(4)
        for i in range(1, (loops - 2)):
            pyautogui.move(xOffset=dir_x_modelo3, yOffset=dir_y_modelo3, duration=1.5)
            pyautogui.click(esq_x_modelo1, esq_y_modelo1, interval=0.5)
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
