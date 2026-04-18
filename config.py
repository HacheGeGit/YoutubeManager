from dotenv import load_dotenv
import os
from pathlib import Path
import sys

######################
#        Rutas       #
######################

BASE_DIR = Path(__file__).resolve().parent
PLAYLIST_PATH = BASE_DIR / "data" / "playlist.txt"
DESCARGAS_DIR = BASE_DIR / "utils" / "descargas_youtube"
HISTORIAL_JSON = BASE_DIR / "data" / "historial.json"

######################
# Variables globales #
######################

lista_videos = []
lista_bool = False
uri_video = ""

####################################
# Configuración de la clave de dev #
####################################

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

if not YOUTUBE_API_KEY:
    raise ValueError("No se encontró YOUTUBE_API_KEY en .env")