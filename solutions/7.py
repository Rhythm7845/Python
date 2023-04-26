def longest_word(words):
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    return max_len

a = input("Enter a sentence: ")
li = a.split(" ")
print(longest_word(li))