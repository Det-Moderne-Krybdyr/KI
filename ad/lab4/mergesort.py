import math
import random
import time
def mergeSort(A,p,r):
    print("mergeSort called:A:{A},p:{p},r:{r}")
    if p>=r:
        return
    q = math.floor((p+r)/2)
    print(f"calling mergeSort: A:{A}, p:{p},q:{q}")
    mergeSort(A,p,q)
    print(f"calling mergeSort: A:{A}, q+1::{q+1},r:{r}")
    mergeSort(A,q+1,r)
    print(f"calling merge: A{A},p:{p},q:{q},r:{r}")
    merge(A,p,q,r)
    return A

def merge(A,p,q,r):
    print(f"merge called A:{A},p:{p},q:{q},r:{r}")
    nl = q-p + 1
    nr = r - q
    l = [0] * (nl)
    r = [0] * (nr)
    for i in range(0,nl):
        l[i] = A[p+i]
    for j in range(0,nr):
        r[j] = A[q+j+1]
    i = 0
    j = 0
    k = p

    while i<nl and j<nr:
        if l[i] <= r[j]:
            A[k] = l[i]
            i+=1
        else:
            A[k] = r[j]
            j+=1
        k+=1
    
    while i<nl:
        A[k] = l[i]
        i+=1
        k+=1
    while j < nr:
        A[k] = r[j]
        j +=1
        k +=1
    print(f"merge exited...")

def randomArray(size):
    array = []
    for i in range(0,size):
        array.append(random.randint(0,10000))
    return array

def complexity(a1,a2,a3,args):
    print("sorted: ")
    for i in range(0,len(a1)):
        print(a1[i]/args[i])
    print("unsorted:")
    for i in range(0,len(a2)):
        print(a2[i]/(args[i]*math.log2(args[i])))
    print("random sorted:")
    for i in range(0,len(a3)):
        print(a3[i]/(args[i]*math.log2(args[i])))

def calcTimeComplexity(nVals):
    arrays = []
    sortedTimes = []
    unSortedTimes = []
    randomSortedTimes = []
    #generate arrays with n elements for each n value
    for n in nVals:
        arrays.append(randomArray(n))

    #sort arrays
    for i in range(0,len(arrays)):
        t = 0
        for j in range(0,3):
            a = sorted(arrays[i])
            time1 = time.perf_counter()
            mergeSort(a,0,len(a)-1)
            time2 = time.perf_counter()
            t+=time2-time1

        print(f"For sorted array #{i}: t:{t/3} with elements of {len(arrays[i])}")
        sortedTimes.append(t/3)

    #unsort arrays
    for i in range(0,len(arrays)):
        t = 0
        for j in range(0,3):
            a = sorted(arrays[i],reverse=True)
            time1 = time.perf_counter()
            mergeSort(a,0,len(a)-1)
            time2 = time.perf_counter()
            t+=time2-time1

        print(f"For unsorted array #{i}: t:{t/3} with elements of {len(arrays[i])}")
        unSortedTimes.append(t/3)

    for i in range(0,len(arrays)):
        t = 0
        for j in range(0,3):
            a = arrays[i]
            time1 = time.perf_counter()
            mergeSort(a,0,len(a)-1)
            time2 = time.perf_counter()
            t+=time2-time1
        
        print(f"For randomly sorted array #{i}: t:{t/3} with elements of {len(arrays[i])}")
        randomSortedTimes.append(t/3)

    complexity(sortedTimes,unSortedTimes,randomSortedTimes,nVals)

def main(args):
    calcTimeComplexity(args)

if __name__ == "__main__":
    main(args=[10,20,40,80,160])