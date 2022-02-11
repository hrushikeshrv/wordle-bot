# Consider all the words that are actually allowed answers while playing the game,
# consider all the words that could be used for analysis
from dictionary import ALLOWED_WORDS, ALLOWED_GUESSES

ALL_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


# Deprecated. Instead of generating words, just parse the set of all words and return matches
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


def get_matching_words(
        word_list,
        fixed_characters='.....',
        containing_character_sets=None,
        containing_characters=None,
        exclude_characters=None,
        length=5
):
    """
    Iterate through all possible guessable words and return only the words which match the input
    parameters.
    
    fixed_characters is a string of length 5
    containing_character_sets is a list of sets
    exclude_characters is a string containing all the characters not in the word
    """
    if exclude_characters is None:
        exclude_characters = set()
    if containing_characters is None:
        containing_characters = ALL_CHARS
    if containing_character_sets is None:
        containing_character_sets = [ALL_CHARS for i in range(length)]
    matches = []
    for word in word_list:
        word = word.upper()
        valid = True
        for i in range(len(word)):
            if fixed_characters[i] != '.' and word[i] != fixed_characters[i]:
                valid = False
                break
            if word[i] not in containing_character_sets[i]:
                valid = False
                break
            if word[i] in exclude_characters:
                valid = False
                break
        if containing_characters and len(containing_characters - set(word)) > 0:
            valid = False
        if valid:
            matches.append(word)
    return matches


def rank(word_list, allowed_guesses):
    """
    Ranks words in the word_list according to the expected amount of
    information the word would give as a guess.
    """
    if len(word_list) == 1:
        return word_list
    
    values = []
    for word in word_list:
        values.append(calculate_value(word, allowed_guesses))
    
    word_ranks = zip(word_list, values)
    return sorted(word_ranks, key=lambda x: x[1], reverse=True)


def calculate_value(word, allowed_guesses):
    return
