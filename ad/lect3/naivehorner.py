import math

def calcPow(x,powVal):
    if(powVal == 0):
        return 1
    sum = 1
    for i in range(0,powVal):
        sum = sum * x
    return sum
def naive(A,x):
    sum = 0
    for i in range(0,len(A)):
        sum += A[i]*calcPow(x,i)
    return sum
def main():
    array = [1,5,3,5,1,8,3]
    res = naive(array,3)
    print(res)

if __name__ == "__main__":
    main()