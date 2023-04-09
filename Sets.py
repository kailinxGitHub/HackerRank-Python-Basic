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
def setactions(): 
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
        return sum(s)

#Set .union() Operation
n = int(input())
a = set(str(input()).split(" "))
b = int(input())
c = set(str(input()).split(" "))
y = set(a.union(c))
print(len(y))

#Set .intersection() Operation
n = int(input())
a = set(str(input()).split(" "))
b = int(input())
c = set(str(input()).split(" "))
y = set(a.intersection(c))
print(len(y))

#Set .difference() Operation
n = int(input())
a = set(str(input()).split(" "))
b = int(input())
c = set(str(input()).split(" "))
y = set(a.difference(c))
print(len(y))

#Set .symmetric_difference() Operation
n = int(input())
a = set(str(input()).split(" "))
b = int(input())
c = set(str(input()).split(" "))
y = set(a.symmetric_difference(c))
print(len(y))

#Set Mutations
A = int(input())
Aset = set(map(int, input().split()))
N = int(input())

if len(set(Aset)) in range(0, 1000) and N in range(0, 100):
    for i in range(N):
        command = input().split()
        Bset = set(map(int, input().split()))
        if len(Bset) in range(0, 100):
            if command[0] == "update":
                Aset.update(Bset)
            elif command[0] == "intersection_update":
                Aset.intersection_update(Bset)
            elif command[0] == "difference_update":
                Aset.difference_update(Bset)
            elif command[0] == "symmetric_difference_update":
                Aset.symmetric_difference_update(Bset)
    print(sum(Aset))

#The Captain's Room


#Check Subset

#Check Strict Superset