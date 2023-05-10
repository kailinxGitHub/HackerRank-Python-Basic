from itertools import combinations

string = "HACK 2"
list1 = [i for i in string if i != " "][:-1]
number = list[-1]
# print(list(combinations(list1[:-1],int(number[-1]))))
# for i in list(combinations(list1,1)).sort(): print(i)
# for i in list(combinations(list1,2)).sort(): print(i)
print(list(combinations(list1,1)))