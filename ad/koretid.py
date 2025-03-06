import random

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
                discovered.append([arr[i]])
                k+=1
                continue
            while(val != i):
                val = arr[val]
                discovered.append(val)
            k+=1

        return n,k,arr