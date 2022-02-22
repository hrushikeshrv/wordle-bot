class Simulator {
    constructor() {
        this.fixedCharacters = '.....';
        this.containingCharacterSets = [];
        this.containingCharacters = new Set();
        this.excludeCharacters = new Set();
        this.wordList = ALL_WORDS;
    }

    parseResponse(guess, response) {
        guess = guess.toUpperCase();
        response = response.toUpperCase();

        for (let i = 0; i < response.length; i++) {
            const respCode = response[i];
            const guessedChar = guess[i];
            if (respCode === 'B') {
                this.excludeCharacters.add(guessedChar);
            }
            if (respCode === 'G') {
                let _ = '';
                for (let c = 0; c < this.fixedCharacters.length; c++) {
                    if (this.fixedCharacters[c] !== '.') {
                        _ += this.fixedCharacters[c];
                    }
                    else if (c === i) {
                        _ += guessedChar;
                    }
                    else {
                        _ += '.';
                    }
                }
                this.fixedCharacters = _;
                this.containingCharacterSets[i] = new Set(guessedChar);
            }
            if (respCode === 'Y') {
                this.containingCharacterSets[i].remove(guessedChar);
                this.containingCharacters.add(guessedChar);
            }
        }
    }
}