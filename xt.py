aa = dict()
ab = dict()
ac = dict()
def ad(ae):
    af = 0
    while (ae > 2 ** af):
        af +=1
    if af == 0:
        aa[str(af)] = 1
        ab[af] = 1
        return af
    else:
        aa[str(af-1)] = 1
        ab[af-1] = 1
        return af-1
ag = int(input("Enter decimal number: "))
while (ag > 0):
    ag = int(ag - 2**(ad(ag)))
for ah in range(max(ab.keys()),):
    if ah not in ab.keys():
        aa[str(ah)] = 0
for key in sorted(aa, reverse=True):
    ac[key] = aa[key]
print(ac.values())