word = input("Enter a word: ")
char_counts = {}

for char in word:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
        
for char, count in char_counts.items():
    print(f"{char}: {count}")
