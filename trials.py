"""Python functions for JavaScript Trials 1."""

""" To test this code, run:
python3 -m doctest trials.py
"""


def output_all_items(items):
    """
    >>> output_all_items([1, 'hello', True])
    1
    hello
    True
    """
    for item in items:
        print(item)


def get_all_evens(nums):
    """
    >>> get_all_evens([7, 8, 10, 1, 2, 2])
    [8, 10, 2, 2]
    """
    answer = []
    for num in nums:
        if num % 2 == 0:
            answer.append(num)
    return answer


def get_odd_indices(items):
    """
    >>> get_odd_indices([1, 'hello', True, 500])
    ['hello', 500]
    """
    answer = []
    for index, item in enumerate(items):
        # print(item, index)
        if index % 2 != 0:
            answer.append(item)
    return answer


def print_as_numbered_list(items):
    """
    https://www.afternerd.com/blog/python-enumerate/
    >>> print_as_numbered_list([1, 'hello', True])
    1. 1
    2. hello
    3. True
    """
    for index, item in enumerate(items, start = 1):
        print(f"{index}. {item}")


def get_range(start, stop):
    """
    >>> get_range(0, 5)
    [0, 1, 2, 3, 4]
    >>> get_range(1, 3)
    [1, 2]
    """
    answer = []
    for num in range(start, stop):
        answer.append(num)
    
    return answer


def censor_vowels(word):
    """
    >>> censor_vowels('hello world')
    'h*ll* w*rld'
    """
    answer = []
    for letter in word:
        if letter in 'aeiou':
            answer.append("*")
        else:
            answer.append(letter)

    return "".join(answer)


def snake_to_camel(string):
    """
    >>> snake_to_camel('hello_world')
    'HelloWorld'
    """
    answer = []
    for word in string.split("_"):
        # Could have done word[0].upper()
        answer.append(word.title())

    return "".join(answer)



def longest_word_length(words):
    """
    >>> longest_word_length(['hello', 'world'])
    5
    >>> longest_word_length(['jellyfish', 'zebra'])
    9
    >>> longest_word_length(['zebra', 'jellyfish'])
    9
    """
    max_word_length = 0

    for word in words:
        if len(word) > max_word_length:
            max_word_length = len(word)

    return max_word_length  # Or put lengths in a list max(word_lengths)
    


def truncate(string):
    """
    >>> truncate('aaaabbbbcccca')
    'abca'
    >>> truncate('hi***!!!! wooow')
    'hi*! wow'
    """
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return "".join(result)



def has_balanced_parens(string):
    """
    >>> has_balanced_parens('()')
    True
    >>> has_balanced_parens('((This) (is) (good))')
    True
    >>> has_balanced_parens('(Oh no!)(')
    False
    """
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        else:
            pass

    return parens == 0
    

def compress(string):
    """
    >>> compress('aabbaabb')
    'a2b2a2b2'
    >>> compress('abc')
    'abc'
    >>> compress('Hello, world! Cows go moooo...')
    'Hel2o, world! Cows go mo4.3'
    """
    compressed = []

    curr_char = ""
    char_count = 0
    for char in string:
        if char != curr_char:  # Next character is different.
            compressed.append(curr_char)  # Chain it to the answer.

            # Take care of any business regarding the PREVIOUS repeater:
            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char  # update this.
            char_count = 0  # reset this.

        # Repeating char:
        # Add one to the count. We don't know how many repeats there will be.
        char_count += 1

    # If you have a new letter, chain it to the answer:
    compressed.append(curr_char)

    # If you have a count, instead of a letter, chain it to the answer now:
    if char_count > 1:
         compressed.append(str(char_count))

    # Present the answer:
    return "".join(compressed)
