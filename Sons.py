from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

import BG

sons = {}
audios = {}


def carregar_sons():
    sons["comeca"] = QSoundEffect()
    sons["comeca"].setSource(QUrl.fromLocalFile(BG.caminho_recurso("sons/Untitled.wav")))
    sons["comeca"].setVolume(1.0)

    sons["ganhou"] = QSoundEffect()
    sons["ganhou"].setSource(QUrl.fromLocalFile(BG.caminho_recurso("sons/ganhou.wav")))
    sons["ganhou"].setVolume(1.0)

    audio = QAudioOutput()
    audio.setVolume(1.0)
    audios["fundo"] = audio
    sons["fundo"] = QMediaPlayer()
    sons["fundo"].setAudioOutput(audio)
    sons["fundo"].setSource(QUrl.fromLocalFile(BG.caminho_recurso("sons/fundo.mp3")))


def tocar_som(nome):
    som = sons.get(nome)

    if som is not None:
        som.play()


def parar_som(nome):
    som = sons.get(nome)

    if som is not None:
        som.stop()
