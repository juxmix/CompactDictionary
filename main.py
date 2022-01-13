import CompactDictionary as compDict
import logging

if __name__ == '__main__':
    cd = compDict.CompactDictionary()
    #clean_word = cd.clean_word(" \n$0_algo-[]123.;\t ")
    #logging.info("Clean word: '{}'".format(clean_word))
    books = ("Frankenstein", "Pride_and_prejudice", "The_Scarlet_Letter", "Alice_in_Wonderland", \
             "Sherlock_Holmes", "Chrismas_Carol", "A_Doll's_house", "The_Sun_Also_Rises", \
             "A_Modest_Proposal", "The_Great_Gatsby", "A_Tale_of_two_cities", \
             "The_importance_of_being_ernest", "Moby_Dick", "The_Picture_of_Dorian_Grey")
    for title in books:
        full_book_name = "Books/" + title + ".txt"
        logging.info("--------------")
        logging.info("Loading: " + full_book_name)
        cd.load_text(full_book_name)
    logging.info("---------------")
    '''    
    cd.load_text("Books/Frankenstein.txt")
    cd.load_text("Books/Pride_and_prejudice.txt")
    cd.load_text("Books/The_Scarlet_Letter.txt")
    cd.load_text("Books/Alice_in_Wonderland.txt")
    cd.load_text("Books/Sherlock_Holmes.txt")
    cd.load_text("Books/Chrismas_Carol.txt")
    cd.load_text("Books/A_Doll's_house.txt")
    cd.load_text("Books/The_Sun_Also_Rises.txt")
    cd.load_text("Books/A_Modest_Proposal.txt")
    cd.load_text("Books/The_Great_Gatsby.txt")
    cd.load_text("Books/A_Tale_of_two_cities.txt")
    '''
    words = ("ancien", "monster", "lady", "gentleman")
    for word in words:
        is_in = cd.contains(word)
        logging.info(word + " in Dictionary: " + str(is_in))


