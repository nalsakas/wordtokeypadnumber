# wordtokeypadnumber
For a given list of words, determine their corresponding phone numbers.
An alternative problem would be inverse of this problem. Instead of determining corresponding number for a given word,
We could determine all possible words for a given phone number. But that would be another nice problem. 

# Problem Statement
For a given phone number and a list of words, determine which words can be contructed from the keypad for given phone number.

# Solution
Loop through all words.
Loop through all chars of the word.
Determine corresponding number of the character in keypad.
Collect all determined numbers
After each word iteration, check weather collected numbers are equal to the given phone number or not.