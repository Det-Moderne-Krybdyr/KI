import random
import time
class Permutation:

    def permutation(n):

        k = n - 1
        arr = []
        for i in range(0,n):
            arr.append(i)
        random.shuffle(arr)

        k = 0
        discovered = []
        for i in range(0,n):
            val = arr[i]
            if(val in discovered):
                continue
            if(val == i):
                discovered.append(str([arr[i]]))
                k+=1
                continue
            while(val != i):
                val = arr[val]
                discovered.append(val)
            k+=1

        return n,k,arr

    def stats():
        pass

num = 1000000
data = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    19: 0,
    20: 0,
    21: 0,
    22: 0,
    23: 0,
    24: 0,
    25: 0
}

probabilities = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    19: 0,
    20: 0,
    21: 0,
    22: 0,
    23: 0,
    24: 0,
    25: 0
}

def average(data,amount):
    sum = 0
    for i in range(0,len(data)):
        sum+=(i+1)*data[i+1]  
    return sum
t0 = time.time()
for i in range(0,num):
    n,k,arr = Permutation.permutation(64)
    data[k] += 1
t = time.time() - t0
print(f"time: {t}")
probsum = 0
for i in range(0,len(data)):
    prob = data[i+1]/num
    probabilities[i+1] = prob
    probsum += prob

print(f"raw data: {data}")
print(f"probabilities for k cycles: {probabilities}")
print(f"sum that should be 1: {probsum}")
print(f"average: {average(probabilities,num)}")
