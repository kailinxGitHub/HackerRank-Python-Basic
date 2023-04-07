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
line1 = int(input())
line2 = str(input())
slicedline2 = line2.split()
l2v1 = int(slicedline2[0])
l2v2 = int(slicedline2[1])
t = tuple(line1) + tuple(l2v1, l2v2)
tup = tuple(t)
print(hash(tup))

#sWAP cASE
def swap_case(s):
    sentence = []
    if len(s) in range(0,1001):
        for letter in s:
            if letter.isupper():
                sentence.append(letter.lower())
            elif letter.islower():
                sentence.append(letter.upper())
            else:
                sentence.append(letter)
    return ''.join(sentence)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join
def split_and_join(line):
    words = line.split()
    joinedwords = '-'.join(words)
    return joinedwords

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?
def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations
def mutate_string(string, position, character):
    letterslist = [letter for letter in string]
    letterslist[position] = character
    return ''.join(letterslist)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Find a String
def count_substring(string, sub_string):
    innercount = 0
    sunique = set()
    newstring = [i for i in string if i not in sunique and not sunique.add(i)]
    ssunique = set()
    newsub_string = [j for j in sub_string if j not in ssunique and not ssunique.add(j)]
    for k in newstring:
        for z in newsub_string:
            if k == z:
                innercount += 1
    return innercount

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)





