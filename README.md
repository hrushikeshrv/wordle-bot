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
For each guess, enter the word you guessed and the response you got from the game in the following 
format - <word> <response>

The <word> is just the word you guessed, the response is a string where each character is one of 
`"g"`, `"y"`, or `"b"`. `"g"` means that the character at that position was green, `"y"` means that the 
character at that position was yellow, and `"b"` means that the character at that position was black.

A sample input could be as follows - `"straw gbygb"`.  
This means that `s` is in the answer, and it is in the correct position, `t` is not in the answer,
`r` is in the answer, but it is not in the 3rd position, and so on.
