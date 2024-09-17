import pyautogui, time


def main():
    abrir_navegador()
    # scrollar_ebook()
    # descobrir_posicao_botao()
    passar_slides()


def abrir_navegador():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')


def passar_slides():
    dir_x_modelo1 = 1417
    dir_y_modelo1 = 566
    esq_x_modelo1 = 490
    esq_y_modelo1 = 565
    dir_x_modelo2 = 1419
    dir_y_modelo2 = 568
    esq_x_modelo2 = 504
    esq_y_modelo2 = 563
    dir_x_modelo3 = 1568
    dir_y_modelo3 = 520
    esq_x_modelo3 = 329
    esq_y_modelo3 = 519
    loops = 10
    pyautogui.FAILSAFE = False
    while True:
        for i in range(1, loops):
            pyautogui.move(xOffset=esq_x_modelo3, yOffset=esq_y_modelo3, duration=1)
            pyautogui.click(dir_x_modelo3, dir_y_modelo3, interval=0.5)
            time.sleep(4)
        for i in range(1, (loops - 2)):
            pyautogui.move(xOffset=dir_x_modelo3, yOffset=dir_y_modelo3, duration=1.5)
            pyautogui.click(esq_x_modelo3, esq_y_modelo3, interval=0.5)
            time.sleep(4)


def descobrir_posicao_botao():
    while True:
        pos = pyautogui.position()
        print(f'x: {pos.x}, y: {pos.y}')
        time.sleep(2)

def scrollar_ebook():
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(1095, 674)
    while True:
        for i in range(1, 200):
            pyautogui.scroll(-100)
            pyautogui.moveTo(1095, 674, 0.5)
            pyautogui.moveTo(1188, 674, 0.5)
        for i in range (1, 200):
            pyautogui.scroll(100)
            pyautogui.moveTo(1095, 674, 0.5)
            pyautogui.moveTo(1188, 674, 0.5)
        pyautogui.move(329, 529, duration=1)


if __name__ == '__main__':
    main()
