import core.historial as historial
from core.videos import convertir_tiempo
import api.API_Client as API_Client
import os
from config import uri_video

def buscar():
     cadena_busqueda = input('Introduce lo que quieras buscar: ')
     query = cadena_busqueda
     page_token = None
     while 1:
      result = API_Client.youtube.search().list(
         q=query, 
         part='snippet', 
         type='video', 
         maxResults=5, 
         pageToken=page_token
      ).execute()

      lista_uris = []
      lista_nombres = [] 
      lista_duraciones = []
      for item in result['items']: 
         if 'videoId' in item['id']:
            video_id = item['id']['videoId']
            lista_uris.append(video_id)

            response = API_Client.youtube.videos().list(
                  part='snippet,contentDetails',
                  id=video_id
            ).execute()

            nombre = response['items'][0]['snippet']['title']
            duracion = response['items'][0]['contentDetails']['duration']

            tiempo = convertir_tiempo(duracion)

            lista_nombres.append(nombre)
            lista_duraciones.append(tiempo)
      print()
       
      for i in range(len(lista_nombres)):
         minutos = lista_duraciones[i] // 60
         segundos = lista_duraciones[i] % 60
         
         print(
            f"Resultado número {i+1}: {lista_nombres[i]} "
            f"({str(minutos).zfill(2)}:{str(segundos).zfill(2)})\n"
         )

      print("6. Siguiente página")
      print("7. Página anterior")
      print("0. Cancelar")
      try:
         eleccion_video = int(input('¿Qué vídeo quieres? Escribe el número: '))
      except ValueError:
         print("Entrada inválida")
         return
      if eleccion_video not in (1,2,3,4,5,6,7,0):
          eleccion_video = int(input('¿Qué vídeo quieres? Escribe el número: '))
      if eleccion_video == 6:
         os.system('clear')
         page_token = result.get("nextPageToken")
         if not page_token:
               print("No hay más resultados")
         continue
      if eleccion_video == 7:
         os.system('clear')
         page_token = result.get("prevPageToken")
         if not page_token:
                print("No hay página anterior")
      elif eleccion_video == 0:
         os.system('clear')
         return None
      elif 1<= eleccion_video <= len(lista_uris):
         video_id_q = lista_uris[eleccion_video-1]
         uri_video = f"https://www.youtube.com/watch?v={video_id_q}"
         return uri_video
      else:
         print("Opción no válida")
         continue

if __name__ == "__main__":
    buscar()