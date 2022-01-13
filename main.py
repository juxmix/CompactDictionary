import CompactDictionary as compDict
import logging

if __name__ == '__main__':
    cd = compDict.CompactDictionary()
    #clean_word = cd.clean_word(" \n$0_algo-[]123.;\t ")
    #logging.info("Clean word: '{}'".format(clean_word))
    books = ("A_Doll's_house", "A_Modest_Proposal", "A_Tale_of_two_cities", \
             "Alice_in_Wonderland", "Chrismas_Carol", "Corea_the_Ermit_Nation", \
             "Frankenstein", "Moby_Dick", "Pride_and_prejudice", "Sherlock_Holmes", \
             "The_Great_Gatsby", "The_importance_of_being_ernest", "The_Picture_of_Dorian_Grey", \
             "The_Scarlet_Letter", "The_Sun_Also_Rises")
    for title in books:
        full_book_name = "Books/" + title + ".txt"
        logging.info("--------------")
        logging.info("Loading: " + full_book_name)
        cd.load_text(full_book_name)
    logging.info("---------------")

    words = ("ancien", "monster", "lady", "gentleman", "hola", "angus")
    for word in words:
        is_in = cd.contains(word)
        logging.info(word + " -> " + str(is_in))


