"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    This class accepts the location of a text file. It reads through that word file, copying each word into a list. It then records the number of words in that list.
    """
    def __init__(self, txt_file="words.txt"):
        "set initial variables"
        self.txt_file = txt_file
        self.word_list = WordFinder.get_word_list(self)
        self.num_words = len(self.word_list)
    
    def __repr__(self):
        "describe the file, technically"
        return f"{self.num_words} words read"

    def get_word_list(self):
        "iterate through the text file, strip it of any html, and append it to the new list of words. Then, return that list of words."
        file = open(self.txt_file)
        lst_of_words = []
        for line in file:
            line = line.strip('\n')
            lst_of_words.append(line)
        file.close()
        return lst_of_words

    def random(self):
        "pull a random word from that list and return it."
        return random.choice(self.word_list)

class SpecialWordFinder(WordFinder):
    """
    This subclass allows you to check if the text file you are using has faulty lines. e.g. a line may start with a # (indicating a section) or it may be an empty line (used for styling). This class implements code to bypass that and not include it in your return.
    """
    def random(self):
        rand_element = ""
        while rand_element == "" or rand_element.startswith('#'):
            rand_element = random.choice(self.word_list)
        return rand_element


