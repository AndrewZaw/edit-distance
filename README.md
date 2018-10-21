# edit-distance
Concise algorithm written in Python used to calculate the Levenshtein distance between two strings.

Supports different edit costs if character is uppercase/lowercase, and recognizes difference between vowels/consonants.

Default values:

Insertion: 1 for lowercase, 2 for uppercase
Substitutions: 1 if both vowels or both consonants, 2 otherwise. 

## Usage

'''
editDistance("StringA","stringB")
'''

## Examples

'''
editDistance("glasses","grass")
'''

returns 4. 

## Built with

Python
