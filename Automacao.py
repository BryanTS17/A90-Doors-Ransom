import pyautogui
import random
import threading

largura, altura = pyautogui.size()


def mover_mouse_aleatorio(tempo=0):
    def move():
        pyautogui.moveTo(random.randint(0, largura), random.randint(0, altura), tempo)

    threading.Thread(target=move, daemon=True).start()
