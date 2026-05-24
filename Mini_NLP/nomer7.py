from gtts import gTTS
from playsound import playsound

# Input sesuai flowchart
nama = input("Masukkan nama Anda: ")

# Suara 1
tts1 = gTTS(text=f"Baik {nama}, silakan menulis menu selanjutnya", lang='id', slow=False)
tts1.save("suara1.mp3")
playsound("suara1.mp3")

# Input hobi
hobi = input("Masukkan hobi Anda: ")

# Suara 2
tts2 = gTTS(text=f"Wow, hobi anda adalah {hobi}", lang='id', slow=False)
tts2.save("suara2.mp3")
playsound("suara2.mp3")

# Suara akhir (Terima kasih)
tts3 = gTTS(text="Terima kasih", lang='id', slow=False)
tts3.save("terima_kasih.mp3")
playsound("terima_kasih.mp3")

print("Program selesai.")