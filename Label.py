from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal


class ImagemClicavel(QLabel):
    clicado = Signal()

    def mousePressEvent(self, event):
        self.clicado.emit()
        super().mousePressEvent(event)
