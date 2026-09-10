from BG import BgsE
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from Label import ImagemClicavel
import random


class JanelaPopUpEstica(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setWindowTitle("RANS0M")
        n1 = random.randint(150, 500)
        n2 = random.randint(150, 500)
        self.resize(n1, n2)
        self.move(random.randint(0, 1900), random.randint(0, 1000))

        self.fundo = ImagemClicavel(self)
        self.fundo.clicado.connect(self.close)

        self.pixmap = QPixmap(random.choice(list(BgsE)).value)

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
        self.move(random.randint(x - 3, x + 3), random.randint(y - 3, y + 3))

    def resizeEvent(self, event):
        self.atualizarFundo()
        return super().resizeEvent(event)
