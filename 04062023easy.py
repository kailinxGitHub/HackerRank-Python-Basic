#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a in range(10**10):
        if b in range(1, 10**10):
            print(a+b)
            print(a-b)
            print(a*b)

#Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a/b))
    print(float(a/b))

#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(5):
        print(i)
        print(i**2)

#Print Function
if __name__ == '__main__':
    n = int(input())
    list = []
    if n in range(1,150):
        for i in range(n):
            list.append(i+1)
        print(*list, sep='')

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