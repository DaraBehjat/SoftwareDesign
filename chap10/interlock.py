"""

interlock Dara Behjat

"""

def interlock(word_list, word):
    """Checks whether a word can be split into two interlocked words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print word, word[::2], word[1::2]


