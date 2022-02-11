from dictionary import ALLOWED_WORDS
from words import get_matching_words
from words import ALL_CHARS


class Simulator:
    def __init__(self, length=5):
        self.fixed_characters = '.....'
        self.containing_character_sets = [ALL_CHARS.copy() for i in range(length)]
        self.containing_characters = set()
        self.exclude_characters = set()
        self.length = length
        self.word_list = list(ALLOWED_WORDS)
    
    def parse_response(self, guess, response):
        """
        Parses the response to the guessed word. The guess is just a word, string of 5 chars.
        The response is also a string of 5 characters where each character is one of - "B", "G", "Y"
        
        "B" stands for black, and means that the letter in the guess at that index was not in the answer
        "G" stands for green, and means that the letter in the guess at that index was correctly guessed
        "Y" stands for yellow, and means that the letter in the guess at that index is in the answer,
        but not at that index
        """
        guess = guess.upper()
        response = response.upper()
        assert len(guess) == len(response)
        
        for i in range(len(response)):
            resp_code = response[i]
            guessed_char = guess[i]
            
            if resp_code == "B":
                # Update the excluded characters
                self.exclude_characters.add(guessed_char)
            if resp_code == "G":
                # Update the fixed characters
                _ = ''
                for c in range(len(self.fixed_characters)):
                    if self.fixed_characters[c] != '.':
                        _ += self.fixed_characters[c]
                    elif c == i:
                        _ += guessed_char
                    else:
                        _ += '.'
                self.fixed_characters = _
                # Update the containing characters
                self.containing_character_sets[i] = set(guessed_char)
            if resp_code == "Y":
                # The guessed_char is not at this index at least
                self.containing_character_sets[i].remove(guessed_char)
                # But it is in the answer somewhere
                self.containing_characters.add(guessed_char)
    
    def run(self):
        print('Enter "W" if you win!')
        for i in range(6):      # We have a total of 6 guesses
            response = input('\n---------\nEnter your last guess and its response - ').strip()
            if response.upper() == 'W':
                print('Great!')
                return
            _ = response.split()
            self.parse_response(_[0], _[1])
            
            print('\nGenerating your next guesses...')
            words = get_matching_words(
                self.word_list,
                self.fixed_characters,
                self.containing_character_sets,
                self.containing_characters,
                self.exclude_characters
            )
            self.word_list = words
            print(f'\nFound {len(words)} possible matches.')
            print(f'Guess one of the following words next - \n{words[:10]}')
        print('Looks like you didn\'t get it this time. Try a better opening word next time...')
