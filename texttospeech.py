import gtts
import playsound

# Hello, Welcome to WsCube Tech. How may I help you?
# Ganapati Bappa Morya
# Ganapati Bappa Morya, Pudhchya Varshi Lavkar Ya.
# Hello
# Resume
# Namaskar
text = input("Enter something here : ")
# sound = gtts.gTTS(text, lang="en")
# sound = gtts.gTTS(text, lang="fr")
# sound = gtts.gTTS(text, lang="hi")
sound = gtts.gTTS(text, lang="mr")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")
