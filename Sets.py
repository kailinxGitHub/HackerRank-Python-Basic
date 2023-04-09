#Introduction to Sets
def average(array):
    if n in range(0, 101):
        array = set(arr)
        return sum(array)/len(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#Symmetric Difference
def symmetricdiff(m,a,n,b):
    list = a.difference(b).union(b.difference(a))
    nums = [int(i) for i in list]
    nums.sort()
    for i in nums:
        print(i)

m = int(input())
a = set(str(input()).split(" "))
n = int(input())
b = set(str(input()).split(" "))
symmetricdiff(m,a,n,b)

#Set .add()
def add():
    n = int(input())
    myset = set()
    if n in range(0, 1000):
        for i in range(n):
            myset.add(str(input()))
    print(len(myset))

add()

#Set .discard(), .remove() & .pop()

#Set .union() Operation

#Set .intersection() Operation

#Set .difference() Operation

#Set .symmetric_difference() Operation

#Set Mutations

#The Captain's Room

#Check Subset

#Check Strict Superset