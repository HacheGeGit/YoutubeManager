from .config import GROQ_API_KEY
from .memory import Memory
from openai import OpenAI
from .prompts import SYSTEM_PROMPT 

class TutorBot:
    def __init__(self,temperature: float = 0.7):
        self.client = OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")
        self.memory = Memory()
        self.memory.historial.append(SYSTEM_PROMPT)
        self.temperature = temperature
        self.comandos = ['salir', 'configurar temperatura']

    def config_temperature(self):
        temperaturas = ['0.0	Muy determinista, respuestas repetitivas: Tutoriales, respuestas técnicas exactas',
                        '0.3	Bastante preciso, un poco flexible: Tutor académico serio',
                        '0.7	Equilibrado, creativo pero coherente: Conversación natural / tutor “amigable”',
                        '1.0	Muy creativo, a veces inventa cosas: Chat informal, generación de ideas',
                        '>1.0	Respuestas muy impredecibles: Experimentos o humor'
                    ]
        for o in temperaturas:
            print(o)
        while 1:
            try:
                temperature = float(input('Seleccione la temperatura del modelo (0.0-1.0): '))
                if 0.0 <= temperature <= 1.0:
                    return temperature
                else:
                    print("Debe estar entre 0.0 y 1.0")
            except ValueError:
                print('Introduce un número entre 0.0 y 1.0')
        return temperature
    def responder(self, mensaje: str) ->str:
        self.memory.agregar_usuario(mensaje)
        #temperature = self.config_temperature()
        respuesta = self.client.chat.completions.create(
            model = "llama-3.1-8b-instant", # Modelo con ~7000 peticiones/día
            messages = self.memory.obtener_historial(),
            temperature=self.temperature, # Control de respuestas
            max_tokens=1000          
        )
        contenido = respuesta.choices[0].message.content
        self.memory.agregar_asistente(contenido)
        return contenido
