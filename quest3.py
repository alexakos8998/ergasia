import sys
import enchant

def permutations(letters): 

    if len(letters) == 0: 
        return [] 
    if len(letters) == 1: 
        return [letters] 
    possible = [] 
    for i in range(len(letters)): 
       m = letters[i] 
       remaining = letters[:i] + letters[i+1:] 
       for p in permutations(remaining): 
           possible.append([m] + p) 
    return possible 

letters = list(sys.argv[1])
per_list = permutations(letters)
d = enchant.Dict("en_US")
for permutation in per_list:
    word = ''.join(permutation)
    if d.check(word):
        print(word)