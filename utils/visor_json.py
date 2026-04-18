import json
from config import HISTORIAL_JSON

def leer_json():
    with open(HISTORIAL_JSON , "r", encoding="utf-8") as f:
        data = json.load(f)
    for video in data["videos"]:
        print("---")
        print(video["title"])  
        print(video["url"])
        print(video["duration"])
        print("---")

