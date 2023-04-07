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
            vari = int(split_command[1])
            vare = int(split_command[2])
            list.insert(vari, vare)
        elif split_command[0] == "print":
            print(list)
        elif split_command[0] == "remove":
            vare = int(split_command[2])
            for j in list:
                if j == vare:
                    list.remove(j)
        elif split_command[0] == "append":
            vare = int(split_command[2])
            list[-1].append(vare)
        elif split_command[0] == "sort":
            list.sort()
        elif split_command[0] == "pop":
            list[-1].pop()
        elif split_command[0] == "reverse":
            list.sort(reverse=True)
        else:
            continue
            
            
        