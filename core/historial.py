from config import PLAYLIST_PATH, HISTORIAL_JSON
import json
from core.videos import json_data

def init_historial():
    if not HISTORIAL_JSON.exists():
        data = {"videos": []}
        with open(HISTORIAL_JSON, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

def leer_json():
     try:
        with open(HISTORIAL_JSON, "r", encoding="utf-8") as f:
          return json.load(f)  
     except FileNotFoundError:
        data = {"videos": []}  
     return data

def escribir_json(data_video):
     data = leer_json()

     if "videos" not in data:
          data["videos"] = []

     data["videos"].append(data_video)

     with open(HISTORIAL_JSON, "w", encoding="utf-8") as f:
          json.dump(data, f, indent=4)

def write_dict(video_id):
     data = leer_json()
     
     video = json_data(video_id)
     
     data["videos"].append(video)
     return data

def json_to_dict():
     pass

#---- Fichero lista de repro con txt ------

def contar_elementos_txt():
     import os
     print("DEBUG CWD:", os.getcwd())
     print("DEBUG FILE EXISTS:", os.path.exists(PLAYLIST_PATH))
     try:
          txt = open(PLAYLIST_PATH,'r')
          txt.seek(0)
          counter = (len(txt.readlines()))
     finally:
          txt.close()
     return counter

def crear_lista_txt(counter):
     lista_reproduccion = []
     try:
          txt = open(PLAYLIST_PATH,'r')
          txt.seek(0)
          for i in range(counter):
               video_id = txt.readline()
               print(video_id)
               lista_reproduccion.append(video_id[-12:].strip())
               for v in lista_reproduccion:
                    print(v)
     finally:
          txt.close()
     return lista_reproduccion

def leer_lista_reproduccion():
     counter = contar_elementos_txt()
     lista_reproduccion = crear_lista_txt(counter)
     return lista_reproduccion