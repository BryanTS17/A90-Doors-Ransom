import ctypes
import winreg
from pathlib import Path

CHAVE_WALLPAPER = r"Control Panel\Desktop"


def obter_wallpaper_atual():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, CHAVE_WALLPAPER) as chave:
        return winreg.QueryValueEx(chave, "WallPaper")[0]


def mudar_wallpaper(caminho):
    caminho = str(Path(caminho).resolve())

    resultado = ctypes.windll.user32.SystemParametersInfoW(
        20,  # SPI_SETDESKWALLPAPER
        0,
        caminho,
        3,  # atualiza a configuração e transmite a mudança
    )

    if not resultado:
        raise OSError("Não foi possível mudar o wallpaper.")


def restaurar_wallpaper(caminho_original):
    mudar_wallpaper(caminho_original)
