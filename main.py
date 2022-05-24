from art import tprint
from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', language='ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'File exits!'
        print(f'(+) Original file: {Path(file_path).name}')
        print(f'(+) Processing...')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        # with open('text1.txt', 'w') as file:
        #     file.write(text)

        text = text.replace('\n', '')

        # with open('text2.txt', 'w') as file:
        #     file.write(text)

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'(+) {file_name}.mp3 saved successfully!\n---Have a good day!---'

    else:
        return 'File not exits, check the file path!'


def main():
    tprint('PDF>>TO>>MP3', font='buldhead')
    file_path = input('\nEnter a file\'s path: ')
    language = input('Choose language, for example "en" or "ru": ')
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()