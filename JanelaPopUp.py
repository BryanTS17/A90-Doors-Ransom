from BG import Bgs
import Globais
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from JanelaPopUpEstica import JanelaPopUpEstica
from Label import ImagemClicavel
import random


class JanelaPopUp(QWidget):
    def __init__(self, imagem=None, tremer=True, x=None, y=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setWindowTitle("RANS0M")
        if x != None and y != None:
            self.resize(300, 150)
            self.move(x, y)
        else:
            n1 = random.randint(150, 500)
            self.resize(n1, n1 // 2)
            self.move(random.randint(0, 1900), random.randint(0, 1000))

        self.fundo = ImagemClicavel(self)
        self.fundo.clicado.connect(self.close)

        if imagem:
            self.pixmap = QPixmap(imagem)
        else:
            self.pixmap = QPixmap(random.choice(list(Bgs)).value)

        if tremer:
            self.time = QTimer(self)
            self.posOriginal = self.pos()
            self.time.timeout.connect(self.tremer)
            self.time.start(50)

        self.fundo.setPixmap(self.pixmap)
        self.fundo.resize(self.size())

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )

        self.show()

    def atualizarFundo(self):
        pixmap = self.pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.fundo.setPixmap(pixmap)
        self.fundo.resize(self.size())

    def tremer(self):
        x = self.posOriginal.x()
        y = self.posOriginal.y()
        self.move(random.randint(x - 5, x + 5), random.randint(y - 5, y + 5))

    def resizeEvent(self, event):
        self.atualizarFundo()
        return super().resizeEvent(event)


def abrir_janela(x=None, y=None, tremer=True, imagem=None):
    janelaPop = JanelaPopUp(x=x, y=y, tremer=tremer, imagem=imagem)

    Globais.janelas.append(janelaPop)

    janelaPop.destroyed.connect(
        lambda: (
            Globais.janelas.remove(janelaPop) if janelaPop in Globais.janelas else None
        )
    )
    Globais.janela.raise_()
