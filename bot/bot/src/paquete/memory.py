class Memory:
    def __init__(self):
        self.historial = []

    def agregar_usuario(self, mensaje):
        self.historial.append({"role": "user", "content": mensaje})

    def agregar_asistente(self, mensaje):
        self.historial.append({"role": "assistant", "content": mensaje})

    def obtener_historial(self):
        return self.historial