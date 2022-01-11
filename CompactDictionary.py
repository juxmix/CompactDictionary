class CompactDictionary:

    def __init__(self, language="English"):
        self.language = language
        self.fullDict = dict()

    def clean_word(self, word):
        return word.strip("\t\n .,;:&/()[]{}¡!¿?$€-_\"\'0123456789")

    def add_word(self, word):
        clean_word1 = self.clean_word(word)
        for letter in clean_word1:
            sub_dict = self.fullDict[letter]
            if sub_dict is None:
                sub_dict = {letter: None}

    def contains(self, word):
        resto = self.fullDict.get(word[0])
        keys = self.fullDict.keys()
        if not word[0] in keys:
            return False
        for letter in word[1:]:
            keys = resto.keys()
            if letter in keys:
                resto = resto.get(letter)
            else:
                return False
        return True

    def load_text(self, file_name):
        f = open(file_name, 'rU')
        for line in f:
            lst_pals = line.split()
            for palabra in lst_pals:
                self.add_word(palabra)
        f.close()




if __name__ == '__main__':
    cd = CompactDictionary()
    clean_word = cd.cleanword(" \n$0_algo-[]123.;\t ")
    print("Clean word: '{}'".format(clean_word))
        



