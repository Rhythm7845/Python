list=[]
n = int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    element = input("Enter an element: ")
    list.append(element)
set = {*set(list)}
num = len(set)
print("There are",num,"elements, which are:",set,"and ",n-num,"duplicate(s)")