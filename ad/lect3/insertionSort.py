import time
import random
def insertionSort(a):

    time1 = time.perf_counter()

    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key

    time2 = time.perf_counter()
    fTime = time2-time1

    return fTime

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
        print(a2[i]/(args[i]*args[i]))
    print("random sorted:")
    for i in range(0,len(a3)):
        print(a3[i]/(args[i]*args[i]))

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
            t += insertionSort(sorted(arrays[i]))

        print(f"For sorted array #{i}: t:{t/3} with elements of {len(arrays[i])}")
        sortedTimes.append(t/3)

    #unsort arrays
    for i in range(0,len(arrays)):
        t = 0
        for j in range(0,3):
            t += insertionSort(sorted(arrays[i],reverse=True))

        print(f"For unsorted array #{i}: t:{t/3} with elements of {len(arrays[i])}")
        unSortedTimes.append(t/3)

    for i in range(0,len(arrays)):
        t = 0
        for j in range(0,3):
            t += insertionSort(arrays[i])
        
        print(f"For randomly sorted array #{i}: t:{t/3} with elements of {len(arrays[i])}")
        randomSortedTimes.append(t/3)

    complexity(sortedTimes,unSortedTimes,randomSortedTimes,nVals)


def main(args):
    calcTimeComplexity(args)

if __name__ == "__main__":
    main(args=[1000,2000,4000,8000,16000])