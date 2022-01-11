import CompactDictionary as compDict
import logging

if __name__ == '__main__':
    cd = compDict.CompactDictionary()
    clean_word = cd.clean_word(" \n$0_algo-[]123.;\t ")
    logging.info("Clean word: '{}'".format(clean_word))
    cd.load_text("Frankenstein.txt")
    words = ("ancien", "monster", "lady", "gentleman")
    for word in words:
        is_in = cd.contains(word)
        logging.info(word + " in Frankenstein.txt: " + str(is_in))


