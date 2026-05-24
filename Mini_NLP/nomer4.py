import pyttsx3

engine = pyttsx3.init()

# 4a. Bahasa Indonesia
engine.setProperty('voice', 'id')

# 4b. Tempo suara lebih cepat 70
engine.setProperty('rate', 70)

# 4c. Volume lebih pelan 50%
engine.setProperty('volume', 0.5)

# 4d. Ubah menjadi suara perempuan
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Selamat pagi, saya sedang belajar pemrosesan bahasa alami")
engine.runAndWait()