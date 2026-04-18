import subprocess
import os
from time import sleep

def reproducir_local(carpeta):
    if not os.path.exists(carpeta):
        print("No existe la carpeta de descargas")
        sleep(3)
        return
        
    videos = [f for f in os.listdir(carpeta)
          if f.endswith((".mp4", ".webm"))]
    
    for v in videos:
        path = os.path.join(carpeta, v)

        subprocess.run([
            "/Applications/VLC.app/Contents/MacOS/VLC",
            "--play-and-exit",
            path
        ])