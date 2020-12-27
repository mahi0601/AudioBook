#importing Google text to speech library and PDF conversion library
from gtts import gTTS

import PyPDF2


text= "welcome to the audiobook "


pdfFileObj = open('a.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

total_pages= pdfReader.numPages

for i in range(0, int(total_pages)):
     pageObj = pdfReader.getPage(i)
     text+= pageObj.extractText()

tts= gTTS(text=text) 

tts.save("sound.mp3")
pdfFileObj.close()
