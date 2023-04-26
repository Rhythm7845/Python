# Code by The-Parth
def dec_to_bin(n):
    st = ""
    while n > 0:
        st = str(n%2) + st
        n //= 2
    return st

n = int(input("Enter a number: "))
print(dec_to_bin(n))