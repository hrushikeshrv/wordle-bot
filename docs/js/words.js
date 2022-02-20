const ALL_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ');

function getMatchingWords(
    wordList,
    fixedCharacters='.....',
    containingCharacterSets=null,
    containingCharacters=null,
    excludeCharacters=null,
    length=5
) {
    /*
    Iterate through all possible guessable words and return only the words which match the input
    parameters.

    fixed_characters is a string of length 5
    containing_character_sets is a list of sets
    exclude_characters is a string containing all the characters not in the word
     */
    if (!excludeCharacters) {
        excludeCharacters = new Set();
    }
    if (!containingCharacters) {
        containingCharacters = ALL_CHARS;
    }
    if (!containingCharacterSets) {
        containingCharacterSets = []
        for (let i = 0; i < length; i++) {
            containingCharacters.push(ALL_CHARS);
        }
    }

    const matches = [];
    for (let word of wordList) {
        word = word.toUpperCase();
        let valid = true;
        for (let i = 0; i < word.length; i++) {
            if (fixedCharacters[i] !== '.' && word[i] !== fixedCharacters[i]) {
                valid = false;
                break;
            }
            if (!containingCharacterSets[i].has(word[i])) {
                valid = false;
                break;
            }
            if (excludeCharacters.has(word[i])) {
                valid = false;
                break;
            }
        }
        if (containingCharacters && (containingCharacters - new Set(word)).length > 0) {
            valid = false;
        }
        if (valid) {
            matches.push(word);
        }
    }
    return rank(matches, wordList);
}

function rank(wordList, allowedGuesses) {
    if (wordList.length === 1) {
        return [[wordList[0], 1]]
    }
    const values = [];
    for (let word of wordList) {
        values.push([word, calculateValue(word, allowedGuesses)]);
    }
    return values.sort((a, b) => {return a[1] - b[1]});
}

function calculateValue(word, allowedGuesses) {
    const responseFrequencies = {};
    for (let guess of allowedGuesses) {
        guess = guess.toUpperCase();
        const _ = guessResponse(word, guess);
        responseFrequencies[guess] = responseFrequencies[guess] ? responseFrequencies[guess] + 1 : 1;
    }
    const totalWords = allowedGuesses.length;
    let value = 0;
    for (let pattern in responseFrequencies) {
        value += (responseFrequencies[pattern] / totalWords) * -Math.log2(responseFrequencies[pattern] / totalWords);
    }
    return value;
}

function guessResponse(guess, answer) {
    let response = '';
    for (let i = 0; i < guess.length; i++) {
        const char = guess[i];
        if (!answer.match(`\w*${char}\w*`)) {
            response += 'b';
        }
        else if (char === answer[i]) {
            response += 'g';
        }
        else {
            response += 'y';
        }
    }
    return response;
}