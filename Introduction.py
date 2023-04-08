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
