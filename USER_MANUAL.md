# Manual de Usuario

## 1. Qué es YouTubeManager
`YouTubeManager` es una aplicación de consola para macOS que facilita:
- buscar y reproducir vídeos de YouTube online,
- descargar vídeos para reproducción offline,
- reproducir playlists de YouTube,
- ver el historial de reproducción,
- usar un asistente de IA integrado,
- gestionar los vídeos descargados localmente.

## 2. Requisitos previos
- Python instalado en el sistema.
- Firefox instalado en `/Applications/Firefox.app`.
- VLC instalado en `/Applications/VLC.app`.
- Archivo `.env` en la raíz del proyecto con la clave `YOUTUBE_API_KEY`.
- Opcional: `GROQ_API_KEY` en `.env` para usar la función de IA.

## 3. Cómo iniciar la aplicación
1. Abrir una terminal en la carpeta raíz del proyecto.
2. Activar entorno virtual si se utiliza uno (opcional).
3. Ejecutar:
   ```bash
   python main.py
   ```

## 4. Menú principal
Al iniciar, se muestra un menú con las siguientes opciones:

1. `Ver vídeo en YouTube`
   - Permite buscar un vídeo o reproducir una playlist.
   - Si eliges buscar, escribe los términos de búsqueda y selecciona el vídeo por número.
   - Si eliges playlist, el sistema pedirá pegar URLs en `data/playlist.txt`.
   - Después puede reproducirse online o descargarse offline.

2. `Usar IA`
   - Lanza el asistente IA definido en `bot/bot/src/paquete/main.py`.
   - Comandos disponibles:
     - `salir`
     - `configurar temperatura`
   - Requiere `GROQ_API_KEY` en `.env`.

3. `Historial`
   - Muestra el contenido de `data/historial.json`.
   - El historial registra cada vídeo reproducido online con título, URL y duración.

4. `Ver vídeos en local`
   - Reproduce archivos descargados desde `utils/descargas_youtube` usando VLC.

5. `Borrar vídeos en local`
   - Elimina la carpeta `utils/descargas_youtube` y su contenido.

6. `Reproducir playlist de YouTube`
   - Pide la URL de una playlist y reproduce los vídeos en Firefox.

7. `Salir`
   - Cierra la aplicación.

## 5. Uso de playlists
- El archivo `data/playlist.txt` debe contener una URL de YouTube por línea.
- La opción de playlist en el buscador guarda estas URLs y permite reproducirlas en bloque.

## 6. Historial de reproducción
- El historial se guarda en `data/historial.json`.
- Si el archivo no existe, `main.py` lo crea automáticamente al arrancar.
- La opción `Historial` imprime cada entrada con título, URL y duración.

## 7. Descargas offline
- Cuando se selecciona descarga offline, los vídeos se guardan en `utils/descargas_youtube`.
- El componente de descarga usa `yt_dlp`.
- La aplicación puede deshabilitar temporalmente SSL para que la descarga funcione correctamente en algunos entornos.

## 8. Notas especiales
- El proyecto está diseñado para macOS y usa rutas fijas para Firefox y VLC.
- Si una de esas aplicaciones no está instalada en la ruta esperada, la reproducción no funcionará.
- Si no existe `YOUTUBE_API_KEY` en `.env`, la aplicación no se iniciará.
- El modo IA usa la API de OpenAI/Groq y requiere clave propia.

## 9. Buenas prácticas de uso
- Mantén las claves de API en `.env` y no las compartas.
- Asegúrate de que `data/playlist.txt` sólo contiene URLs válidas de YouTube.
- Elimina vídeos descargados por seguridad y espacio cuando ya no sean necesarios.
