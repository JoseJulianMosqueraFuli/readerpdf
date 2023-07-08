from gtts import gTTS
import os


def text_to_speech(text, filename):
    tts = gTTS(text, lang="es", slow=False)
    tts.save(filename)


if __name__ == "__main__":
    text = "Hola mundo"  # Replace with your desired text
    filename = "output.mp3"  # Output file name

    text_to_speech(text, filename)
    os.system("mpg123 " + filename)
