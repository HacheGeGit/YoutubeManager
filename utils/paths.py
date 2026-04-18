from pathlib import Path
import sys
import os

def base_path():
    if getattr(sys, "frozen", False):
        # Ejecutable PyInstaller
        return Path(sys._MEIPASS)
    else:
        # Desarrollo
        return Path(__file__).resolve().parent