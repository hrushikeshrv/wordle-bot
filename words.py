from math import log2
# Consider all the words that are actually allowed answers while playing the game,
# consider all the words that could be used for analysis
from dictionary import ALLOWED_WORDS, ALLOWED_GUESSES

ALL_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


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
    response_frequencies = {}
    for guess in allowed_guesses:
        _ = guess_response(guess=word, answer=guess)
        response_frequencies[_] = response_frequencies.get(_, 0) + 1
    total_words = len(allowed_guesses)
    value = 0
    for pattern in response_frequencies:
        # This gives the amount of information contained in the word in bits
        value += (response_frequencies[pattern] / total_words) * -log2(response_frequencies[pattern] / total_words)
    return value


def guess_response(guess, answer):
    return ''
