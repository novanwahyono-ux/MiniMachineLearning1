import speech_recognition as sr

listener = sr.Recognizer()

print("=== PROGRAM SPEECH RECOGNITION (bahasa Indonesia) ===")

with sr.Microphone() as source:
    # Input suara nama
    print("Silakan sebutkan nama Anda...")
    voice_nama = listener.listen(source)
    nama = listener.recognize_google(voice_nama, language="id-ID")
    print(f"Baik {nama}, silakan sebutkan hobi Anda...")   # output text sesuai flowchart

    # Input suara hobi
    voice_hobi = listener.listen(source)
    hobi = listener.recognize_google(voice_hobi, language="id-ID")
    print(f"Wow, hobi anda adalah {hobi}")

    # Output akhir
    print("Terima kasih")