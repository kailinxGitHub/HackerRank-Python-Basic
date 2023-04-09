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

#No Idea!
n, m = input().split()
n_int = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(sum((i in A)-(i in B) for i in n_int))

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
K = int(input())
unord = list(map(int, input().split()))

if K in range(1, 1000):
    unique = set()
    multiple = set()
    for i in unord:
        if i in unique:
            multiple.add(i)
        else:
            unique.add(i)
    joint = list(unique.difference(multiple))
    print(joint[0])

#Check Subset
T = int(input())

for i in range(T):
    ele_a = int(input())
    set_a = set(map(int, input().split()))
    ele_b = int(input())
    set_b = set(map(int, input().split()))
    if T in range(0, 21) and (len(set_a) and len(set_b)) in range(0, 1001):
        if set_a.issubset(set_b):
            print(True)
        else:
            print(False)

#Check Strict Superset
set_a = set(map(int, input().split()))

n = int(input())
master_set = []
for i in range(n):
    temp_set = set(map(int, input().split()))
    answer = set_a.issuperset(temp_set)
    temp_full = temp_set, answer
    master_set.append(temp_full)
status = True
for j in range(len(master_set)):
    if master_set[j][1] == False:
        status = False
    else: 
        continue
print(status)
