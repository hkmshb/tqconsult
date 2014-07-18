"""
Transquisite Consulting: Pre-Test Questions from eHealth Systems Africa.
Answers to programming questions.
"""


#+----------------------------------------------------------------------------+
#| Programming Question 1:
#| Implement a function with signature find_chars(string1, string2) that takes 
#| two strings and returns a string that contains only the characters found in 
#| string1 and string two in the order that they are found in string1. Implement
#| a version of order N*N and one of order N.
#+----------------------------------------------------------------------------+
def find_chars(string1, string2):
    """
    find_chars: order N*N
    
    alternative (verbose):
    found = []
    for c in string1:
        if c in string2:
            found.append(c)
    return ''.join(found)
    """
    return ''.join([c for c in string1 if c in string2])


def find_chars2(string1, string2):
    """
    find chars: order N
    
    alternative (verbose):
    found, uniq = [], set(string2)
    for c in string1:
        if c in uniq:
            found.append(c)
    return ''.join(found)
    """
    return ''.join([c for c in string1 if c in set(string2)])


#+----------------------------------------------------------------------------+
#| Programming Question 2:
#| Write a function that takes as input a sorted array and modifies the array 
#| to compact it, removing duplicates. Also return the new length of the array.
#| Notes: The input array might be very large.
#| For example:
#|    input array = [1, 3, 7, 7, 8, 9, 9, 9, 10]
#|    transformed array = [1, 3, 7, 8, 9, 10]
#|    size = 6
#+----------------------------------------------------------------------------+
def compact(array):
    prev = array[0]
    
    idx = 1
    while (idx < len(array)):
        if prev == array[idx]:
            del array[idx]
        else:
            prev = array[idx]
            idx += 1
    return len(array)


#+----------------------------------------------------------------------------+
#| Programming Question 3: String Tokenization in Python
#| Write a function, tokenize_string(input_string, delimiter_list) that returns 
#| a list of strings that are separated by the delimiters.
#| For example: 
#|    tokenize_string("How now, Mrs. Brown Cow") 
#|    returns ['How', 'now', 'Mrs', 'Brown', 'Cow']
#+----------------------------------------------------------------------------+
def tokenize_string(input_string, delimiter):
    """
    Tokenizes a string using a single delimiter character.
    """
    return input_string.split(delimiter)


def tokenize_string2(input_string, delimiter_list):
    """
    Tokenizes a string using a list of delimiter characters.
    """
    buff, tknz = [], input_string.split(delimiter_list[0])
    for c in delimiter_list[1:]:
        for t in tknz:
            # split and remove white space
            buff.extend([x for x in t.split(c) if x.strip()])
        tknz = buff
        buff = []
    return tknz

