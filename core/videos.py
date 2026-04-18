import utils.rutas as rutas
import api.API_Client as API_Client
import core.historial as historial
import subprocess
import sys
import config

def leer_urls():
    print("Pega URLs (Ctrl+D para terminar en macOS/Linux):")
    texto = sys.stdin.read()
    urls = [line.strip() for line in texto.splitlines() if line.strip()]
    print("DEBUG RAW STDIN:", repr(texto))
    return urls

def guardar_urls_txt(archivo=config.PLAYLIST_PATH):
     print("\nPega URLs de YouTube")
     urls = []
     urls = leer_urls()
     with open(archivo, "w", encoding="utf-8") as f:
          for url in urls:
                    f.write(url.strip() + "\n")   

def convertir_tiempo(cadena):
     #print(cadena)
     cadena = cadena.replace('PT','')
     hora = 0
     minutos = 0
     segundos = 0
     lista_tiempo = []
     for i, caracter in enumerate(cadena):
          lista_tiempo.append(caracter)
     contador = -1
     for c in range(len(lista_tiempo)):
          contador+=1
          if lista_tiempo[c] == 'H':
               hora = cadena[0:contador].replace('H','')
               cadena = cadena[contador:].replace('H','')
               contador = 0
          if lista_tiempo[c] == 'M':
               minutos = cadena[0:contador].replace('M','')
               cadena = cadena[contador:].replace('M','')
               contador = 0
          if lista_tiempo[c] == 'S':
               segundos = cadena[0:contador].replace('S','')
               cadena = cadena[contador:].replace('S','')
               contador = 0
     tiempo_total = (int(hora)*60+int(minutos))*60+int(segundos)
     #print(f'El tiempo de reproducción del vídeo es: {str(hora).zfill(2)}:{str(minutos).zfill(2)}:{str(segundos).zfill(2)}')
     return tiempo_total

def data_video(video_id):
     #print(f'ID: {video_id}')
     response = API_Client.youtube.videos().list(part='contentDetails', id=video_id).execute()
     if not response['items']:
          print(f"Video inválido o no encontrado: {video_id}")
          return 0, ''
     response_name = API_Client.youtube.videos().list(part='snippet', id=video_id).execute()
     duracion_video = response['items'][0]['contentDetails']['duration']
     name = response_name['items'][0]['snippet']['title']
     '''print(f'Nombre del vídeo: {name}')
     print(type(name))'''
     tiempo_reproduccion = convertir_tiempo(duracion_video)
     return tiempo_reproduccion, name

def json_data(video_id):
     tiempo_reproducción, title = data_video(video_id)
     video = {
          "title": str(title),
          "url": f'www.youtube.es/watch?v={str(video_id)}',
          "duration": tiempo_reproducción
     }
     '''print(video)'''
     return video

def reproducir():
     placeholder = []
     if config.lista_bool != True:
          placeholder = config.lista_videos.copy()
     else:
          lista_videos = historial.leer_lista_reproduccion()
          placeholder = lista_videos.copy()
     for e in range(len(placeholder)):
          if config.lista_bool != True:
               video_id = placeholder[e][-11:]
          else:
               video_id = placeholder[e][0:11]
          
          r, name = data_video(video_id)

          if r == 0:
              print(f"Saltando vídeo inválido: {video_id}")
              continue

          subprocess.run(["/Applications/Firefox.app/Contents/MacOS/firefox", 
                          f"https://www.youtube.com/watch?v={video_id}&autoplay=1"]
                          )
          video_json = json_data(video_id)
          historial.escribir_json(video_json)
          rutas.sleep(r)
          rutas.cerrar()

if __name__ == "__main__":
    reproducir()
    
    