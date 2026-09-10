from BG import Bgs
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import BG
from Label import ImagemClicavel
import random


class JanelaThank(QWidget):
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

        self.pixmap = QPixmap(
            BG.caminho_recurso("imagens\\Captura de tela 2026-09-08 204346.png")
        )

        self.fundo.setPixmap(self.pixmap)
        self.fundo.resize(self.size())

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
