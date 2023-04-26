def divisible_numbers(numbers, divisor):
    result = []
    for num in numbers:
        if num % divisor == 0:
            result.append(num)
    return result

li=[]
c = int(input("Enter the divisor: "))
a = int(input("Enter the number of elements: "))

i = 0
while(i < a):
    b = int(input("Enter a number: "))
    li.append(b)
    i +=1

print(divisible_numbers(li, c))