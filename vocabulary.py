import os
import requests
import re


class Vocabulary:
    DATA_FOLDER = "data"
    SPANISH_WORDS_FILE = "10000_formas.TXT"
    SPANISH_WORDS_URL = f"http://corpus.rae.es/frec/{SPANISH_WORDS_FILE}"
    SPANISH_WORDS_PATTERN = '^\s+[0-9]+\.\s+([a-zA-Záóúíéñ]+).*$'

    def __init__(self):
        self.data_path = self.DATA_FOLDER
        self.vocabulary_file = self.SPANISH_WORDS_FILE
        self.vocabulary_url = self.SPANISH_WORDS_URL
        self.parsing_pattern = self.SPANISH_WORDS_PATTERN
        self.words = []

    def download(self):
        print("Downloading vocabulary file...")
        file_path = os.path.join(self.data_path, self.vocabulary_file)
        if os.path.exists(file_path):
            print("Not necessary, vocabulary file already downloaded.")
        else:
            response = requests.get(self.vocabulary_url, allow_redirects=True)
            open(file_path, 'wb').write(response.content)
            print("Download successful.")

    def parse(self):
        print("Parsing vocabulary file...")
        file_path = os.path.join(self.data_path, self.vocabulary_file)
        with open(file_path, 'r') as file:
            line = file.readline()
            while line:
                match = re.search(self.parsing_pattern, line)
                if match:
                    word = match.group(1)
                    self.words.append(word)
                line = file.readline()
        print("Parsing successful.")

    def get_words(self):
        if len(self.words) == 0:
            print("Word list is empty.")
            self.download()
            self.parse()
        return self.words

    def search(self, pattern):
        print(f"Searching for words with pattern {pattern}")
        words = self.get_words()
        result = []
        for word in words:
            if re.match(pattern, word):
                result.append(word)
        return result
