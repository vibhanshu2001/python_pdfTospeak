# python program to convert a pdf to speaking one.
import pyttsx3
import PyPDF2


book=open('oop.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
# total number of pages: pages
pages=pdfReader.numPages

speaker = pyttsx3.init()
# to make the bot to speak all the pages we apply for loop
for num in pages:
    page =pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
# to make the bot speak some of the pages in given range
# for num in range(7, pages):
#     page =pdfReader.getPage(7)
#     text = page.extractText()
#     speaker.say(text)
#     speaker.runAndWait()
