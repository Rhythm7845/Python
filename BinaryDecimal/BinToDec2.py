# Get the number in binary
binary = input("Enter binary number: ")

# Code by The-Parth @ Github
# Check if the number is binary
for i in binary:
    if i not in "01":
        print("Invalid input")
        exit(0)

decimal = 0 # Initialize the decimal number

# Loop through the binary number and convert it to decimal
for i in binary:
    decimal = decimal*2 + int(i)

# Print the decimal number
print("The number in decimal form is:", decimal)