# Manual de Despliegue

## 1. Propósito
Este documento describe cómo preparar y desplegar `YouTubeManager` en un entorno local de macOS. La aplicación no está diseñada como servicio web: su despliegue es la instalación y ejecución local en un equipo compatible.

## 2. Requisitos de sistema
- macOS compatible.
- Python 3 instalado.
- Firefox instalado en `/Applications/Firefox.app`.
- VLC instalado en `/Applications/VLC.app`.
- Conexión a Internet para búsquedas y descargas.

## 3. Dependencias del proyecto
El proyecto requiere los paquetes listados en `requirements.txt`:
- `certifi`
- `google_api_python_client`
- `openai`
- `PyAutoGUI`
- `python-dotenv`
- `yt_dlp`

## 4. Preparar el entorno
1. Clona o copia el proyecto en el equipo.
2. En la raíz del proyecto, crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 5. Configuración de variables de entorno
Crea un archivo `.env` en la raíz del proyecto con al menos:
```env
YOUTUBE_API_KEY=tu_clave_de_api_de_youtube
```

Opcionalmente, para usar la función IA, crea otro archivo `.env` en la carpeta `bot/bot/src/paquete/` con:
```env
GROQ_API_KEY=tu_clave_groq
```

Nota: Mantén los archivos `.env` separados para evitar confusiones entre las claves de diferentes servicios.

## 6. Configuración opcional de la IA
Si deseas cambiar el modelo de IA usado por Groq API (por defecto es `llama-3.1-8b-instant`):
1. Edita el archivo `bot/bot/src/paquete/chatbot.py`.
2. En la línea donde se define `model = "llama-3.1-8b-instant"`, cambia el valor por otro modelo soportado por Groq (ej. `mixtral-8x7b-32768` o `gemma-7b-it`).
3. Consulta la documentación de Groq para ver modelos disponibles: https://console.groq.com/docs/models

Nota: Asegúrate de que el modelo elegido sea compatible con la API de OpenAI usada en el código.

## 7. Verificación previa al despliegue
- Asegúrate de que las rutas a Firefox y VLC son correctas.
- Comprueba que el archivo `.env` en la raíz existe y contiene la clave `YOUTUBE_API_KEY`.
- Si usas IA, verifica que el archivo `.env` en `bot/bot/src/paquete/` existe y contiene `GROQ_API_KEY`.

## 8. Cómo generar una API Key de YouTube
1. Abre la Consola de Google Cloud: https://console.cloud.google.com/
2. Crea o selecciona un proyecto existente.
3. Activa la API de YouTube Data v3.
4. En el menú de APIs y servicios, selecciona "Credenciales".
5. Crea una nueva clave de API.
6. Copia la clave generada y pégala en `.env` como `YOUTUBE_API_KEY`.

Ayuda adicional:
- Documentación de Google Cloud: https://developers.google.com/youtube/v3

## 9. Ejecución del proyecto
Desde la carpeta raíz del proyecto, ejecuta:
```bash
python main.py
```

## 10. Consideraciones de producción
- La aplicación se ejecuta como programa de consola; no hay servidor web.
- Protege las claves en `.env` y evita subirlas a repositorios públicos.
- Concede permisos a `pyautogui` si macOS solicita acceso para automatización.
- Revisa las rutas de aplicaciones macOS si el usuario tiene instalación en ubicaciones distintas.

## 11. Directorios clave
- `data/playlist.txt`: playlist local de URLs de YouTube.
- `data/historial.json`: historial de reproducción.
- `utils/descargas_youtube`: carpeta donde se guardan los vídeos descargados.

## 12. Tareas comunes de despliegue
1. Instalar Python y las aplicaciones necesarias.
2. Crear y activar entorno virtual.
3. Instalar dependencias.
4. Crear `.env` con claves válidas.
5. Ejecutar `python main.py`.
6. Probar las opciones del menú para confirmar que Firefox y VLC se lancen correctamente.

## 13. Notas finales
- Este proyecto está pensado para uso local en macOS.
- No incluye un flujo de despliegue a servidores ni contenedores.
- Para ejecutar en otro sistema operativo, adapta las rutas a Firefox y VLC manualmente.
