"""
Usage:
editDistance('String1','String2')

Recursive algorithm for calculating Edit Distance between two strings. Supports different edit costs for lowercase, uppercase. Supports different edit costs if substitution goes from consonant to vowel or vice versa.
Default values:
Insertion: 1 for lowercase, 2 for uppercase
Substitutions: 1 if both vowels or both consonants, 2 otherwise. 
"""

def editDistanceWrap(A,B,Array):
    a = len(B) 
    b = len(A)
    lowercaseCost = 1
    uppercaseCost = 2
    differentLetterCost = 2
    sameLetterCost = 1
    if Array[a][b] == None:
            # If one of the strings is empty, the cost is equivalent to inserting all characters from the other string. 
        if len(A) == 0:
            # Sums all lowercase and uppercase chars, adding 1 to the cost for lower and 2 to the cost for upper
            cost = sum(lowercaseCost for c in B if c.islower()) + sum(uppercaseCost for c in B if c.isupper())
            Array[a][b] = cost
        elif len(B) == 0:
            cost = sum(lowercaseCost for c in A if c.islower()) + sum(uppercaseCost for c in A if c.isupper())
            Array[a][b] = cost
            # If the last char in the strings are equivalent, return editDistance of same strings minus the last char.
        elif A[-1] == B[-1]:
            Array[a][b] = editDistanceWrap(A[:-1],B[:-1],Array)
        else:
            vowels = 'aeiou'
            # Check if character added to B will be lowercase or uppercase
            if (A[-1].islower()):
                insertCostB = lowercaseCost
            else:
                insertCostB = uppercaseCost
            # Check if character added to A will be lowercase or uppercase
            if (B[-1].islower()):
                insertCostA = lowercaseCost
            else:
                insertCostA = uppercaseCost
            # Check replace cost
            if (((A[-1] in vowels) and (B[-1] in vowels)) or ((A[-1] not in vowels) and (B[-1] not in vowels))):
                replaceCost = sameLetterCost
            else:
                replaceCost = differentLetterCost        
            insertB = insertCostB + editDistanceWrap(A[:-1],B,Array) # Cost of inserting onto B, this also corresponds to deleting char from A
            insertA = insertCostA + editDistanceWrap(A,B[:-1],Array) # Cost of inserting onto A, this also corresponds to deleting char from B
            replace = replaceCost + editDistanceWrap(A[:-1],B[:-1],Array) # Cost of replacing char
            Array[a][b] = min(insertB,insertA,replace)
    return Array[a][b]

def editDistance(A,B):
    Array = [[None for i in range(len(A)+1)] for j in range(len(B)+1)]
    return editDistanceWrap(A,B,Array)

print(editDistance("glasses","grass"))


