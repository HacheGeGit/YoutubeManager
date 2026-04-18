'''from pytube import YouTube 

def descargar(uri, path):
     try:
          uri_descarga = uri
          json = YouTube(uri_descarga)
          yt = json.streams.get_highest_resolution()
          yt.download(path)
          print(f"Descarga de {json.title} completada.")
     except Exception as e:
          print(f'Error al descargar el video {json.title}: {str(e)}')
     return path'''

import yt_dlp

def descargar(url, path):
    ydl_opts = {
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



