"""Module that provides is_palindrome.

Author of is_palindrome: Dara
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Returns if word is the same read forward and in reverse

    word: string
    
    returns: string

    this looks through the list of words provided by words.txt"""

if first(word) == last(word) and middle(word) == middle(word):

   return True


