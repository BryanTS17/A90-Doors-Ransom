import random

import BG
import JanelaCara
import Globais
import JanelaPopUp
from PySide6.QtCore import QTimer


def janelasCascadaCara(
    imagem=BG.caminho_recurso("imagens\\803012A6-FCEF-4CC9-A7B7-BC7FE34C3307.png"),
    quantidade=20,
    tempo=300,
    distancia=20,
    x=None,
    y=None,
):
    if x is None:
        x = random.randint(0, Globais.largura - 200)

    if y is None:
        y = random.randint(0, Globais.altura - 200)

    if quantidade <= 0:
        return True

    QTimer.singleShot(
        100 * quantidade,
        lambda: JanelaCara.abrir_janela(
            x=x + (distancia * quantidade),
            y=y + (distancia * quantidade),
            imagem=imagem,
            tempo=tempo,
        ),
    )

    return janelasCascadaCara(
        imagem=imagem,
        quantidade=quantidade - 1,
        x=x,
        y=y,
        distancia=distancia,
        tempo=tempo,
    )
