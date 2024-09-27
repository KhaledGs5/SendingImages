import speech_recognition as sr
import pyttsx3
import pywhatkit


class Alexa:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.listener = sr.Recognizer()

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def take_command(self):
        command = ""
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the request: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return command
      
    def run_alexa(self):
          command = ""
          self.talk("what the muique you need to listen")
          command = self.take_command()
          self.talk('playing ' + command)
          pywhatkit.playonyt(command)
 

