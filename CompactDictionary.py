import logging
import re

F_INSERTED_WORDS = "Inserted.txt"
F_REJECTED_WRODS = "Rejected.txt"
F_FAILED_WORDS = "Failed.txt"

class CompactDictionary:

    def __init__(self, language="English"):
        self.END_WORD = '#'
        self.language = language
        self.fullDict = dict()
        logging.basicConfig(level=logging.INFO)

    def clean_word(self, word):
        return word.strip("\t\n .,;:&#*/()[]{}¡!¿?$€—-_“”\‘\"\'0123456789").lower()

    def add_word(self, word):
        clean_word1 = self.clean_word(word)
        if (clean_word1 is None) or (len(clean_word1) < 1):
            return False
        if self.contains(clean_word1):
            return False
        first_letter = clean_word1[0]
        if first_letter not in self.fullDict:
            self.fullDict[first_letter] = dict()
        sub_dict = self.fullDict.get(first_letter)
        for letter in clean_word1[1:]:
            if sub_dict is None or letter not in sub_dict:
                sub_dict[letter] = dict()
            sub_dict = sub_dict[letter]
        return True

    def contains(self, word):
        clean_word = word.lower()
        #clean_word = self.clean_word(word)
        #if (not clean_word is None) and (len(clean_word) > 0):
        #    return False
        resto = self.fullDict.get(clean_word[0])
        keys = self.fullDict.keys()
        if not clean_word[0] in keys:
            return False
        for letter in clean_word[1:]:
            keys = resto.keys()
            if letter in keys:
                resto = resto.get(letter)
            else:
                return False
        return True

    def load_text(self, file_name):
        f = open(file_name)
        fi = open(F_INSERTED_WORDS, "w")
        fr = open(F_REJECTED_WRODS, "w")
        ff = open(F_FAILED_WORDS, "w")
        num_words = 0
        skipped_words = 0
        failed_words = 0
        for line in f:
            #lst_pals = line.split()
            lst_pals = re.split(':|;|_|,|\.|/|\’|\t| |\'|\-|\—|\n', line)
            for palabra in lst_pals:
                #Notepad UTF-8 unicode indicator breaks everything
                if '\ufeff' in palabra:
                    fr.write(palabra + " (Marca de Notepad de UTF-8)")
                    continue
                added = False
                if len(palabra) > 0 and not self.contains(palabra):
                    added = self.add_word(palabra)
                    if added:
                        num_words += 1
                        fi.write(str(num_words) + " " +\
                                 palabra + " " + self.clean_word(palabra) + "\n")
                    else:
                        failed_words += 1
                        ff.write(str(failed_words) + " " +\
                                 palabra + " " + self.clean_word(palabra) + "\n")
                else:
                    skipped_words += 1
                    fr.write(str(skipped_words) + " " +\
                             palabra + " " + self.clean_word(palabra) + "\n")

                logging.debug(palabra + " " + str(added))
        logging.info("Added: " + str(num_words) + " / skipped: " + str(skipped_words)\
                     + " / failed: " + str(failed_words))
        f.close()
        ff.close()
        fr.close()
        fi.close()
        



