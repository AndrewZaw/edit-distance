# edit-distance
Concise algorithm written in Python used to calculate the Levenshtein distance between two strings.

Supports different edit costs if character is uppercase/lowercase, and recognizes difference between vowels/consonants.

Default values:

Insertion: 1 for lowercase, 2 for uppercase
Substitutions: 1 if both vowels or both consonants, 2 otherwise. 

## Usage

```
editDistance("StringA","stringB")
```

to calculate edit distance between StringA and StringB. 

## Examples

```
editDistance("glasses","Grass")
```

returns 4. The shortest possible edit distance between the two strings is to modify "Grass" in the following manner:

1. Replacing G with g (cost of 1)
2. Replacing l with r (cost of 1)
3. Adding e. (cost of 1)
4. Adding s. (cost of 1)

## Built with

Python
