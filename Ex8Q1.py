flag = 0 
while(flag == 0):
    age = int(input("Enter your age: "))
    try:
        if type(age) is int:
            raise Exception("Enter an integer")
        elif type(age) is int:
            flag = 1
    except TypeError:
        print("Please enter an integer.")
    except:
        print("Unexpected error, please retry.")
print(age)