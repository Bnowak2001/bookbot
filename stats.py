def get_book_text(filepath):
    with open(filepath) as f:
        filecontent = f.read()
    return filecontent

def get_words(textstring:str):
    return textstring.split()

def get_character_dict(word_list:list):
    char_dict = {}
    for word in word_list:
        lowercased = word.lower()
        for char in lowercased:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def sort_char_dict(char_dict:dict):
    char_list = []
    for char in char_dict:
        sub_dict = {
            'character' : char,
            'count': char_dict[char]
        }
        char_list.append(sub_dict)
#    print(char_list)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
def sort_on(dict):
    return dict['count']


