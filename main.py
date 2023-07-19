import PyPDF2
from gtts import gTTS
import os
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt

nltk.download('punkt')

def read_pdf(filename):
    with open(filename, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        pages = []
        for page in range(num_pages):
            current_page = reader.pages[page]
            text = current_page.extract_text()
            tokens = word_tokenize(text)

            pages.append((text, tokens))

        return pages


def text_to_speech(text, words_to_highlight, filename):
    soup = BeautifulSoup(features="html.parser")
    p_tag = soup.new_tag("p")

    for word in word_tokenize(text):
        if word in words_to_highlight:
            span_tag = soup.new_tag("span")
            span_tag.string = word
            span_tag["style"] = "background-color: yellow"
            p_tag.append(span_tag)
        else:
            p_tag.append(word)
        p_tag.append(" ")

    soup.append(p_tag)
    highlighted_text = soup.get_text()

    tts = gTTS(highlighted_text, lang="es", slow=False)
    tts.save(filename)


class PDFReaderWindow(QMainWindow):
    def __init__(self, filename):
        super().__init__()
        self.setWindowTitle("PDF Reader")
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.highlight_action = QAction("Resaltar", self)
        self.highlight_action.setShortcut(Qt.Key_H)
        self.highlight_action.triggered.connect(self.highlight_text)
        self.text_edit.addAction(self.highlight_action)
        self.load_pdf(filename)

    def load_pdf(self, filename):
        pages = read_pdf(filename)
        for i, page_content in enumerate(pages):
            self.text_edit.append(f"=== Página {i+1} ===\n")
            self.text_edit.append(page_content[0])

    def highlight_text(self):
        selected_text = self.text_edit.textCursor().selectedText()
        cursor = self.text_edit.textCursor()
        format = cursor.charFormat()
        format.setBackground(Qt.yellow)
        cursor.mergeCharFormat(format)
        self.text_edit.setTextCursor(cursor)


def main():
    filename = "test.pdf"
    output_folder = "output"
    words_to_highlight = ["resaltar", "texto"]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pages = read_pdf(filename)

    for i, (page_content, page_tokens) in enumerate(pages):
        output_filename = os.path.join(output_folder, f"output_{i + 1}.mp3")
        text_to_speech(page_content, words_to_highlight, output_filename)
        os.system("mpg123 " + output_filename)

    app = QApplication([])
    window = PDFReaderWindow(filename)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
