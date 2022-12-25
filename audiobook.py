import pyttsx3
import PyPDF2

with open("D://RentAgreement//Yashwin Encore A1-1803 Rent Agreement.pdf", "rb") as book:

    full_text = ""
    reader = PyPDF2.PdfReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 100)

    for page in range(len(reader.pages)):
        next_page = reader.pages[page]
        content = next_page.extract_text()
        full_text += content

        audio_reader.save_to_file(full_text,"myaudiobook.mp3")
        audio_reader.runAndWait()
