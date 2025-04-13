from stats import get_book_text
from stats import get_words
from stats import get_character_dict
from stats import sort_char_dict
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        frankenstein_text = get_book_text(filepath)
        frankenstein_words_list = get_words(frankenstein_text)
        wordcount = len(frankenstein_words_list)
        char_dict = get_character_dict(frankenstein_words_list)
        char_list = sort_char_dict(char_dict)
        print_report(filepath,wordcount,char_list)
        sys.exit(0)

def print_report(filepath:str,word_count:int,char_list:list):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_list:
        if char['character'].isalpha():
            print(f"{char['character']}: {char['count']}")
    print("============= END ===============")


main()