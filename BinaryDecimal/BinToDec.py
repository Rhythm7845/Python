#Function to reverse strings. This is used to reverse the binary number so that it can be read from left to right.
def reverse(temp_binary):
    return(temp_binary[::-1])

#Inputs a binary number and reverses it using the above function. Also initializes the variables used in the loop.

binary_num = str(reverse(input("Enter power number in binary: ")));n = len(binary_num)
power = 0
decimal_number = 0

#Converts the binary number to decimal_number. Can be done via recursion, but I chose to do it this way.

while (power < n):
    bin_bool = bool(int(binary_num[power]))    #bin_bool is a boolean variable that is True if the digit of the inary number is 1 and False if the digit is 0.
    if(bin_bool == True):
        decimal_number = decimal_number + 2**power   #Adds 2 to the power of the digit to the decimal number.
    power +=1
    
#Prints the decimal_number number.

print("The number in decimal_number form is:", decimal_number)
