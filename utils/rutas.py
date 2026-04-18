import os
from shutil import rmtree
import subprocess
import pyautogui as pyg
from time import sleep

def cerrar():
    subprocess.run(["open", "-a", "Firefox"])
    with pyg.hold('command'):
          sleep(1)
          pyg.press('9') 
    with pyg.hold('command'):
          sleep(1)
          pyg.press('w')

def crear_ruta():
     path = os.path.dirname(__file__)
     path = path + '/descargas_youtube'
     os.makedirs(path, exist_ok=True)
     return path

def abrir_ruta(path):
     try:
          os.system(f'open {path}')
     except Exception as e:
          print(f'Error al abrir la ubicación de la carpeta {str(e)}')

def borrar_videos(path_archivos):
     try:
          rmtree(path_archivos)
     except Exception as e:
          print(f'Error al borrar la carpeta{path_archivos}: {str(e)}')