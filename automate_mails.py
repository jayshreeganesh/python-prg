import smtplib
# import speech_recognition
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3

# pip install secure-smtplib
# pip install pyttsx3
# pip install playsound
# pip install playsound3
# pip install playsound==1.2.2
# pip install PyAudio

listener = sr.Recognizer()
tts = pyttsx3.Engine()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()

def mic():
    with sr.Microphone() as source:
        print("Program is listening...")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        # print(data)
        return data.lower()

dict = {"jojo":"jo141004.jo@gmail.com"}

def send_mail(receiver, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 578)
    server.starttls()
    # server.login("coco1410014@gmail.com","ayushiwscube")
    server.login("coco1410014@gmail.com","iqrmknfbpxifweho")
    # server.sendmail("coco1410014@gmail.com","joe141004.jo@gmail.com","hey there")
    email = EmailMessage()
    email["From"] = "coco1410014@gmail.com"
    # email["To"] = "jo141004.jo@gmail.com"
    email["To"] = receiver
    # email["Subject"] = "text"
    email["Subject"] = subject
    email.set_content("text")
    server.send_message(email)

def main_poc():
    talking_tom("To whom do you want to send this email")
    name = mic()
    receiver = dict[name]
    talking_tom("Speak the subject of the email")
    subject = mic()
    talking_tom("Speak the message of the email")
    body = mic()
    send_mail(receiver, subject, body)
    print("Your email has been sent!!")

main_poc()
