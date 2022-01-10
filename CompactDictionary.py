class CompactDictionary:

    def __init__(self, language="English"):
        self.language = language
        self.fullDict = dict()

    def addword(self, word):
        clean_word = self.cleanword(word)
        for letter in clean_word:
            sub_dict = self.fullDict[letter]
            if sub_dict is None:
                sub_dict = {letter: None}

    def cleanword(self, word):
        clean_word = word.strip("\t\n .,;:&/()[]{}¡!¿?$€\"\'0123456789")
        return clean_word

if __name__ == '__main__':
    cd = CompactDictionary()
    clean_word = cd.cleanword(" \n$0algo[]123.;\t ")
    print("Clean word: '{}'".format(clean_word))
        



