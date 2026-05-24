from gtts import gTTS
from playsound import playsound

tts = gTTS(text='Good morning, i am studying natural language processing', lang='en', slow=False)
tts.save("morning.mp3")
playsound("morning.mp3")