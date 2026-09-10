from enum import Enum
import os
import sys


def caminho_recurso(caminho):
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base, caminho)


class Bgs(Enum):
    img1 = caminho_recurso("imagens\\Captura de tela 2026-09-08 163147.png")
    img2 = caminho_recurso("imagens\\Captura de tela 2026-09-08 163159.png")
    img3 = caminho_recurso("imagens\\Captura de tela 2026-09-08 195812.png")
    img4 = caminho_recurso("imagens\\Captura de tela 2026-09-08 195802.png")


class BgsE(Enum):
    img1 = caminho_recurso("imagens\\Captura de tela 2026-09-08 195729.png")
    img2 = caminho_recurso("imagens\\Captura de tela 2026-09-08 195704.png")
    img3 = caminho_recurso("imagens\\Captura de tela 2026-09-08 201730.png")
    img4 = caminho_recurso("imagens\\Captura de tela 2026-09-08 201730.png")


class Caras(Enum):
    img1 = caminho_recurso("imagens\\A-90IDLE.ong.png")
    img2 = caminho_recurso("imagens\\A-90JUMPSCARE.png")
    img3 = caminho_recurso("imagens\\90_3.png")
    img4 = caminho_recurso("imagens\\803012A6-FCEF-4CC9-A7B7-BC7FE34C3307.png")
