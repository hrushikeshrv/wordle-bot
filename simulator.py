from words import generate_words


class Simulator:
    def __init__(self, length=5):
        self.fixed_characters = '.....'
        self.containing_characters = [set() for i in range(length)]
        self.exclude_characters = set()
        self.length = length
    
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
            if resp_code == "Y":
                # Update the containing_character
                for j in range(len(guess)):
                    if j == i:
                        self.containing_characters[j].remove(guessed_char)
                    else:
                        self.containing_characters[j].add(guessed_char)
    
    def run(self):
        for i in range(6):      # We have a total of 6 guesses
            response = input('\n---------\nEnter the response to your last guess - ').strip()
            if response == 'W':
                print('Great!')
                return
            # The response will have format "fixed_chars<SPACE>containing_chars<SPACE>exclude_chars"
            _ = response.split()
            response_dict = {
                'fixed_characters': _[0],
                'containing_characters': _[1],
                'exclude_characters': _[2],
            }
            self.parse_response(response_dict)
            print('\nGenerating your next guesses...')
            words = self.get_possible_guesses()
            print(f'Guess one of the following words next - \n{words[:10]}')
