import os
import requests
import re


class Vocabulary():
    DATA_FOLDER = "data"
    MOST_FREQUENT_SPANISH_WORDS_FILE = "10000_formas.TXT"
    MOST_FREQUENT_SPANISH_WORDS_URL = f"http://corpus.rae.es/frec/{MOST_FREQUENT_SPANISH_WORDS_FILE}"

    def __init__(self):
        self.data_path = self.DATA_FOLDER
        self.vocabulary_file = self.MOST_FREQUENT_SPANISH_WORDS_FILE
        self.vocabulary_url = self.MOST_FREQUENT_SPANISH_WORDS_URL
        self.words = []

    def download(self):
        file_path = os.path.join(self.data_path, self.vocabulary_file)
        if os.path.exists(file_path):
            print("Vocabulary file already downloaded.")
        else:
            print("Downloading vocabulary file...")
            response = requests.get(self.vocabulary_url, allow_redirects=True)
            open(file_path, 'wb').write(response.content)
            print("Download successful.")

    def parse(self):
        print("Parsing vocabulary file...")
        file_path = os.path.join(self.data_path, self.vocabulary_file)
        with open(file_path, 'r') as file:
            line = file.readline()
            while line:
                match = re.search('^\s+([0-9]+)\.\s+([a-zA-Záóúíéñ]+).*$', line)
                if match:
                    word = match.group(2)
                    self.words.append(word)
                line = file.readline()
        print("Parsing successful.")

    def get_words(self):
        if len(self.words) == 0:
            print("Word list is empty.")
            self.download()
            self.parse()
        return self.words
