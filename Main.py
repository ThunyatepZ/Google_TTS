from gtts import gTTS
import playsound
TTS = gTTS(text='Hello World', lang='en')
TTS.save('Hello.mp3')
playsound.playsound('Hello.mp3', True)
