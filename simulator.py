from dictionary import ALLOWED_WORDS
from words import generate_words


class Simulator:
    def __init__(self, length=5):
        self.fixed_characters = '.....'
        self.containing_characters = ''
        self.exclude_characters = ''
        self.length = length
    
    # TODO - Make sure the character sets in fixed_characters, containing_characters,
    #   and exclude_characters are disjoint sets
    def set_fixed_chars(self, fixed_chars):
        self.fixed_characters = fixed_chars
        assert len(self.fixed_characters) <= self.length
    
    def add_containing_char(self, char):
        self.containing_characters += char
        assert len(self.containing_characters) <= self.length
    
    def exclude_char(self, char):
        self.exclude_characters += char
    
    def get_possible_words(self):
        return generate_words(
            fixed_chars=self.fixed_characters,
            containing_chars=self.containing_characters,
            exclude_chars=self.exclude_characters,
            length=self.length
        )
