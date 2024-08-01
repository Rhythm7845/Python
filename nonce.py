import sha256 as sh
import random
import time
import matplotlib.pyplot as plt
def list2String(s):
    string = ""
    for i in s:
        string += i
    return string

def stringChecker(difficulty, hash):
    x = 0
    for i in range(1, difficulty+1):
        if hash[i] == '0':
            x+=1
        else:
            continue
    if x == difficulty:
        return True
    else:
        return False

data = 8534564864738975269436789
nonce = 0
difficulty = 2
#print(list2String(sh.sha_256(str(data))))
#print(stringChecker(difficulty, list2String(sh.sha_256(str(data + nonce)))))
x = [1, 2, 3]
y = []
for i in range(1,4):
    flag = True
    startTime = time.time()
    while(flag):
        currentHash = list2String(sh.sha_256(str(data + nonce)))
        if stringChecker(i, currentHash):
            print("The nonce number is:", nonce)
            print("Final hash is:", currentHash)
            flag = False
        else:
            print(currentHash)
            nonce = random.randint(0, 10000000000000)
    endTime = time.time()
    print("Total time take:", (endTime - startTime), "Seconds")
    y.append(endTime - startTime)
plt.plot(x, y)
plt.show()