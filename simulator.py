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
    
    def add_containing_chars(self, chars):
        if chars == '_':
            return
        self.containing_characters += chars
        self.containing_characters = ''.join(set(self.containing_characters))
        assert len(self.containing_characters) <= self.length
    
    def exclude_chars(self, chars):
        if chars == '_':
            return
        self.exclude_characters += chars
        self.exclude_characters = ''.join(set(self.exclude_characters))
    
    def get_possible_guesses(self):
        return generate_words(
            fixed_chars=self.fixed_characters,
            containing_chars=self.containing_characters,
            exclude_chars=self.exclude_characters,
            length=self.length
        )
    
    def parse_response(self, response):
        """
        Parses the "response" to a guess. Each guess will give us some new information,
        this function will parse that response and update the values of the fixed_characters,
        containing_characters, and exclude_characters.
        
        response is a dictionary of the following format -
        response = {
            'fixed_characters': 'D..SY',
            'containing_characters': 'A',
            'exclude_characters': 'MNO',
        }
        'containing_characters' only contains the characters that we learned about
        IN THIS GUESS, and not in all guesses. Same for 'exclude_characters'
        """
        self.set_fixed_chars(response.get('fixed_characters', ''))
        self.add_containing_chars(response.get('containing_characters', ''))
        self.exclude_chars(response.get('exclude_characters', ''))
    
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
