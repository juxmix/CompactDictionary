import logging

class CompactDictionary:

    def __init__(self, language="English"):
        self.END_WORD = '#'
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
        num_words = 0
        skipped_words = 0
        failed_words = 0
        for line in f:
            lst_pals = line.split()
            for palabra in lst_pals:
                #Notepad UTF-8 unicode indicator breaks everything
                if '\ufeff' in palabra:
                    continue
                if not self.contains(palabra):
                    added = self.add_word(palabra)
                    num_words = num_words + 1 if added else num_words
                    failed_words = failed_words + 1 if not added else failed_words
                else:
                    skipped_words += 1
                logging.debug(palabra + " " + str(added))
        logging.info("Added: " + str(num_words) + " / skipped: " + str(skipped_words)\
                     + " / failed: " + str(failed_words))
        f.close()
        



