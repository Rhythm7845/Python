def reverse(x):
    return(x[::-1])

def bintodec():
    bin = str(reverse(input("Enter a number in binary: ")));n = len(bin);a = 0;dec = 0

    while (a < n):
        b = bool(int(bin[a]))
        if(b == True):
            dec = dec + 2**a
        a = a + 1
    print("The number in decimal form is:", dec)
    
def dectobin(n):
    return "{0:b}".format(int(n))

choice = input("Do you want to enter a decimal number or binary number? d/b: ")
if(choice == "d"):
    n = int(input("Enter a decimal number: "))
    print("The decimal form is:", dectobin(n))
    quit()
elif(choice == "b"):
    bintodec()
    quit()
else:
    print("Enter d or b only")
    quit()