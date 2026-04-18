import utils.rutas as rutas
import core.buscador as buscador
import googleapiclient.discovery
import core.download_video as download_video
import api.API_Client as API_Client
import core.videos as videos
import utils.SSL_disabler as ssl
import sys
import os
import subprocess
import config
from core.historial import init_historial
from utils.visor_json import leer_json
from core.reproductor_local import reproducir_local
from core.playlist import get_playlist_videos

init_historial()

def menu():
     #print(API_Client.YOUTUBE_API_KEY)
     option_list = ['1.- Ver vídeo en YouTube:',
                    '2.- Usar IA.',
                    '3.- Historial.',
                    '4.- Ver vídeos en local.',
                    '5.- Borrar vídeos en local.',
                    '6.- Reproducir playlist de YouTube.',
                    '7.- Salir.']
     for o in option_list:
          print(o)
     try:
          o = int(input('Elija una opción: \n'))
     except ValueError:
          print("Entrada inválida")
          return
     if o not in (1,2,3,4,5,6,7):
          o = int(input('Elija una opción: \n'))
     match o:
          case 1:
               os.system('clear')
               flujo()
          case 2:
               os.system('clear') 
               base_dir = os.path.dirname(os.path.abspath(__file__))
               '''
               export PYTHONPATH=$(pwd)/srcpython3 -m paquete.main
               '''
               src_path = os.path.join(base_dir, "bot", "bot", "src")
               subprocess.run(
                    [sys.executable, "-m", "paquete.main"],
                    env={**os.environ, "PYTHONPATH": src_path})
          case 3:
               os.system('clear')
               leer_json()
          case 4:
               os.system('clear')
               reproducir_local(config.DESCARGAS_DIR)
          case 5:
               os.system('clear')
               rutas.borrar_videos(config.DESCARGAS_DIR)
          case 6:
               url = input("URL playlist: ")
               config.lista_videos = get_playlist_videos(url)
               videos.reproducir()
               config.lista_videos.clear()
          case 7:
               print('Programa finalizado.')
               exit(0)   
          case _:
               print('Opción inválida.')
               

def flujo():
     youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_Client.YOUTUBE_API_KEY)

     pregunta_al_user = input("¿Quieres reproducir una playlist o usar el buscador de youtube? p/y ")
     os.system('clear')

     if pregunta_al_user != "p":
          config.lista_bool = False
          while 1:
               uri = buscador.buscar()
               if uri == None:
                    continue
               print(uri)
               config.lista_videos.append(uri)
               i = input('¿Desea hacer otra búsqueda? s/n: ')
               if i != 's':
                    break
     else:
          config.lista_bool = True
          videos.guardar_urls_txt()
     try:
          quest_to_user = input('¿Desea ver los vídeos online(1) u offline(2)? : ')
     except ValueError:
          print("Entrada inválida")
          return
     while quest_to_user not in ('1','2'):
          quest_to_user = input('¿Desea ver los vídeos online(1) u offline(2)? : ')
     if quest_to_user == '1':
          videos.reproducir()
          config.lista_videos.clear()             
     else:
          # El protocolo SSL sólo se modifica en el de caso que se use pytube,
          # ya que no es necesario para cargar vídeos en el navegador, pero sí
          # para hacer las descargas.
          ssl.disable_SSL()
          path_archivos = rutas.crear_ruta()
          for i in range(len(config.lista_videos)):
               print(config.lista_videos[i])
               uri = config.lista_videos[i]
               download_video.descargar(uri, path_archivos)
          rutas.abrir_ruta(path_archivos)
          config.lista_videos.clear()
     os.system('clear')
     
if __name__ == '__main__':
     while 1:
          menu()
          
          