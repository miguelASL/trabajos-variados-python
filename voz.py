import speech_recognition as sr # Esta librería es para reconocimiento de voz
import subprocess # Esta librería es para ejecutar comandos en la terminal
import pyautogui # Esta librería es para simular acciones del teclado

# Crear una clase que se encargue de ejecutar los comandos
class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.process = None
        self.commands = {
            "abrir notepad": self.open_notepad,
            "Como estan los maquinas ??": self.greet_followers,
            "cerrar notepad": self.close_notepad
        }
        self.saludo = """
        Holi familia !!!
        """
        
    # Crear un método para cada comando           
    def open_notepad(self):
        self.process = subprocess.Popen(["notepad.exe"])
        
    # Crear un método para saludar a los seguidores
    def greet_followers(self):
        pyautogui.write(self.saludo)

    # Crear un método para cerrar el notepad
    def close_notepad(self):
        if self.process:
            self.process.terminate()
            
    # Crear un método para ejecutar el comando
    def execute_command(self, command):
        func = self.commands.get(command)
        if func:
            func()
    # Crear un método para escuchar el comando
    def listen_command(self):
        with sr.Microphone() as source:
            print("Escuchando...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language="es-ES")
            except sr.UnknownValueError:
                print("No te he entendido")
            except sr.RequestError as e:
                print(f"No se ha podido obtener una respuesta del servicio de Google Speech Recognition; {e}")
            else:
                print(f"Comando: {text}")
                self.execute_command(text)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    while True:
        assistant.listen_command()
    