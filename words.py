# Consider all the words that are actually allowed answers while playing the game,
# consider all the words that could be used for analysis
from dictionary import ALLOWED_WORDS

ALL_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def generate_words(fixed_chars='.....', containing_chars='', exclude_chars='', length=5):
    """
    Generate all possible words of the given length with all the characters in fixed_chars in their given
    positions and including all the characters in containing_chars and not including any of the characters
    in exclude_chars.
    
    fixed_chars is a string of 5 characters where each letter in each position is a fixed character.
    A '.' at a position in fixed_chars means we don't know which character occurs at that position yet.
    
    containing_chars is a string of at most 5 characters.
    
    exclude_chars is a string of at most 5 characters.
    :param fixed_chars: str
    :param containing_chars: str
    :param exclude_chars: str
    :param length: int (default 5)
    :return : List[str]
    """
    assert len(containing_chars) <= length
    assert len(fixed_chars) == length
    containing_chars = set(containing_chars)
    exclude_chars = set(exclude_chars)
    
    possible_chars = {x: '' for x in range(length)}
    
    for i in range(length):
        if fixed_chars[i] != '.':
            possible_chars[i] = fixed_chars[i]
        else:
            possible_chars[i] = ''.join(ALL_CHARS - exclude_chars)
    
    temp_possible_words = list(possible_chars[0])
    for i in range(1, length):
        temp_possible_words = permute_chars_on(temp_possible_words, possible_chars[i])
    
    # Creating another list here, memory may be used more efficiently by doing
    # character filtering in-place, but that would take more time
    possible_words = []
    for word in temp_possible_words:
        if all(char in word for char in containing_chars) and word.lower() in ALLOWED_WORDS:
            possible_words.append(word)
    
    return possible_words


def permute_chars_on(words, chars):
    """"""
    possible_words = []
    for word in words:
        for char in chars:
            possible_words.append(word + char)
    return possible_words
