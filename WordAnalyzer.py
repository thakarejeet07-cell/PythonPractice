import re

class WordAnalyzer:
    def __init__(self, text):
        self.text = text

    def get_words(self):
        return re.findall(r"[a-zA-Z]+", self.text.lower())

    def unique_words(self):
        words = self.get_words()
        return {word for word in words}

    def word_lengths(self):
        words = self.get_words()
        return {word: len(word) for word in words}

    def long_words(self, min_len=5):
        words = self.get_words()
        return [word for word in words if len(word) >= min_len]


text = "Python is fun! Python is powerful, and Python is easy to learn."

analyzer = WordAnalyzer(text)

print("All words:", analyzer.get_words())
print("Unique words:", analyzer.unique_words())
print("Word lengths:", analyzer.word_lengths())
print("Long words (5+ letters):", analyzer.long_words())