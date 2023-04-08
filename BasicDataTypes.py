
#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    xlist = [i for i in range(0,x+1)]
    ylist = [j for j in range(0,y+1)]
    zlist = [k for k in range(0,z+1)]
    perm = [[i, j, k] for i in xlist for j in ylist for k in zlist if i+j+k!=n]
    print(perm)

#Find the Runner-Up Score!
#Trial 1
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newlist = []
    for i in arr:
        if n in range(2, 10) and i not in newlist:
            newlist.append(i)
    newlist.sort(reverse=True)
    print(newlist[1])
#Trial 2: 
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newlist = [i for i in arr if n in range(2, 10) and i not in newlist]
    newlist.sort(reverse=True)
    print(newlist[1])
#Working
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in range(n):
        if arr[i] > arr[i+1]:
            print(arr[i+1])
            break

#Nested Lists
if __name__ == '__main__':
    studentlist = []
    listrange = int(input())
    if 2 <= listrange <= 5:
        for _ in range(listrange):
            name = input()
            score = float(input())
            innerlist = [name, score]
            studentlist.append(innerlist)
        uniquescore = []
        for i in studentlist:
            if i[1] not in uniquescore:
                uniquescore.append(i[1])
        sorted = uniquescore.sort()
        names = []
        for k in studentlist:
            if k[1] == uniquescore[1]:
                names.append(k[0])
        names.sort()
        for y in names:
            print(y)

#Finding The Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if n in range(2,11):
        nums = []
        for i in student_marks:
            if i == query_name:
                nums.append(student_marks[i])
        if len(nums[0]) == 3:
            floatnums = [float(j) for j in nums[0] if 0.00 <= j <= 101.00]
            print(format(sum(floatnums)/3, ".2f"))

#Lists
if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        command = str(input())
        split_command = command.split()
        if split_command[0] == "insert":
            list.insert(int(split_command[1]), int(split_command[2]))
        elif split_command[0] == "print":
            print(list)
        elif split_command[0] == "remove":
            list.remove(int(split_command[1]))
        elif split_command[0] == "append":
            list.append(int(split_command[1]))
        elif split_command[0] == "sort":
            list.sort()
        elif split_command[0] == "pop":
            list.pop()
        elif split_command[0] == "reverse":
            list.reverse()
            
#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(tuple(integer_list).__hash__())


