import sys
import os
import BG
import Globais
from pynput import mouse
from BG import Bgs
from BG import Caras
from shiboken6 import isValid
from Automacao import mover_mouse_aleatorio
from VariasJanelas import janelasCascadaCara
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from JanelaPopUp import JanelaPopUp
from JanelaPopUpEstica import JanelaPopUpEstica
from JanelaMain import JanelaMain
from JanelaMoedas import JanelaMoeda
from JanelaCara import JanelaCara
from JanelaThank import JanelaThank
from JanelaVideo import JanelaVideo
from Sons import tocar_som, carregar_sons, parar_som
from Wallpaper import mudar_wallpaper, restaurar_wallpaper, obter_wallpaper_atual
import random

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
wallpaper_original = obter_wallpaper_atual()

janelas = Globais.janelas
moedas = Globais.moedas
caras = Globais.caras

mexeu = False

video = None
janela = None  # JanelaMain()
timer = None
timer2 = None
timer3 = None
timer4 = None
timer5 = None
timer6 = None
listener = None


def abrir_janela():
    nun = random.randint(1, 2)
    if nun == 1:
        janelaPop = JanelaPopUp()

    else:
        janelaPop = JanelaPopUpEstica()

    janelas.append(janelaPop)
    janelaPop.raise_()

    janelaPop.destroyed.connect(
        lambda: janelas.remove(janelaPop) if janelaPop in janelas else None
    )


def criar_moedas():
    janelaMoeda = JanelaMoeda()
    # mover_mouse_aleatorio()
    janelasCascadaCara(
        x=random.randint(0, Globais.largura - 300),
        y=random.randint(0, Globais.altura - 300),
    )

    # Guarda a referência para a janela não ser destruída
    moedas.append(janelaMoeda)

    janelaMoeda.destroyed.connect(
        lambda: moedas.remove(janelaMoeda) if janelaMoeda in moedas else None
    )

    Globais.janela.raise_()


def criar_caras():
    janelaCara1 = JanelaCara()
    janelaCara2 = JanelaCara()
    janelaCara3 = JanelaCara()

    janelasCascadaCara(
        x=random.randint(0, Globais.largura - 300),
        y=random.randint(0, Globais.altura - 300),
        quantidade=5,
        tempo=100,
        distancia=50,
        imagem=random.choice(list(BG.Caras)).value,
    )

    # Guarda a referência para a janela não ser destruída
    caras.append(janelaCara1)
    caras.append(janelaCara2)
    caras.append(janelaCara3)

    janelaCara1.destroyed.connect(
        lambda: caras.remove(janelaCara1) if janelaCara1 in caras else None
    )
    janelaCara2.destroyed.connect(
        lambda: caras.remove(janelaCara2) if janelaCara2 in caras else None
    )
    janelaCara2.destroyed.connect(
        lambda: caras.remove(janelaCara2) if janelaCara2 in caras else None
    )

    proximo_tempo = random.randint(300, 700)
    timer4.start(proximo_tempo)
    Globais.janela.raise_()


def abrir_cmd():
    n1 = random.randint(1, 5)
    n1 = 4

    os.system(f'start cmd /k "color {n1} && cd /d c:\\ && dir /s"')


def fechar_todas():
    global janela, listener

    # Parar os timers
    for t in (timer, timer2, timer3, timer4, timer5, timer6):
        if t is not None:
            t.stop()

    # Parar o listener do mouse, se existir
    if listener is not None:
        listener.stop()

    # Fechar as janelas das listas
    for janela_atual in list(janelas + caras + moedas):
        if janela_atual is not None and isValid(janela_atual):
            janela_atual.close()
            janela_atual.deleteLater()

    janelas.clear()
    caras.clear()
    moedas.clear()

    # Fechar a janela principal
    Globais.janela.close()
    Globais.janela.deleteLater()

    # Fechar os CMDs criados pelo programa
    os.system("taskkill /f /im cmd.exe")

    restaurar_wallpaper(wallpaper_original)
    parar_som("fundo")

    # Criar a janela final somente depois de fechar tudo
    janela = JanelaThank()
    janela.show()
    janela.raise_()
    janela.activateWindow()

    janelas.append(janela)

    janela.destroyed.connect(
        lambda: janelas.remove(janela) if janela in janelas else None
    )

    tocar_som("ganhou")


def verificar_moedas():
    if Globais.Moedas <= 0:
        fechar_todas()


def iniciar_video():
    global video, mexeu, listener

    if mexeu:

        video = JanelaVideo(BG.caminho_recurso(r"videos\\Video Project 1.mp4"))
        video.terminou.connect(iniciar_jogo)
        video.show()

    else:
        listener.stop()
        listener = None
        num = random.randint(1000 * 10, 1000 * 60)
        num = 1000
        QTimer.singleShot(num, testar_mexeu)


def iniciar_jogo():
    global janela, timer, timer2, timer3, timer4, timer5, timer6

    timer = QTimer(Globais.janela)
    timer2 = QTimer(Globais.janela)
    timer3 = QTimer(Globais.janela)
    timer4 = QTimer(Globais.janela)
    timer5 = QTimer(Globais.janela)
    timer6 = QTimer(Globais.janela)

    tocar_som("fundo")

    Globais.janela = JanelaMain()
    Globais.janela.show()

    timer.timeout.connect(abrir_janela)
    timer.start(1000)  # 1000 ms = 1 segundo

    timer2.timeout.connect(abrir_cmd)
    timer2.start(10000)  # 1000 ms = 1 segundo

    timer3.timeout.connect(criar_moedas)
    timer3.start(2000)  # 1000 ms = 1 segundo

    timer4.timeout.connect(criar_caras)
    timer4.start(random.randint(300, 700))  # 1000 ms = 1 segundo

    timer5.timeout.connect(verificar_moedas)
    timer5.start(100)  # 1000 ms = 1 segundo

    timer6.timeout.connect(mover_mouse_aleatorio)
    timer6.start(10000)  # 1000 ms = 1 segundo

    mudar_wallpaper(
        BG.caminho_recurso(r"imagens\\Captura de tela 2026-09-09 194707.png")
    )


# principal = QWidget()
# principal.setWindowTitle("Controle da réplica")

# layout = QVBoxLayout(principal)

# botao_abrir = QPushButton("Abrir janela")
# botao_abrir.clicked.connect(abrir_janela)

# botao_fechar = QPushButton("Fechar todas")
# botao_fechar.clicked.connect(fechar_todas)

# layout.addWidget(botao_abrir)
# layout.addWidget(botao_fechar)


# principal.show()
def chamar_iniciar_video(x, y):
    global mexeu

    if not mexeu:
        mexeu = True
        # QTimer.singleShot(0, iniciar_video)


def testar_mexeu():
    global video, listener
    janela = JanelaCara(Caras.img1.value, tempo=1000)
    janelas.append(janela)

    janela.destroyed.connect(
        lambda: janelas.remove(janela) if janela in janelas else None
    )
    tocar_som("comeca")

    def trocar_video():
        global video, listener
        video = JanelaVideo(BG.caminho_recurso("videos\\Video Project 7.mp4"))
        video.terminou.connect(iniciar_video)
        video.show()

        listener = mouse.Listener(on_move=chamar_iniciar_video)
        listener.start()

    # timeV = QTimer()
    # timeV.timeout.connect(trocar_video)

    QTimer.singleShot(900, trocar_video)


carregar_sons()
testar_mexeu()

sys.exit(app.exec())
