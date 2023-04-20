#itertools.product()
from itertools import product

inputA = input()
listA = inputA.split()
A = [int(i) for i in listA]

inputB = input()
listB = inputB.split()
B = [int(j) for j in listB]

prod = list(product(A,B))

for t in prod:
    print(t, end=" ")

#itertools.permutations()

#itertools.combinations()

#itertools.combinations_with_replacement()

#Compress the String!

#Iterables and Iterators

#Maximize It!

