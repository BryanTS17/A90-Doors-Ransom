import BG
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from Label import ImagemClicavel
import Globais
import random


class JanelaCara(QWidget):
    def __init__(self, imagem=None, x=None, y=None, tempo=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.resize(200, 200)

        if x and y:
            self.move(x, y)
        else:
            self.move(random.randint(0, 1900), random.randint(0, 1000))

        self.fundo = ImagemClicavel(self)

        self.fundo.setStyleSheet("background-color: transparent;")

        if imagem == None:
            self.pixmap = QPixmap(random.choice(list(BG.Caras)).value)
        else:
            self.pixmap = QPixmap(imagem)

        self.fundo.setPixmap(self.pixmap)
        self.fundo.resize(self.size())

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )

        time = QTimer(self)
        time.timeout.connect(self.close)
        time.start(tempo)

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


def abrir_janela(x=None, y=None, imagem=None, tempo=100):
    janelaCara = JanelaCara(x=x, y=y, imagem=imagem, tempo=tempo)

    # Guarda a referência para a janela não ser destruída
    Globais.caras.append(janelaCara)
    janelaCara.destroyed.connect(
        lambda: (
            Globais.caras.remove(janelaCara) if janelaCara in Globais.caras else None
        )
    )
    Globais.janela.raise_()
