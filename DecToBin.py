#Initialising Dictionaries.
bin_dic_str = dict()
bin_dic_int = dict()
bin_dic_fin = dict()

#Function to find the highest power of two less than dec_temp.

def nearest_power_of_2(dec_temp):
    power = 0
    while (dec_temp > 2 ** power):
        power +=1
    if power == 0:
        bin_dic_str[str(power)] = 1
        bin_dic_int[power] = 1
        return power
    else:
        bin_dic_str[str(power-1)] = 1
        bin_dic_int[power-1] = 1
        return power-1

dec = int(input("Enter decimal number: "))

#loop to call nearest_power_of_2 function and subtract the value from dec.

while (dec > 0):
    dec = int(dec - 2**(nearest_power_of_2(dec)))
    
#loop to add the missing powers of two to the dictionary and sorting it reverse numerically.
    
for powers_of_two in range(max(bin_dic_int.keys()),):
    if powers_of_two not in bin_dic_int.keys():
        bin_dic_str[str(powers_of_two)] = 0

for key in sorted(bin_dic_str, reverse=True):
    bin_dic_fin[key] = bin_dic_str[key]

print(bin_dic_fin.values())