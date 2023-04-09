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
n = int(input())
s = set(map(int, input().split()))
N = int(input())
if n in range(0, 20) and N in range(0, 20):
    for i in range(N):
        command = str(input()).split(" ")
        if command[0] == "pop":
            s.pop()
        elif command[0] == "remove":
            s.remove(int(command[1]))
        elif command[0] == "discard":
            s.discard(int(command[1]))
    print(sum(s))

#Set .union() Operation


#Set .intersection() Operation

#Set .difference() Operation

#Set .symmetric_difference() Operation

#Set Mutations

#The Captain's Room

#Check Subset

#Check Strict Superset