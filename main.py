import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()
num_of_pages = len(pdfreader.pages)

for page_num in range(num_of_pages):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()