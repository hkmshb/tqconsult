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


#+----------------------------------------------------------------------------+
#| Programming Question 4: Rotating an Array in Python
#| Write a function that takes an array of integers and returns that array 
#| rotated by N positions. For example, if N=2, given the input array 
#| [1, 2, 3, 4, 5, 6] the function should return [5, 6, 1, 2, 3, 4]
#+----------------------------------------------------------------------------+
def rotate(array, npos):
    """
    Rotates the provided array by the number of position specified in npos.
    """
    if len(array):
        # ensure npos is positive & not greater than array length
        npos = abs(npos) % len(array)
        if npos:
            chunk = array[-npos:]
            del array[-npos:]
            
            chunk.reverse()
            for x in chunk:
                array.insert(0, x)
    return array


#+----------------------------------------------------------------------------+
#| Programming Question 5: Least Common Multiple in Python 
#| The least common multiple of a set of integers is the smallest positive 
#| integer that is a multiple of all of the integers in the set.Write a 
#| function that takes an array of integers and efficiently calculates and 
#| returns the LCM.
#+----------------------------------------------------------------------------+
def lcm(array):
    """
    Returns the lease common multiple of the set of integers in array.
    """
    i, repo = 0, {}
    while i < 10000:    # prevents endless loop?
        i += 1
        for n in array:
            multiple = n * i
            if not repo.has_key(multiple):
                repo[multiple] = 1
            else:
                repo[multiple] += 1
                if repo[multiple] == len(array):
                    return multiple                
    
    

