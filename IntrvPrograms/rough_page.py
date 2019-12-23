# function that filters vowels 

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 

def vowels(x):
    if x in "aeiou":
        return True
    else:
        return False


v = list(filter(vowels, sequence))
print(v)