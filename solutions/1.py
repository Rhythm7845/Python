def vowelsandconsonants(x):
    x = str(x)
    li = []
    li[:0] = x
    vowels = {"a", "e", "i", "o", "u"}
    count_vowels = 0
    count_consonants = 0
    
    for i in li:
        if i in vowels:
            count_vowels += 1
        else:
            count_consonants += 1
    
    return(count_vowels, count_consonants)

a = input("Enter a word: ")
print(vowelsandconsonants(a))