import pyttsx3
import PyPDF2

# pip install pyttsx3
# pip install pypdf
# pip install PyPDF2

# https://royalsociety.org/
# https://royalsociety.org/-/media/policy/projects/climate-evidence-causes/climate-change-evidence-causes.pdf

melo = pyttsx3.init()

file = open("climate_change.pdf", mode="rb")
# pdf_reader = PyPDF2.PdfFileReader(file)
pdf_reader = PyPDF2.PdfReader(file)
# pages = pdf_reader.numPages
pages = pdf_reader.pages
print(len(pages))

# page = pdf_reader.getPage(6)
# page = pdf_reader.pages[6]
#text = page.extractText()
#for i in range(2, pages):
for i in range(2, len(pages)):
    page = pdf_reader.pages[2]
    text = page.extract_text()

    melo.say(text)
    # melo.say("Welcome to WSCube Tech")
    melo.runAndWait()