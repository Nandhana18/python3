import pyttsx3
import PyPDF2
book=open("story.pdf",'rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)
speaker=pyttsx3.init()
for num in range(1,pages):
    page = pdfreader.getPage(1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

