num = input("Enter an armstrong number: ")
sum = 0
n = len(num)
i = 0
while (i < n):
    a = int(num[i])**n
    sum = sum + a
    i+=1
if sum == int(num):
    print("The number is an armstrong number.")
else:
    print("the number is not an armstrong number.")
quit()