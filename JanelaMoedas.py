from BG import Bgs
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import BG
from Label import ImagemClicavel
import Globais
import random


class JanelaMoeda(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.resize(50, 50)
        self.move(random.randint(0, 1900), random.randint(0, 1000))

        self.fundo = ImagemClicavel(self)
        self.fundo.clicado.connect(self.coletado)

        self.fundo.setStyleSheet("background-color: transparent;")

        self.pixmap = QPixmap(BG.caminho_recurso("imagens\\Gold.png"))

        self.fundo.setPixmap(self.pixmap)
        self.fundo.resize(self.size())

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.show()

    def atualizarFundo(self):
        pixmap = self.pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.fundo.setPixmap(pixmap)
        self.fundo.resize(self.size())

    def resizeEvent(self, event):
        self.atualizarFundo()
        return super().resizeEvent(event)

    def coletado(self):
        Globais.Moedas -= 250
        self.close()
