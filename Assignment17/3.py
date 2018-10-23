class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def get_first_word(self):
        all_words = self.sentence.split()
        return all_words[0]
    
    def get_all_words(self):
        return self.sentence.split()

    def replace(self, index, new_word):
        try:
            replace_words = self.sentence.split()
            replace_words[index] = new_word
            self.sentence = ' '.join(replace_words)
        except IndexError:
            return None