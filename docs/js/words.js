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
        excludeCharacters = set();
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
        if (containingCharacters && (containingCharacters - set(word)).length > 0) {
            valid = false;
        }
        if (valid) {
            matches.push(word);
        }
    }
    return rank(matches, wordList);
}

function rank(wordList, allowedGuesses) {

}