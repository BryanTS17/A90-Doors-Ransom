from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl, Qt, Signal


class JanelaVideo(QWidget):
    terminou = Signal()

    def __init__(self, caminho_video):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.setWindowTitle("RANS0M")

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )

        self.video = QVideoWidget(self)

        self.player = QMediaPlayer(self)
        self.audio = QAudioOutput(self)

        self.player.setAudioOutput(self.audio)
        self.player.setVideoOutput(self.video)

        self.player.mediaStatusChanged.connect(self.verificar_fim)

        self.player.setSource(QUrl.fromLocalFile(caminho_video))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.video)

        # Tela cheia
        self.showFullScreen()

        self.player.play()

    def keyPressEvent(self, event):
        # Esc sai da tela cheia e fecha o vídeo
        if event.key() == Qt.Key.Key_Escape:
            self.player.stop()
            self.close()
        else:
            super().keyPressEvent(event)

    def verificar_fim(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.player.stop()
            self.terminou.emit()
            self.close()
