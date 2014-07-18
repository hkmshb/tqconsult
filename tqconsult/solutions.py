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

