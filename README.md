# YouTubeManager

YouTubeManager es una aplicación de línea de comandos (CLI) desarrollada en Python que permite gestionar la reproducción de vídeos y playlists de YouTube de manera automatizada. Ideal para desarrolladores y usuarios que prefieren trabajar desde la terminal sin distracciones del navegador.

## Características

- **Búsqueda de vídeos**: Busca vídeos en YouTube directamente desde la terminal.
- **Reproducción automática**: Reproduce vídeos en Firefox con autoplay y cierra las pestañas automáticamente.
- **Descarga offline**: Descarga vídeos para reproducción local con VLC.
- **Gestión de playlists**: Importa y reproduce playlists completas de YouTube.
- **Historial**: Guarda un registro JSON de los vídeos reproducidos.
- **Asistente IA**: Incluye un chatbot integrado para consultas relacionadas.
- **Interfaz CLI**: Ligera y rápida, perfecta para entornos de desarrollo.

## Requisitos

- Python 3.8 o superior
- macOS (diseñado para macOS con rutas fijas a aplicaciones)
- Firefox instalado en `/Applications/Firefox.app`
- VLC instalado en `/Applications/VLC.app`
- Conexión a Internet para búsquedas y descargas

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/YouTubeManager.git
   cd YouTubeManager
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto:
   ```env
   YOUTUBE_API_KEY=tu_clave_de_api_de_youtube
   GROQ_API_KEY=tu_clave_groq_opcional
   ```

2. Obtén una `YOUTUBE_API_KEY` desde la [Consola de Google Cloud](https://console.cloud.google.com/):
   - Crea un proyecto.
   - Activa la API de YouTube Data v3.
   - Genera una clave de API.

3. Para la función IA, obtén una `GROQ_API_KEY` desde [Groq](https://groq.com/).

## Uso

Ejecuta la aplicación:
```bash
python main.py
```

### Menú principal
1. **Ver vídeo en YouTube**: Busca o reproduce playlists online.
2. **Usar IA**: Interactúa con el asistente conversacional.
3. **Historial**: Muestra el historial de reproducción.
4. **Ver vídeos en local**: Reproduce vídeos descargados con VLC.
5. **Borrar vídeos en local**: Elimina la carpeta de descargas.
6. **Reproducir playlist de YouTube**: Reproduce una playlist completa.
7. **Salir**: Cierra la aplicación.

### Ejemplos de uso
- Para buscar un vídeo: Selecciona opción 1, elige "y" para buscador, escribe términos y selecciona el vídeo.
- Para reproducir una playlist: Selecciona opción 1, elige "p", pega URLs en `data/playlist.txt`.
- Para descargar: Elige opción 2 (offline) después de seleccionar vídeos.

## Estructura del proyecto

```
YouTubeManager/
├── main.py                 # Punto de entrada y menú principal
├── config.py               # Configuraciones y rutas
├── requirements.txt        # Dependencias
├── .env                    # Variables de entorno (no subir a Git)
├── data/
│   ├── playlist.txt        # Lista de URLs para reproducción
│   └── historial.json      # Historial de reproducción
├── core/
│   ├── buscador.py         # Lógica de búsqueda en YouTube
│   ├── videos.py           # Reproducción y descarga de vídeos
│   ├── historial.py        # Gestión del historial
│   ├── playlist.py         # Manejo de playlists
│   └── reproductor_local.py # Reproducción local
├── utils/
│   ├── rutas.py            # Utilidades de rutas y archivos
│   ├── SSL_disabler.py     # Desactivación de SSL para descargas
│   ├── visor_json.py       # Visualización del historial
│   └── paths.py            # Definición de rutas
├── api/
│   └── API_Client.py       # Cliente de la API de YouTube
├── bot/
│   └── bot/src/paquete/    # Módulo del asistente IA
├── build/                  # Archivos de build (PyInstaller)
└── dist/                   # Distribuciones generadas
```

## Tecnologías utilizadas

- **Python 3**: Lenguaje principal.
- **YouTube Data API**: Para búsquedas y metadatos.
- **yt-dlp**: Para descarga de vídeos.
- **google-api-python-client**: Cliente de la API de Google.
- **openai**: Para el asistente IA (Groq).
- **python-dotenv**: Gestión de variables de entorno.
- **PyAutoGUI**: Automatización de interfaz.
- **subprocess**: Ejecución de comandos externos.
- **JSON**: Persistencia de datos.

## Contribución

1. Haz un fork del proyecto.
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`.
3. Haz commit de tus cambios: `git commit -am 'Añade nueva funcionalidad'`.
4. Push a la rama: `git push origin feature/nueva-funcionalidad`.
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Notas

- Diseñado específicamente para macOS.
- Requiere permisos para automatizar Firefox y VLC.
- Las claves de API deben mantenerse seguras y no subirse al repositorio.# YoutubeManager
