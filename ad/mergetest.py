import math
def mergeSort(A,p,r):
    print(f"mergeSort called:A:{A},p:{p},r:{r}")
    if p>=r:
        print("p >= q, exiting mergeSort")
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

a = [3,4,1,5]
print(a)
mergeSort(a,0,len(a)-1)
print(a)