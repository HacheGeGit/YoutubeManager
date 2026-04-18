from .chatbot import TutorBot
import os
import sys
# Agrega src a sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

def main():
    
    temp = 0.7
    bot = TutorBot(temp)
    print("YouAITube - Opciones:")
    for comando in bot.comandos:
        print(comando)

    while True:
        mensaje = input("Tú: ")
        match mensaje.lower():
            case'salir':
                print("Bot: ¡Hasta luego!")
                break
            case 'configurar temperatura':
                t = bot.config_temperature()
                print(f'Temperatura configurada a {t} correctamente.')
                mensaje = input("Tú: ")

        respuesta = bot.responder(mensaje)
        print("Bot:", respuesta)

if __name__ == '__main__':
    main()