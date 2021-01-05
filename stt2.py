import speech_recognition as sr

r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, 1)
    print("say anything : ")
    audio= r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("sorry, could not recognise")