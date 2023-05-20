a = input("Enter a sentence: ")
dict={}

for letter in a:
    if letter not in dict.keys():
        dict[letter] = 1
    elif letter in dict.keys():
        dict[letter] = dict[letter] + 1
for x, y in dict.items():
  print(x, y)