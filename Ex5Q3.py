numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

separate = lambda nums: {'even': [n for n in nums if n % 2 == 0],
                         'odd': [n for n in nums if n % 2 != 0]}

print(separate(numbers))