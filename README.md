# wordle-bot
A bot (python script) that will give you the best words to guess in Wordle

# Requirements
None except python installed (for now, web based bot coming soon)

# Usage
Clone this repository and then -
1. Open a game of wordle either on the [official website](https://www.powerlanguage.co.uk/wordle/) or another simulator like (https://engaging-data.com/wordguessr-wordle/)
2. Navigate into this repo's directory
3. run `python main.py`
4. Make any first guess in your game
5. Enter the result of your guess in your terminal (see the input format in the next heading)
6. The bot will give you the next few words to guess
7. Repeat till you win

# Input format
If you guess a word, say "YEAST", and the game tells you that the letters "S" and "T" in the correct spot, and none of the other letters are in the answer, then you should 
input the following string into the terminal - `...ST _ YEA`

The input consists of three parts separated by a space. 
1. The first part contains the characters that are in the correct spot in the answer - in this case "S" and "T". Since we don't know
the first 3 characters, we write them as "." If we didn't know any characters in the correct spot, we would just write `.....`
2. The second part contains characters that are in the answer but were not in the correct position in your guess. In this case
we didn't have any characters like that, so we write a `_` instead.
3. The second part contains characters that we know are not in the answer - in this case "Y", "E", and "A". If we didn't get any
characters like this, we would have written a `_` instead.

You don't have to write all the characters for the second and third part for each guess, you can just add the new characters that you
discovered and the bot will remember all the characters you had entered before.
