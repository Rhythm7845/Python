def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
a = int(input("Enter a number: "))
b = input("Do you want to use a simple or recursive function? (s/r): ")

if b == "s":
    print(factorial(a))

elif b == "r":
    print(factorial_recursive(a))
    
else:
    print("Invalid input")