import logging

class CompactDictionary:

    def __init__(self, language="English"):
        self.END_WORD = '-'
        self.language = language
        self.fullDict = dict()
        logging.basicConfig(level=logging.INFO)

    def clean_word(self, word):
        return word.strip("\t\n .,;:&/()[]{}¡!¿?$€-_\"\'0123456789")

    def add_word(self, word):
        clean_word1 = self.clean_word(word).lower()
        if (clean_word1 is None) or (len(clean_word1) < 1):
            return False
        first_letter = clean_word1[0]
        if first_letter not in self.fullDict:
            self.fullDict[first_letter] = dict()
        sub_dict = self.fullDict.get(first_letter)
        for letter in clean_word1[1:]:
            if sub_dict is None or letter not in sub_dict:
                sub_dict[letter] = {}
            sub_dict = sub_dict[letter]
        return True

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
        f = open(file_name)
        for line in f:
            lst_pals = line.split()
            for palabra in lst_pals:
                if '\ufeff' in palabra:
                    continue
                added = self.add_word(palabra)
                logging.debug(palabra + " " + str(added))
        f.close()




if __name__ == '__main__':
    cd = CompactDictionary()
    clean_word = cd.clean_word(" \n$0_algo-[]123.;\t ")
    logging.info("Clean word: '{}'".format(clean_word))
    cd.load_text("Frankenstein.txt")
    words = ("ancien", "monster", "lady", "gentleman")
    for word in words:
        is_in = cd.contains(word)
        logging.info(word + " in Frankenstein.txt: " + str(is_in))
        



