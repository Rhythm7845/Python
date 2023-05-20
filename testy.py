import os
ls = os.listdir()

for i in ls:
    if "ex" in i.lower():
        os.system("git mv "+i+" ./ex/")
    elif "dec" in i.lower():
        os.system("git mv "+i+" ./BinaryDecimal/")