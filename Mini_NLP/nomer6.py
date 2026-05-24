import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone() as input_source:
    print("Hello Novandy, silahkan bicara")
    voice_input = listener.listen(input_source)
    
    # recognize_google dengan bahasa Indonesia
    text = listener.recognize_google(voice_input, language="id-ID")
    print("Anda bilang:", text)