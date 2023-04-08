#Python If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if n in range(1,101):
        if n%2 == 0:
            if n in range(2,6):
                print("Not Weird")
            elif n in range(6, 21):
                print("Weird")
            elif n > 20:
                print("Not Weird")
        else:
            print("Weird")

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

#Write a Function
def is_leap(year):
    leap = False
    if year in range(1900, 1000001):
        if year%4 == 0:
            if year%100 == 0:
                if year%400 != 0:
                    leap = False
                else: 
                    leap = True
            else:
                leap = True
        else:
            leap = False
    return leap

year = int(input())
print(is_leap(year))

#Print Function
if __name__ == '__main__':
    n = int(input())
    list = []
    if n in range(1,150):
        for i in range(n):
            list.append(i+1)
        print(*list, sep='')
