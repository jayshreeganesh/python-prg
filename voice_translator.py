import googletrans
import speech_recognition
import gtts
import playsound

# pip install googletrans==3.1.0a0
# pip install googletrans==3.1.0a0
# pip install SpeechRecognition
# pip install PyAudio
# pip install gTTS
# pip install playsound
# pip install playsound==1.2.2

input_lang = "hi"
output_lang = "fr"

# print(googletrans.LANGUAGES)

recognizer = speech_recognition.Recognizer()
# with speech_recognition.Microphone as source:
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice = recognizer.listen(source)
    # text = recognizer.recognize_google(voice, language="en")
    # text = recognizer.recognize_google(voice, language="hi")
    text = recognizer.recognize_google(voice, language=input_lang)
    print(text)

translator = googletrans.Translator()
# translation = translator.translate("hello", dest="fr")
# translation = translator.translate(text, dest="fr")
# translation = translator.translate(text, dest="en")
translation = translator.translate(text, dest=output_lang)
print (translation.text)

# converted_audio = gtts.gTTS(translation.text, lang="fr")
# converted_audio = gtts.gTTS(translation.text, lang="en")
converted_audio = gtts.gTTS(translation.text, lang=output_lang)
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")