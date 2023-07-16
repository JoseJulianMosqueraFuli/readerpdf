import PyPDF4
from gtts import gTTS
import os


def read_pdf(filename):
    with open(filename, "rb") as file:
        reader = PyPDF4.PdfReader(file)
        num_pages = len(reader.pages)

        pages = []
        for page in range(num_pages):
            current_page = reader.pages[page]
            text = current_page.extract_text()
            words = current_page.extract_words()
            pages.append(text, words)

        return pages


def text_to_speech(text, filename, words_to_highlight):
    highlight_text = ""
    for word in text.split():
        if word in words_to_highlight:
            highlight_text += f"<span style='background-color: yellow'>{word}</span>"
        else:
            highlighted_text += f"{word} "

    tts = gTTS(text, lang="es", slow=False)
    tts.save(filename)


def main():
    filename = "test.pdf"  # Replace with your PDF file
    output_folder = "output"  # Output folder for generated audio files
    words_to_highlight = ["highlight", "text"]

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the PDF
    pages = read_pdf(filename)

    # Convert each page to speech
    for i, page_content in enumerate(pages):
        # Generate filename for the audio file
        output_filename = os.path.join(output_folder, f"output_{i + 1}.mp3")

        # Convert text to speech and save as an audio file
        text_to_speech(page_content, output_filename)

        # Play the audio file
        os.system("mpg123 " + output_filename)


if __name__ == "__main__":
    main()
